import cx_Oracle

con = cx_Oracle.connect("vanbelle/c1234567@gwynne.cs.ualberta.ca:1521/CRS")

curs = con.cursor()

f = open('project_setup.sql')
full_sql = f.read()
table_creation = full_sql.split(';')

for create_table in table_creation:
    if create_table == '\n':
        continue
    curs.execute(create_table)
    
g = open('a2-data.sql')
data_sql = g.read()
populate_table = data_sql.split(';')

for info in populate_table:
    if info == '\n':
        continue    
    curs.execute(info)

curs.close()
con.close()