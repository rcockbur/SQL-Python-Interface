import cx_oracle

con = cx_Oracle.connect('vanbelle/hogwarts77@gwynne.cs.ualberta.ca:1521:CRS[:1521]/CRS')

cur = con.cursor()

cur.execute("""
DROP TABLE not_allowed;
DROP TABLE doctor;
DROP TABLE patient;
DROP TABLE can_conduct;
DROP TABLE medical_lab;
DROP TABLE test_type;""")

cur.execute("""CREATE TABLE patient (
    health_care_no int,
    name           varchar(100) NOT NULL,
    address        varchar(200),
    birth_day      date,
    phone          char(10),
    PRIMARY KEY(health_care_no),
    UNIQUE(name,address)
);

CREATE TABLE doctor (
    employee_no     int,
    clinic_address  varchar(100) NOT NULL,
    office_phone    char(10),
    emergency_phone char(10),
    health_care_no  int,
    PRIMARY KEY (employee_no),
    FOREIGN KEY (health_care_no) REFERENCES patient
);

CREATE TABLE medical_lab (
    lab_name  varchar(25),
    address   varchar(100) NOT NULL,
    phone     char(10) NOT NULL,
    PRIMARY KEY (lab_name)
);
   
CREATE TABLE test_type (
    type_id        int,
    test_name      varchar(48) NOT NULL,
    pre_requirement varchar(1024),
    test_procedure varchar(1024),
    PRIMARY KEY (type_id),
    UNIQUE (test_name)
);

CREATE TABLE can_conduct (
    lab_name  varchar(25),
    type_id   int,
    PRIMARY KEY(lab_name,type_id),
    FOREIGN KEY(lab_name) REFERENCES medical_lab,
    FOREIGN KEY(type_id) REFERENCES test_type
);
  
CREATE TABLE not_allowed (
    health_care_no  int,
    type_id         int,
    PRIMARY KEY(health_care_no, type_id),
    FOREIGN KEY(health_care_no) REFERENCES patient,
    FOREIGN KEY(type_id) REFERENCES test_type
);

CREATE TABLE test_record (
    test_id     int,
    type_id     int,
    patient_no  int,
    employee_no int,
    medical_lab varchar(25),
    result      varchar(1024),
    prescribe_date  date,
    test_date   date,
    PRIMARY KEY(test_id),
    FOREIGN KEY (employee_no) REFERENCES doctor,
    FOREIGN KEY (medical_lab) REFERENCES medical_lab,
    FOREIGN KEY (type_id) REFERENCES test_type,
    FOREIGN KEY (patient_no) REFERENCES patient
);""")

