-- @AYUSH ACHARYA TE 1

CREATE TABLE LIB_TABLE(Roll_no NUMBER(5),Student_Name VARCHAR2(20),DATE_OF_ISSUE DATE,Book_Name VARCHAR2(20),Status CHAR(1));
CREATE TABLE LIB_AUDIT(Roll_no NUMBER(5),Student_Name VARCHAR2(20),DATE_OF_ISSUE DATE,Book_Name VARCHAR2(20),Status CHAR(1));

INSERT INTO LIB_TABLE VALUES(20,'OMKAR LATPATE',TO_DATE('12-09-2022','DD-MM-YYYY'),'IoT','I');
INSERT INTO LIB_TABLE VALUES(55,'SAMPADA AGHAV',TO_DATE('15-09-2022','DD-MM-YYYY'),'HCI','I');
INSERT INTO LIB_TABLE VALUES(35,'AYUSH ACHARYA',TO_DATE('15-09-2022','DD-MM-YYYY'),'SPOS','I');
INSERT INTO LIB_TABLE VALUES(39,'KAUSTUBH WARADE',TO_DATE('15-09-2022','DD-MM-YYYY'),'CNS','I');

SELECT * FROM LIB_TABLE;

CREATE OR REPLACE TRIGGER TRG
BEFORE UPDATE OR DELETE
ON LIB_TABLE
FOR EACH ROW 

BEGIN
	INSERT INTO LIB_AUDIT VALUES(:OLD.Roll_no,:OLD.Student_Name,:OLD.DATE_OF_ISSUE,:OLD.Book_Name,:OLD.Status);

END;
/
    
UPDATE LIB_TABLE SET Roll_No=36 WHERE Student_Name='AYUSH ACHARYA';
DELETE FROM LIB_TABLE WHERE Roll_no=39;
SELECT * FROM LIB_AUDIT;
