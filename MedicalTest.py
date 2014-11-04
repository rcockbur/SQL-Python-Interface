#Medical Test module

import random
import cx_Oracle

con = cx_Oracle.connect("msumner/c1234567@gwynne.cs.ualberta.ca:1521/CRS")

cur = con.cursor()

question = True
while question:
	print("Input the number corresponding to the data you would like to enter.")
	print("1. Health care number of the patient")
	print("2. Employee number of the doctor")
	choice = input()
	if choice == '1':
		health_care_number = input('Enter the health care number of the patient: ')
	if choice == '2':
		employee_number = input('Enter the employee number of the doctor: ')
	again = input("Would you like to enter more data? (y/n) ")
	if again == 'n':
		question = False

lab_name = input('Enter your lab name: ')
test_date = input('Enter the date of the test: ')
test_result = input('Enter the result of the test: ')

cur.execute(INSERT INTO test_record 
                VALUES(:test_id, :type_id, :patient_no, :employee_no, 
                :medical_lab, :result, :prescribe_date, :test_date,{"test_id":test_id, "type_id":type_id, "patient_no":patient_no, "employee_no":employee_no, 
                "medical_lab":medical_lab, "result":NULL, "prescribe_date":prescribe_date, "test_date":test_date})

con.close()
