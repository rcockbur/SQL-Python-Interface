import cx_Oracle

class gp1_main(object):
	def __init__(self,username,password):
		super(gp1_main, self).__init__()

		con = cx_Oracle.connect(username +"/"+password+"@gwynne.cs.ualberta.ca:1521/CRS")
		
		curs = con.cursor()

		#opens file of create/drop table statements
		f = open('project_setup.sql')
		full_sql = f.read()
		table_creation = full_sql.split(';')

		#reads in each individual statement
		for create_table in table_creation:
		    if create_table == '\n':
		        continue
		    print(create_table)
		    curs.execute(create_table)
    
		#opens file of populate table statements
		g = open('a2-data.sql')
		data_sql = g.read()
		populate_table = data_sql.split(';')

		#reads in the individual statements
		for info in populate_table:
		    if info == '\n':
		        continue
		    print(info)    
		    curs.execute(info)
		    
		con.commit()
		#closes cursor and connection
		curs.close()
		con.close()
		print('complete gp1_main.py')
