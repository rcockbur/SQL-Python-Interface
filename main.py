import sys
import gp1_main
import prescription
import MedicalTest
import PatientInformationUpdate
import SearchEngine

username = input("Enter your Username: ")
password = input("Enter your Password: ")

while(1):
	print('')
	print('Main Menu')
	print('1. Prescribe a Test')
	print('2. Enter Test Results')
	print('3. Patient Manager')
	print('4. Search Engine') #returns all test rest results 
	print('5. Quit Application')
	i = input('Select Option (1-5):')
	print('')

	while(1):	
		if i == '1':
			p = prescription.Prescription(username,password)
			break;

		elif i == '2':
			mt = MedicalTest.MedicalTest(username,password)
			break;

		elif i == '3':
			u = PatientInformationUpdate.Update(username,password)
			break;

		elif i == '4':
			se = SearchEngine.SearchEngine(username,password)
			break;

		elif i == '5':
			exit()

		else: 
			i = input('Invalid Entry, Select Option 1-6:')


