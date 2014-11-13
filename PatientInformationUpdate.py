#This component is used to enter the information of a new patient or to update the information of an existing patient. All the information about a patient, except the health_care_no for an existing patient, may be updated.

import cx_Oracle
class Update(object):
	def __init__(self, username, password):
		super(Update, self).__init__()
		
		self.con = cx_Oracle.connect(username +"/"+password+"@gwynne.cs.ualberta.ca:1521/CRS")
		self.curs = self.con.cursor()
		self.quote = """'"""

		while(1):
			print('Patient Manager:')
			print('1. Add new patient')
			print('2. Update existing patient')
			print('3. Return to main menu')

			i = input('Please select an option (1-3):')
			print('')

			if i == '1':
				self.addPatient()
			elif i == '2':
				self.updatePatient()
			elif i == '3':
				break
			else: 
				print('Invalid entry')

		self.curs.close()
		self.con.close()

	def addPatient(self):
		hcn = input('Enter patients healthcare number:') + ','	
		name = self.quote + input('Enter patient name:') + self.quote + ','
		address = self.quote + input('Enter patients address:') + self.quote + ','

		year = self.quote + input('Enter patients year of birth:') + '-'
		month = input('Enter patients month of birth (01-12):') + '-'
		day = input('Enter patients day of birth:') + self.quote
		birthday =  '(' + year + month + day + ',' + self.quote + 'YYYY-MM-DD' + self.quote + ')' + ','

		phone = self.quote + input('Enter patients phone number:') + self.quote

		s0 = 'insert into patient values('
		s1 = 'to_date'
		s2 = ')'

		command = s0 + hcn + name + address + s1 + birthday + phone + s2
		self.curs.execute(command)
		self.con.commit()
		print('Patient successfully added')
		print('')

	def displayRow(self, row):
		print('Info for patient ' + str(row[0]))
		print('Name:         ' + row[1])
		print('Address:      ' + row[2])
		print('Birthday:     ' + str(row[3].year) +' '+ str(row[3].month) +' '+ str(row[3].day))
		print('Phone Number: ' + row[4])
		print('')

	def displayUpdateOptions(self, row):
		while(1):
			print('Update Patient:')
			print('1. Update name')
			print('2. Update address')
			print('3. Update birthday')
			print('4. Update phone number')
			print('5. Done')
			i = input('Please select an option (1-5):')
			print('')

			if i == '1':
				i = input('Enter name: ')
				command = 'UPDATE Patient SET name=' + self.quote + i + self.quote +' WHERE health_care_no=' + str(row[0])
				self.curs.execute(command)
				self.con.commit()
				print('Name updated')
				print('')

			elif i == '2':
				i = input('Enter address: ')
				command = 'UPDATE Patient SET address=' + self.quote + i + self.quote +' WHERE health_care_no=' + str(row[0])
				self.curs.execute(command)
				self.con.commit()
				print('Address updated')
				print('')

			elif i == '3':
				y = input('Enter year: ')
				m = input('Enter month: ')
				d = input('Enter day: ')
				birthday = '(' + self.quote + y + '-' + m + '-' + d + self.quote + ','
				temp = 'to_date' + birthday + self.quote + 'YYYY-MM-DD' + self.quote + ')'
				command = 'UPDATE Patient SET birth_day=' + temp +' WHERE health_care_no=' + str(row[0])
				print(command)
				self.curs.execute(command)
				self.con.commit()
				print('Birthday updated')
				print('')
	
			elif i == '4':
				i = input('Enter phone number: ')
				command = 'UPDATE Patient SET phone=' + self.quote + i + self.quote +' WHERE health_care_no=' + str(row[0])
				print(command)
				self.curs.execute(command)
				self.con.commit()
				print('Phone number updated')
				print('')

			elif i == '5':
				break
			else: 
				i = input('Invalid entry')

	def updatePatient(self):
		patientNo = input('Enter patients healthcare number:')
		print('')
		self.curs.execute("SELECT * FROM patient WHERE health_care_no = %s" % (patientNo,))
		row = self.curs.fetchone()
		if row == None:
			patientFound = False
		else:
			patientFound = True
			self.displayRow(row)
			self.displayUpdateOptions(row)
		if patientFound == False:
			print("Patient not found")

