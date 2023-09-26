/**CREATE TABLE Areas (radius number(10), area number(10));

DECLARE 
	pi constant number:=3.14;
	ar number(10);

BEGIN
	FOR i in 5..9 LOOP
		ar:=pi*i*i;
		INSERT INTO Areas values (i,ar);
		dbms_output.put_line('Area of circle is : ' || ar);
	END LOOP;

END;
/
select distinct * from Areas;*/

/**CREATE TABLE Borrower(Roll_no number (10) primary key,Stud_name varchar2(20),Date_of_issue date,Book_Name varchar2(20),Status char(1));
CREATE TABLE Fine(Roll_no number (10),Date_of_Return date, amount number(5),foreign key (Roll_no) references Borrower(Roll_no));*/
/*INSERT INTO Borrower VALUES(10,'AAYUSH MEHRA',TO_DATE('12-12-2013','DD-MM-YYYY'),'NIRALI','I');
INSERT INTO Borrower VALUES(11,'ANKUSH JOSHI',TO_DATE('22-01-2014','DD-MM-YYYY'),'NIRALI','I');
INSERT INTO Borrower VALUES(25,'NIHAR JAIN',TO_DATE('22-01-2014','DD-MM-YYYY'),'NIRALI','I');
INSERT INTO Fine(Roll_no,Date_of_Return) VALUES(10,TO_DATE('05-01-2014','DD-MM-YYYY'));
INSERT INTO Fine (Roll_no,Date_of_Return) VALUES(11,TO_DATE('28-02-2014','DD-MM-YYYY'));
INSERT INTO Fine (Roll_no,Date_of_Return)VALUES(25,TO_DATE('17-02-2014','DD-MM-YYYY'));*/


DECLARE
    Fine number(5);
	days number(5);
	return_date date;
	Book_name varchar2(20);
	issue_date date;
	roll_no number(5):=10;

BEGIN
    /*SELECT TO_DATE(Borrower.DATE_OF_ISSUE,'DD-MM-YYYY') INTO issue_date FROM Borrower WHERE Borrower.DATE_OF_ISSUE=issue_date;
	SELECT TO_DATE(Fine.Date_of_Return,'DD-MM-YYYY') INTO return_date FROM Fine WHERE Fine.Date_of_Return=return_date;*/
   	SELECT DATE_OF_ISSUE INTO issue_date FROM Borrower WHERE Borrower.Roll_no=roll_no;
	SELECT Date_of_Return INTO return_date FROM Fine;


	days:=return_date-issue_date;	

	dbms_output.put_line(days);
	IF (days>15 AND days<=30) THEN
        Fine:=5*days;
		INSERT INTO Fine(Amount) VALUES (Fine);

	ELSE 
        Fine:=50*days;
		INSERT INTO Fine(Amount) VALUES (Fine);

	END IF;

	dbms_output.put_line(Fine);

	UPDATE Borrower SET Status='R';


END;
/ 
SELECT * FROM Borrower;
SELECT * FROM Fine;
	
