/*CREATE TABLE STUD_MARKS(Roll_no number(10) PRIMARY KEY, Student_Name varchar2(20), Total_Marks number(5));
CREATE TABLE RESULT(Roll_no number(10), Student_Name varchar2(20), Class varchar(20), FOREIGN KEY(Roll_no) REFERENCES STUD_MARKS(Roll_no));

INSERT INTO STUD_MARKS VALUES (20, 'DHRUV PANDIT', 700);
INSERT INTO STUD_MARKS VALUES (26, 'KRUTI JOSHI', 898);
INSERT INTO STUD_MARKS VALUES (35, 'AANSH SHARMA', 987);
INSERT INTO STUD_MARKS VALUES (37, 'AYUSH ACHARYA', 1459);*/

CREATE OR REPLACE PROCEDURE proc_GRADE(roll IN NUMBER, name IN VARCHAR2, marks IN NUMBER) IS
BEGIN
    IF (marks <= 1500 AND marks >= 990) THEN
        INSERT INTO RESULT VALUES(roll, name, 'DISTINCTION');
        DBMS_OUTPUT.PUT_LINE(name || ' is granted DISTINCTION');
    ELSIF (marks >= 900 AND marks <= 989) THEN
        INSERT INTO RESULT VALUES(roll, name, 'FIRST CLASS');
        DBMS_OUTPUT.PUT_LINE(name || ' is granted FIRST CLASS');
    ELSIF (marks >= 825 AND marks <= 899) THEN
        INSERT INTO RESULT VALUES(roll, name, 'HIGHER SECOND CLASS');
        DBMS_OUTPUT.PUT_LINE(name || ' is granted HIGHER SECOND CLASS');
    ELSE
        INSERT INTO RESULT VALUES(roll, name, 'FAILED');
        DBMS_OUTPUT.PUT_LINE(name || ' has FAILED');
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Student with Roll ' || roll || ' not found.');
END;

/

DECLARE
    temp_roll number(5);
    temp_name varchar2(20);
    temp_marks number(5);
BEGIN
    FOR student_rec IN (SELECT Roll_no, Student_Name, Total_Marks FROM STUD_MARKS)
    LOOP
        temp_roll := student_rec.Roll_no;
        temp_name := student_rec.Student_Name;
        temp_marks := student_rec.Total_Marks;
        
        proc_GRADE(temp_roll, temp_name, temp_marks);
    END LOOP;
    
END;
/