cur.execute("""insert into patient values(121212, 'Peter Capaldi', '12 Gallifrey',to_date('1958-04-11', 'YYYY-MM-DD'), '121-2121');

insert into patient values(111111, 'Matt Smith', '11 Gallifrey',to_date('1982-10-28','YYYY-MM-DD') , '111-1111');

insert into patient values(101010, 'David Tennant', '10 Gallifrey', to_date('1971-04-18', 'YYYY-MM-DD'), '101-0101');

insert into patient values(090909, 'Christopher Eccleston', '9 Gallifrey', to_date('1964-02-16', 'YYYY-MM-DD'), '090-9090');

insert into patient values(777777, 'Harry Potter', '4 Privet Drive', to_date('1980-07-07', 'YYYY-MM-DD'), '070-0707');

insert into patient values(888888, 'Hermione Granger', 'England', to_date('1979-09-19', 'YYYY-MM-DD'), '080-8080');

insert into patient values(666666, 'Ron Weasley', 'The Burrow', to_date('1980-03-01', 'YYYY-MM-DD'), '060-6060');

insert into patient values(222222, 'Poppy Pomfrey', 'Hogwarts', to_date('1941-02-02', 'YYYY-MM-DD'), '222-2222');

insert into patient values(11, 'Joe Boring', 'Edmonton', to_date('1987-03-10' , 'YYYY-MM-DD'), '123-4567');

insert into doctor values(1112, 'Edmonton Hospital', '456-8790', '546-7854', 11);

insert into doctor values(2222, 'Infirmary in Hogwarts', '222-2222', '222-2222', 222222);

insert into doctor values(1212, '12 Tardis', '111-2222', '012-0012', 121212);

insert into doctor values(1111, '11 Tardis', '111-1111', '111-1111', 111111);

insert into doctor values(1010, '10 Tardis', '010-1010', '111-0000', 101010);

insert into doctor values(0909, '9 Tardis', '999-9999', '009-0909', 090909);

insert into medical_lab values('St. Mungos Hospital', 'London', '000-0000');

insert into medical_lab values('Hogwarts Infirmary', 'Hogwarts', '222-2222');

insert into medical_lab values('Tardis', 'Everywhere in Space and Time, except apparently Manhatten to save Amy and Rory','910-1112');

insert into medical_lab values('Edmonton Hospital', '7 Edmonton', '000-1234');

insert into test_type values(222221, 'bone regrowth', 'missing bones', 'give Skele-gro bone regrowth potion');

insert into test_type values(333331, 'saving the world', 'none', 'astounding them with wit and brilliance, or trapping the doomed world in a painting');

insert into test_type values(1, 'CT scan', 'brain injury', 'whirring machine');

insert into test_type values(5, 'bone marrow check', 'none', 'pointy needles');

insert into test_type values(6, 'X ray', 'none', 'pretty pictures');

insert into test_type values(333332, 'Regeneration', 'be a time lord', 'magical timey wimey stuff?');

insert into can_conduct values('Hogwarts Infirmary',222221);

insert into can_conduct values('Hogwarts Infirmary',222223);

insert into can_conduct values('St. Mungos Hospital', 000001);

insert into can_conduct values('Tardis', 333331);

insert into can_conduct values('Tardis', 333332);

insert into not_allowed values(666666, 333332);

insert into not_allowed values(777777, 333332);

insert into not_allowed values(888888, 333332);

insert into not_allowed values(090909, 222223);

insert into not_allowed values(111111, 222223);

insert into not_allowed values(090909, 5);

insert into not_allowed values(101010, 5);

insert into not_allowed values(121212, 5);

insert into not_allowed values(111111, 5);

insert into test_record values(4445, 1, 090909, 1010, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2010-03-11', 'YYYY-MM-DD'));

insert into test_record values(4446, 1, 121212, 1010, 'Edmonton Hospital', 'normal', to_date('2013-06-11', 'YYYY-MM-DD'), to_date('2011-12-29', 'YYYY-MM-DD'));

insert into test_record values(4447, 1, 101010, 1111, 'Edmonton Hospital', 'normal', to_date('2013-07-11', 'YYYY-MM-DD'), to_date('2012-12-11', 'YYYY-MM-DD'));

insert into test_record values(44449, 5, 222222, 1111, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2013-11-11', 'YYYY-MM-DD'));

insert into test_record values(44448, 5, 777777, 1212, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2012-11-11', 'YYYY-MM-DD'));

insert into test_record values(44447, 5, 888888, 1112, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2011-11-11', 'YYYY-MM-DD'));

insert into test_record values(44446, 5, 11, 1112, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2010-11-11', 'YYYY-MM-DD'));

insert into test_record values(4443, 6, 090909, 1112, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2010-11-11', 'YYYY-MM-DD'));

insert into test_record values(4442, 6, 222222, 0909, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2011-11-11', 'YYYY-MM-DD'));

insert into test_record values(4441, 6, 666666, 1010, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2012-11-11', 'YYYY-MM-DD'));

insert into test_record values(44440, 222221, 777777, 2222, 'Hogwarts Infirmary', 'normal', to_date('2013-01-11', 'YYYY-MM-DD'), to_date('2010-12-31', 'YYYY-MM-DD'));

insert into test_record values(44445, 222221, 888888, 2222, 'Hogwarts Infirmary', 'normal', to_date('2013-01-11', 'YYYY-MM-DD'), to_date('2012-12-31', 'YYYY-MM-DD'));

insert into test_record values(444440, 222221, 666666, 2222, 'Hogwarts Infirmary', 'normal', to_date('2013-01-11', 'YYYY-MM-DD'), to_date('2011-12-31', 'YYYY-MM-DD'));

insert into test_record values(444441, 222221, 777777, 2222, 'Hogwarts Infirmary', 'normal', to_date('2013-01-11', 'YYYY-MM-DD'), to_date('2013-10-31', 'YYYY-MM-DD'));

insert into test_record values(444442, 333332, 090909, 0909, 'Tardis', 'normal', to_date('2012-04-11', 'YYYY-MM-DD'), to_date('2010-04-10', 'YYYY-MM-DD'));

insert into test_record values(444443, 333332, 101010, 1010, 'Tardis', 'normal', to_date('1995-04-11', 'YYYY-MM-DD'), to_date('2011-04-11', 'YYYY-MM-DD'));

insert into test_record values(44441, 333331, 090909, 0909, 'Tardis', 'normal', to_date('1965-04-11', 'YYYY-MM-DD'), to_date('2010-12-25', 'YYYY-MM-DD'));

insert into test_record values(44442, 333331, 101010, 1010, 'Tardis', 'normal', to_date('1965-04-11', 'YYYY-MM-DD'), to_date('2011-12-25', 'YYYY-MM-DD'));

insert into test_record values(44443, 333331, 111111, 1111, 'Tardis', 'normal', to_date('1965-04-11', 'YYYY-MM-DD'), to_date('2012-12-25', 'YYYY-MM-DD'));

insert into test_record values(444444, 333332, 111111, 1111, 'Tardis', 'abnormal', to_date('2012-02-11', 'YYYY-MM-DD'), to_date('2012-04-12', 'YYYY-MM-DD'));

insert into test_record values(444445, 333332, 111111, 1111, 'Tardis', 'normal', to_date('2011-04-11', 'YYYY-MM-DD'), to_date('2012-07-13', 'YYYY-MM-DD'));

insert into test_record values(444449, 333332, 121212, 1212, 'Tardis', 'normal', to_date('2011-04-11', 'YYYY-MM-DD'), to_date('2013-07-13', 'YYYY-MM-DD'));

insert into test_record values(444447, 333331, 101010, 1010, 'Tardis', 'normal', to_date('1965-04-11', 'YYYY-MM-DD'), to_date('2013-12-25', 'YYYY-MM-DD'));

insert into test_record values(9, 1, 11, 1010, 'St. Mungos Hospital', 'normal', to_date('2013-03-11', 'YYYY-MM-DD'), to_date('2013-11-11', 'YYYY-MM-DD'));

insert into test_record values(789, 6, 777777, 1112, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2013-11-11', 'YYYY-MM-DD'));

insert into test_record values(765, 1, 777777, 1112, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2014-01-11', 'YYYY-MM-DD'));

insert into test_record values(2, 1, 777777, 1112, 'Edmonton Hospital', 'normal', to_date('2013-05-11', 'YYYY-MM-DD'), to_date('2014-03-11', 'YYYY-MM-DD'));

insert into test_record values(3, 1, 777777, 1112, 'Edmonton Hospital', 'normal', to_date('2013-06-11', 'YYYY-MM-DD'), to_date('2013-12-29', 'YYYY-MM-DD'));

insert into test_record values(4, 1, 666666, 1112, 'Edmonton Hospital', 'normal', to_date('2013-07-11', 'YYYY-MM-DD'), to_date('2013-12-11', 'YYYY-MM-DD'));""")

con.close()