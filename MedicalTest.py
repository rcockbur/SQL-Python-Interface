#Medical Test module

import random
import cx_Oracle


con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")
cur = con.cursor()

#Get a list of the patient number and test type for each result that has not been completed.
patient = "SELECT patient_no, test_name FROM test_record tr, test_type tt WHERE tr.type_id = tt.type_id AND result IS NULL"
cur.execute(patient)
rows = cur.fetchall()

again = True
while again:
	patient_no = int(input('Enter the health care number of the patient: '))
	test_type = str(input('Enter the test type of the test: '))
	combined = (patient_no , test_type)

	valid = False
	for i in rows:
		print(i)
		if i == combined:
			valid = True

	if not valid:
		yn = input("This record is not in the database, would you like to try again? (y/n) ")
		if yn == "n":
			again = False
			exit()
	if valid:
		again = False

lab_name = input('Enter your lab name: ')
test_id = input('Enter the Id of the test ')
test_result = input('Enter the result of the test: ')


cur.execute("UPDATE test_record SET result = :result WHERE test_id = :test_id", {'result' : str(test_result), 'test_id' :int(test_id)})


con.commit()
con.close()
