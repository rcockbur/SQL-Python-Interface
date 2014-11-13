#used to perform searches
import cx_Oracle
quote = """'"""
class SearchEngine(object):
	def __init__(self):
		super(SearchEngine, self).__init__()
		self.con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")
		self.curs = self.con.cursor()


		while(1):
			print('Search Engine:')
			print('1. List test records for a particular patient')
			print('2. List of Prescribed tests of a given doctor during a specified time span')
			print('3. List the patients who have reached the alarming age for a particular test')
			print('4. Return to main menu')

			i = input('Please select an option (1-4):')

			if i == '1':
				self.searchPatient()
			elif i == '2':
				self.searchDoctor()
			elif i == '3':
				self.alarmingAge()
			elif i == '4':
				break
			else: 
				print('Invalid entry')

		self.curs.close()
		self.con.close()
		print('complete search engine')



	def searchPatient(self):
		self.curs.execute("SELECT distinct health_care_no, name FROM patient")
		patients = self.curs.fetchall()
		patient_nos = [i[0] for i in patients] 	
		while True:
			health_care_no = int(input("Enter the patient's health care number: "))
			if health_care_no in patient_nos:
				break
			self.cont = input("That patient number is not on file, would you like to try again (Y/N): ")          
			if self.cont == 'N':
				return	
		self.curs.execute("SELECT p.name, tt.test_name, t.test_date, t.result FROM patient p, test_record t, test_type tt WHERE t.type_id = tt.type_id AND p.health_care_no = t.patient_no AND t.patient_no = %d" %(health_care_no,))
		test_list = self.curs.fetchall()
		if test_list == None:
			print("that patient has no test records")
		for row in test_list:
			print('Health Care Number: ' +str(health_care_no))
			print('Name: ' + row[0])
			print('Test Name: ' + row[1])
			print('Testing Date: ' + str(row[2].year) +'-'+ str(row[2].month) +'-'+ str(row[2].day))
			print('Test Result: ' + row[3])
			print('')	
		
	def searchDoctor(self):
		start_date = input('Enter the starting date(YYYY-MM-DD): ')
		end_date = input('Enter the end date(YYYY-MM-DD): ')
		sdate = start_date.split('-')
		edate = end_date.split('-')
		self.curs.execute("SELECT distinct employee_no name FROM doctor")
		doctors = self.curs.fetchall()
		doctor_nos = [i[0] for i in doctors] 	
		while True:
			employee_no = int(input("Enter doctor's employee number: "))
			if employee_no in doctor_nos:
				break
			self.cont = input("That employee number is not on file, would you like to try again (Y/N): ")          
			if self.cont == 'N':
				return	
		self.curs.execute("SELECT t.patient_no, p.name, tt.test_name, t.prescribe_date FROM patient p, test_record t, test_type tt WHERE t.type_id = tt.type_id AND p.health_care_no = t.patient_no AND t.employee_no = %d AND t.prescribe_date >= to_date('%d-%d-%d', 'YYYY-MM-DD') AND t.prescribe_date <= to_date('%d-%d-%d', 'YYYY-MM-DD')" %(employee_no,int(sdate[0]),int(sdate[1]), int(sdate[2]), int(edate[0]), int(edate[1]), int(edate[2])))
		test_list = self.curs.fetchall()
		print(' ')
		if test_list == None:
			print("that doctor has not prescribed any tests")
		for row in test_list:
			print('Health Care Number: ' +str(row[0]))
			print('Name: ' + row[1])
			print('Test Name: ' + row[2])
			print('Prescribe Date: ' + str(row[3].year) +'-'+ str(row[3].month) +'-'+ str(row[3].day))
			print('')	

	def alarmingAge(self):
		testType = quote + input('Which test are inquiring about?') + quote
		print('')
		
		self.curs.execute('SELECT * FROM test_type WHERE test_name = %s' % (testType,))

		row = self.curs.fetchone()
		type_id = row[0]
		#print('type is ' + str(type_id))

		f = open('engine.sql')
		statementsFile = f.read()
		statements = statementsFile.split(';')

		try: self.curs.execute(statements[0])
		except: pass
		self.curs.execute(statements[1])
		self.curs.execute(statements[2])

		results = self.curs.fetchall()
		print('The following patients should schedule a test')
		n = 'Name:   '
		a = 'Adress: '
		p = 'Phone:  '
		for result in results:
			#print(result[3])
			if result[3] == type_id:
				print(n + result[0])
				print(a + result[1])
				print(p + result[2])
				print('')
		#print(x)

		#for statement in statements:
		#	if statement == '\n':
		#		continue
		#	print(statement)
		#	self.curs.execute(statement)
		#	x = self.curs.fetchall()
		#	print('')
		#	print(x)


		#print(statements[1])
		#self.curs.execute(statements[1])
		#self.curs.execute(statements[2])
		#print(statements[2])
		#x = self.curs.fetchall()
		#print(x)


