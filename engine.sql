DROP VIEW medical_risk;
CREATE VIEW medical_risk(medical_type,alarming_age,abnormal_rate) AS
SELECT c1.type_id,min(c1.age),ab_rate
FROM  
      -- Find the abnormal rate for each test type
     (SELECT   t1.type_id, count(distinct t1.patient_no)/count(distinct t2.patient_no) ab_rate
      FROM     test_record t1, test_record t2
      WHERE    t1.result <> 'normal' AND t1.type_id = t2.type_id AND t1.result IS NOT NULL AND t2.result IS NOT NULL
      GROUP BY t1.type_id
      ) r,
	-- Find the abnormal result count above each age
     (SELECT   t1.type_id,age,COUNT(distinct p1.health_care_no) AS ab_cnt
      FROM     patient p1,test_record t1,
               (SELECT DISTINCT trunc(months_between(sysdate,p1.birth_day)/12) AS age FROM patient p1) 
      WHERE    trunc(months_between(sysdate,p1.birth_day)/12)>=age
               AND p1.health_care_no=t1.patient_no
               AND t1.result<>'normal' AND t1.result IS NOT NULL 
      GROUP BY age,t1.type_id
      ) c1, 
 	 --- Find the patient count above each age
      (SELECT  t1.type_id,age,COUNT(distinct p1.health_care_no) AS cnt
       FROM    patient p1, test_record t1,
      	       (SELECT DISTINCT trunc(months_between(sysdate,p1.birth_day)/12) AS age FROM patient p1)
       WHERE trunc(months_between(sysdate,p1.birth_day)/12)>=age
             AND p1.health_care_no=t1.patient_no AND t1.result IS NOT NULL 
       GROUP BY age,t1.type_id
      ) c2
WHERE  c1.age = c2.age AND c1.type_id = c2.type_id AND c1.type_id = r.type_id 
       AND c1.ab_cnt/c2.cnt>=2*r.ab_rate
GROUP BY c1.type_id,ab_rate;
SELECT DISTINCT name, address, phone, m.medical_type
FROM   patient p, medical_risk m
WHERE  trunc(months_between(sysdate,birth_day)/12) >= m.alarming_age 
AND
       p.health_care_no NOT IN (SELECT patient_no
                                FROM   test_record t
                                WHERE  m.medical_type = t.type_id
                               );

