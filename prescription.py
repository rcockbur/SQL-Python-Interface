#Prescription module: allows a doctor to enter a prescription for a patient
#returns a conflict error if that test is not allowed to be taken
import random
import cx_Oracle

class Prescription(object):
    def __init__(self, username, password):
        super(Prescription, self).__init__()
        self.con = cx_Oracle.connect(username +"/"+password+"@gwynne.cs.ualberta.ca:1521/CRS")
        self.curs = self.con.cursor()

        #get a list of all the test_ids currently in use
        self.curs.execute("SELECT distinct test_id FROM test_record")
        self.test_ids = self.curs.fetchall()

        #create an array of test_ids
        self.test_ids = [i[0] for i in self.test_ids]
        self.test_id = 0
        #generate a new/random test_id that is unique
        while self.test_id == 0:
            t = random.randrange(1000000,9999999)
            if t not in self.test_ids:
                self.test_id = t

        self.curs.execute("SELECT distinct d.employee_no, p.name FROM doctor d, patient p WHERE d.health_care_no = p.health_care_no")
        self.employees = self.curs.fetchall()

        #make separate arrays for employee numbers and names
        self.employee_nos = [i[0] for i in self.employees]
        self.employees = [i[1] for i in self.employees]

#find a valid employee name/number
        while True:
            self.employee_no = int(input("Enter your employee number: "))
            if self.employee_no in self.employee_nos:
                break

            cont = input("That employee number is not on file, would you like to try again (Y/N): ")          
            if cont == 'N':
                exit()             

#determine the corresponding employee name that goes with the given employee number
        self.i = self.employee_nos.index(self.employee_no)
        self.employee_name = self.employees[self.i]

#make separate arrays for patient numbers and names
        self.curs.execute("SELECT distinct health_care_no, name FROM patient")
        self.patients = self.curs.fetchall()
        self.patient_nos = [i[0] for i in self.patients] 
        self.patient_names = [i[1] for i in self.patients] 
#find a valid patient name/number
        while True:
            self.patient_no = int(input("Enter the patient's health care number: "))
            if self.patient_no in self.patient_nos:
                break
            cont = input("That patient number is not on file, would you like to try again (Y/N): ")          
            if cont == 'N':
                exit() 
            
#determine the corresponding patient name that goes with the given patient number
        i = self.patient_nos.index(self.patient_no)
        self.patient_name = self.patient_names[i]

#make separate arrays for test numbers and names
        self.curs.execute("SELECT distinct type_id, test_name FROM test_type")
        self.tests = self.curs.fetchall()
        self.type_ids = [i[0] for i in self.tests] 
        self.tests = [i[1] for i in self.tests] 

        self.curs.execute("SELECT distinct type_id FROM not_allowed WHERE health_care_no = %s" % (self.patient_no,))
        self.t = self.curs.fetchall()
        self.not_allowed = [i[0] for i in self.t]    
#find a valid test name/number
        while True:
            while True:
                self.test_name = input("Enter the name of the test you wish to prescribe: ")
                if self.test_name in self.tests:
                    break
                cont = input("That test name is not on file, would you like to try again (Y/N): ")          
                if cont == 'N':
                    exit()     
            i = self.tests.index(self.test_name)
            self.type_id = self.type_ids[i]
            if self.type_id in self.not_allowed:
                print("this patient is not allowed to take this test.")
                while self.type_id in self.not_allowed:
                    cont = input("Would you like to prescribe another test for this patient?(Y/N): ")
                    if cont == 'Y':
                        break
                    elif cont =='N':
                        exit()
                    else:
                        print("invalid answer")
                        continue
            else:
                break

#executes update of prescription info 
        self.curs.execute("INSERT INTO test_record VALUES(:test_id, :type_id, :patient_no, :employee_no, NULL, NULL, SYSDATE, NULL)",
             {'test_id':int(self.test_id), 'type_id':int(self.type_id), 'patient_no':int(self.patient_no), 'employee_no':int(self.employee_no)})

        self.con.commit()
        self.curs.close()
        self.con.close()         
