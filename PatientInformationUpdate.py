#This component is used to enter the information of a new patient or to update the information of an existing patient. All the information about a patient, except the health_care_no for an existing patient, may be updated.

import cx_Oracle

con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")
curs = con.cursor()
quote = """'"""

def addPatient():
	hcn = input('Enter patients healthcare number:') + ','	
	name = quote + input('Enter patient name:') + quote + ','
	address = quote + input('Enter patients address:') + quote + ','

	year = quote + input('Enter patients year of birth:') + '-'
	month = input('Enter patients month of birth (01-12):') + '-'
	day = input('Enter patients day of birth:') + quote
	birthday =  '(' + year + month + day + ',' + quote + 'YYYY-MM-DD' + quote + ')' + ','

	phone = quote + input('Enter patients phone number:') + quote

	s0 = 'insert into patient values('
	s1 = 'to_date'
	s2 = ')'

	command = s0 + hcn + name + address + s1 + birthday + phone + s2
	curs.execute(command)
	con.commit()

def displayRow(row):
	print('Info for patient ' + str(row[0]))
	print('Name:         ' + row[1])
	print('Address:      ' + row[2])
	print('Birthday:     ' + str(row[3].year) +' '+ str(row[3].month) +' '+ str(row[3].day))
	print('Phone Number: ' + row[4])
	print('')

def displayUpdateOptions(row):
	while(1):
		print('Options:')
		print('1. Update name')
		print('2. Update address')
		print('3. Update birthday')
		print('4. Update phone number')
		print('5. Done')
		i = input('Please select an option (1-5):')
		print('')

		if i == '1':
			i = input('Enter name: ')
			command = 'UPDATE Patient SET name=' + quote + i + quote +' WHERE health_care_no=' + str(row[0])
			curs.execute(command)
			con.commit()
			print('Name updated')
			print('')

		elif i == '2':
			i = input('Enter address: ')
			command = 'UPDATE Patient SET address=' + quote + i + quote +' WHERE health_care_no=' + str(row[0])
			curs.execute(command)
			con.commit()
			print('Address updated')
			print('')

		elif i == '3':
			y = input('Enter year: ')
			m = input('Enter month: ')
			d = input('Enter day: ')
			birthday = '(' + quote + y + '-' + m + '-' + d + quote + ','
			temp = 'to_date' + birthday + quote + 'YYYY-MM-DD' + quote + ')'
			command = 'UPDATE Patient SET birth_day=' + temp +' WHERE health_care_no=' + str(row[0])
			print(command)
			curs.execute(command)
			con.commit()
			print('Birthday updated')
			print('')
	
		elif i == '4':
			i = input('Enter phone number: ')
			command = 'UPDATE Patient SET phone=' + quote + i + quote +' WHERE health_care_no=' + str(row[0])
			curs.execute(command)
			con.commit()
			print('Phone number updated')
			print('')

		elif i == '5':
			break
		else: 
			i = input('Invalid entry')

		#curs = con.cursor()

def updatePatient():
	patientNo = input('Enter patients healthcare number:')
	print('')
	curs.execute("SELECT * FROM patient")
	print(curs)
	row = curs.fetchone()
	patientFound = False
	while row:
		#print(row)
		
		if str(row[0]) == patientNo:
			patientFound = True
			displayRow(row)
			#saveCurs = curs
			displayUpdateOptions(row)
			#curs = saveCurs
		print(curs)
		row = curs.fetchone()
	if patientFound == False:
		print("Patient not found")
			



while(1):
	print('Options:')
	print('1. Add new patient')
	print('2. Update existing patient')
	print('3. Done')

	i = input('Please select an option (1-3):')

	if i == '1':
		addPatient()
	elif i == '2':
		updatePatient()
	elif i == '3':
		break
	else: 
		print('Invalid entry')

curs.close()
con.close()
print('complete patient info update')




		
