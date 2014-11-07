#used to perform searches
import cx_Oracle

con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")
curs = con.cursor()

def searchPatient():
	curs.execute("SELECT distinct health_care_no, name FROM patient")
	patients = curs.fetchall()
	patient_nos = [i[0] for i in patients] 	
	while True:
		health_care_no = int(input("Enter the patient's health care number: "))
		if health_care_no in patient_nos:
			break
		cont = input("That patient number is not on file, would you like to try again (Y/N): ")          
		if cont == 'N':
			return	
	curs.execute("SELECT p.name, tt.test_name, t.test_date, t.result FROM patient p, test_record t, test_type tt WHERE t.type_id = tt.type_id AND p.health_care_no = t.patient_no AND t.patient_no = %d" %(health_care_no,))
	test_list = curs.fetchall()
	if test_list == None:
		print("that patient has no test records")
	for row in test_list:
		print('Health Care Number: ' +str(health_care_no))
		print('Name: ' + row[0])
		print('Test Name: ' + row[1])
		print('Testing Date: ' + str(row[2].year) +'-'+ str(row[2].month) +'-'+ str(row[2].day))
		print('Test Result: ' + row[3])
		print('')	
		
def searchDoctor():
	pass 

def alarmingAge():
	pass


while(1):
	print('Options:')
	print('1. List test records for a particular patient')
	print('2. List of Prescribed tests of a given doctor during a specified time span')
	print('3. List the patients who have reached the alarming age for a particular test')
	print('4. Done')

	i = input('Please select an option (1-4):')

	if i == '1':
		searchPatient()
	elif i == '2':
		searchDoctor()
	elif i == '3':
		alarmingAge()
	elif i == '4':
		break
	else: 
		print('Invalid entry')

curs.close()
con.close()
print('complete search engine')