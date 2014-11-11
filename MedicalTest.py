#Medical Test module

import random
import cx_Oracle
import gp1_main

con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")
cur = con.cursor()

#Get a list of the patient number and test type for each result that has not been completed.
patient = "SELECT patient_no, test_name FROM test_record tr, test_type tt WHERE tr.type_id = tt.type_id AND result IS NULL"
cur.execute(patient)
rows = cur.fetchall()
print(rows)
again = True
while again:
	patient_no = int(input('Enter the health care number of the patient: '))
	test_type = str(input('Enter the test type of the test: '))
	combined = (patient_no , test_type)

	valid = False
	for i in rows:
		if i == combined:
			valid = True

	if not valid:
		yn = input("This record is not in the database, would you like to try again? (y/n) ")
		if yn == "n":
			again = False
			exit()
	if valid:
		again = False

up = 'UPDATE test_record SET '
medical_lab ='medical_lab= ' + "'" + input('Enter your lab name: ') + "'" +  ', '
result = 'result = ' + "'" + input('Enter the result of the test: ') + "'" + ','
test_date = 'test_date= ' + 'to_date(' + "'" + input('Enter the date the test was constructed: (YYYY-MM-DD)') + "'" + ',' +"'"+ 'YYYY-MM-DD' + "'" + ')'
fr = ' WHERE patient_no =' + str(patient_no) +  ' and result IS NULL'
command = up + medical_lab + result + test_date + fr
print(command)



cur.execute(command)


con.commit()
cur.close()
con.close()
