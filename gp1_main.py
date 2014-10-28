import cx_oracle

con = cx_Oracle.connect('vanbelle/hogwarts77@gwynne.cs.ualberta.ca:1521:CRS[:1521]/CRS')

cur = con.cursor()

cur.execute("DROP TABLE test_record;")
cur.execute("DROP TABLE not_allowed;")
cur.execute("DROP TABLE doctor;")
cur.execute("DROP TABLE patient;")
cur.execute("DROP TABLE can_conduct;")
cur.execute("DROP TABLE medical_lab;")
cur.execute("DROP TABLE test_type;")

cur.execute("CREATE TABLE patient (health_care_no int,name varchar(100) NOT NULL,address        varchar(200),birth_day      date,phone          char(10),PRIMARY KEY(health_care_no),UNIQUE(name,address));")


cur.execute("CREATE TABLE doctor (    employee_no     int,    clinic_address  varchar(100) NOT NULL,    office_phone    char(10),    emergency_phone char(10),    health_care_no  int,    PRIMARY KEY (employee_no),    FOREIGN KEY (health_care_no) REFERENCES patient);")

cur.execute("CREATE TABLE medical_lab (    lab_name  varchar(25),    address   varchar(100) NOT NULL,    phone     char(10) NOT NULL,    PRIMARY KEY (lab_name));")

cur.execute("CREATE TABLE test_type (    type_id        int,    test_name      varchar(48) NOT NULL,    pre_requirement varchar(1024),    test_procedure varchar(1024),   PRIMARY KEY (type_id),    UNIQUE (test_name));")

cur.execute("CREATE TABLE can_conduct (    lab_name  varchar(25),    type_id   int,    PRIMARY KEY(lab_name,type_id),    FOREIGN KEY(lab_name) REFERENCES medical_lab,    FOREIGN KEY(type_id) REFERENCES test_type);")
  
cur.execute("CREATE TABLE not_allowed (    health_care_no  int,    type_id         int,    PRIMARY KEY(health_care_no, type_id),    FOREIGN KEY(health_care_no) REFERENCES patient,    FOREIGN KEY(type_id) REFERENCES test_type);")

cur.execute("CREATE TABLE test_record (    test_id     int,    type_id     int,    patient_no  int,    employee_no int,    medical_lab varchar(25),    result      varchar(1024),    prescribe_date  date,    test_date   date,    PRIMARY KEY(test_id),    FOREIGN KEY (employee_no) REFERENCES doctor,    FOREIGN KEY (medical_lab) REFERENCES medical_lab,    FOREIGN KEY (type_id) REFERENCES test_type,    FOREIGN KEY (patient_no) REFERENCES patient);")

con.close()