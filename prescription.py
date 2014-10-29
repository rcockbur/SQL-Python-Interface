#Prescription module
import random
import cx_Oracle

con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")

cur = con.cursor()

cur.execute("""SELECT distinct test.id 
               FROM test_record;""")
test_ids = cur.fetchall()
print(test_ids)

test_id = 0

#could we just increment the id from 1 until they stop adding ID's to make it faster?
while test_id == 0:
    t = random.randrange(1000000,9999999)
    if t not in test_ids:
        test_id = t

#employee_no = input('Enter your employee number: ')
#employee_name = input('Enter your name: ')
#test_name = input('Enter the name of the test: ')
#pat_name = input("Enter the patient's name: ")
#pat_no = input("Enter the patient's health care number: ")

#cur.execute(""" INSERT INTO test_record 
                #VALUES(:test_id, :type_id, :patient_no, :employee_no, 
                #:medical_lab, :result, :prescribe_date, :test_date""",{"test_id":test_id, "type_id":type_id, "patient_no":patient_no, "employee_no":employee_no, 
                #"medical_lab":medical_lab, "result":NULL, "prescribe_date":prescribe_date, "test_date":test_date})

con.close()
