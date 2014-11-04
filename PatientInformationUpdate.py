#This component is used to enter the information of a new patient or to update the information of an existing patient. All the information about a patient, except the health_care_no for an existing patient, may be updated.

import cx_Oracle

con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")
cur = con.cursor()

quote = """'"""

def addPatient():
	hcn = input('Enter patients healthcare number:') + ','	
	name = quote + input('Enter patient name:') + quote + ','
	address = quote + input('Enter patients address:') + quote + ','

	year = quote + input('Enter patients year of birth:') + '-'
	month = input('Enter patients month of birth (01-12):') + '-'
	day = input('Enter patients day of birth:') + quote
	birthday =  '(' + year + month + day + ',' + 'YYYY-MM-DD' + ')' + ','

	phone = quote + input('Enter patients phone number:') + quote

	s0 = 'insert into patient values('
	s1 = 'to_date'
	s2 = ')'

	command = s0 + hcn + name + address + s1 + birthday + phone + s2
	print(command)
	cur.execute(command)

print('Patient Update')
print('1. Add new patient')
print('2. Update existing patient')
i = input('Please select an option (1/2):')

while(1):
	if i == '1':
		addPatient()
		print(i)
		break;
	elif i == '2':
		#doSomething
		print(i)
		break;
	else: 
		i = input('Invalid entry, select option (1/2):')

curs.close()
con.close()
print('complete patient info update')




		
