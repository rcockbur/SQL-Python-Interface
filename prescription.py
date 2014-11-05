#Prescription module
import random
import cx_Oracle

con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")

curs = con.cursor()

#get a list of all the test_ids currently in use
curs.execute("SELECT distinct test_id FROM test_record")
test_ids = curs.fetchall()

#create an array of test_ids
test_ids = [i[0] for i in test_ids]

test_id = 0
#generate a new/random test_id that is unique
while test_id == 0:
    t = random.randrange(1000000,9999999)
    if t not in test_ids:
        test_id = t

curs.execute("SELECT distinct d.employee_no, p.name FROM doctor d, patient p WHERE d.health_care_no = p.health_care_no")
employees = curs.fetchall()

#make separate arrays for employee numbers and names
employee_nos = [i[0] for i in employees]
employees = [i[1] for i in employees]

#find a valid employee name/number
while True:
        employee_no = int(input("Enter your employee number: "))
        if employee_no in employee_nos:
            break
        cont = input("That employee number is not on file, would you like to try again (Y/N): ")          
        if cont == 'N':
            exit()             

#determine the corresponding employee name that goes with the given employee number
i = employee_nos.index(employee_no)
employee_name = employees[i]

#make separate arrays for patient numbers and names
curs.execute("SELECT distinct health_care_no, name FROM patient")
patients = curs.fetchall()
patient_nos = [i[0] for i in patients] 
patient_names = [i[1] for i in patients] 
#find a valid patient name/number
while True:
        patient_no = int(input("Enter the patient's health care number: "))
        if patient_no in patient_nos:
            break
        cont = input("That patient number is not on file, would you like to try again (Y/N): ")          
        if cont == 'N':
            exit() 
            
#determine the corresponding patient name that goes with the given patient number
i = patient_nos.index(patient_no)
patient_name = patient_names[i]

#make separate arrays for test numbers and names
curs.execute("SELECT distinct type_id, test_name FROM test_type")
tests = curs.fetchall()
type_ids = [i[0] for i in tests] 
tests = [i[1] for i in tests] 

print('These are the available tests')
for i in tests:
    print(i)
#find a valid test name/number
while True:
    test_name = input("Enter the name of the test you wish to prescribe: ")
    if test_name in tests:
        break
    cont = input("That test name is not on file, would you like to try again (Y/N): ")          
    if cont == 'N':
        exit()     
        
#determine the corresponding test id that goes with the given test name
i = tests.index(test_name)
type_id = type_ids[i]

#executes update of prescription info 
curs.execute("INSERT INTO test_record VALUES(:test_id, :type_id, :patient_no, :employee_no, NULL, NULL, SYSDATE, NULL)",
             {'test_id':int(test_id), 'type_id':int(type_id), 'patient_no':int(patient_no), 'employee_no':int(employee_no)})

con.commit()
curs.close()
con.close()         
