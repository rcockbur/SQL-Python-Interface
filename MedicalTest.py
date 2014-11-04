#Medical Test module

import random
import cx_Oracle


con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")
cur = con.cursor()



health_care_number = int(input('Enter the health care number of the patient: '))
employee_number = int(input('Enter the employee number of the doctor: '))

patient = "select patient_no from test_record"
cur.execute(patient)
pat_rows = cur.fetchall()
pat = []
pat_list = []
for i in pat_rows:
	for j in i:
		if j == ',' or j == '(' or j == ')':
			continue
		else:
			pat.append(j)
	pat_list.append(int(j))

'''SQL CODE:
select patient_no, test_name from test_record tr, test_type tt
where tr.type_id = tt.type_id and
result IS NULL;
'''

doctor = "select employee_no from test_record"
cur.execute(doctor)
doc_rows = cur.fetchall()
doc = []
doc_list = []
for i in doc_rows:
	for j in i:
		if j == ',' or j == '(' or j == ')':
			continue
		else:
			doc.append(j)
	doc_list.append(int(j))

for i in pat_list:
	if i == health_care_number:
		print("Yes")

'''
lab_name = input('Enter your lab name: ')
test_date = input('Enter the date of the test: ')
test_result = input('Enter the result of the test: ')
'''
'''
cur.execute(INSERT INTO test_record 
                VALUES(:test_id, :type_id, :patient_no, :employee_no, 
                :medical_lab, :result, :prescribe_date, :test_date,{"test_id":test_id, "type_id":int(type_id), "patient_no":int(patient_no), "employee_no":int(employee_no), 
                "medical_lab":medical_lab, "result":NULL, "prescribe_date":prescribe_date, "test_date":test_date})
'''
con.commit()
con.close()
