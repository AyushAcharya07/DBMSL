/*CREATE TABLE BORROWER (Roll_no number(10) PRIMARY KEY,Name varchar2(20),Date_of_issue Date,Book_name varchar2(30),Status char(1));
CREATE TABLE FINE(Roll_no number(10),Date_of_Return Date,Amount number(5),FOREIGN KEY(Roll_no) REFERENCES BORROWER(Roll_no));*/
/*INSERT INTO BORROWER VALUES(20,'SHIVA SRESHTH',TO_DATE('12-09-2022','DD-MM-YYYY'),'NIRALI','I');
INSERT INTO BORROWER VALUES(55,'SAMPADA AGHAV',TO_DATE('15-09-2022','DD-MM-YYYY'),'HCI','I');
INSERT INTO BORROWER VALUES(35,'AYUSH ACHARYA',TO_DATE('15-09-2022','DD-MM-YYYY'),'SPOS','I');
INSERT INTO BORROWER VALUES(39,'KAUSTUBH WARADE',TO_DATE('15-09-2022','DD-MM-YYYY'),'CNS','I');*/
SELECT * FROM BORROWER;

DECLARE
    v_roll_no NUMBER := 35; 
    v_book_name VARCHAR2(30) := 'SPOS'; 
    v_issue_date DATE;
    v_status CHAR(1);
    v_fine_amt NUMBER;
    v_days_diff NUMBER;
BEGIN
    
    SELECT Roll_no, Date_of_issue, Status
    INTO v_roll_no, v_issue_date, v_status
    FROM Borrower
    WHERE Roll_no = v_roll_no AND Book_name = v_book_name;

    
    v_days_diff := TO_DATE('12-10-2022', 'DD-MM-YYYY') - v_issue_date;

    
    IF v_status = 'I' THEN
        IF v_days_diff <= 30 THEN
            
            v_fine_amt := v_days_diff * 5;
        ELSE
            -- Calculate fine at Rs 50 per day for each day beyond 30 days
            v_fine_amt := (v_days_diff - 30) * 50 + 30 * 5;
        END IF;

        INSERT INTO Fine (Roll_no, Date_of_Return, Amount)
        VALUES (v_roll_no, TO_DATE('12-10-2022', 'DD-MM-YYYY'), v_fine_amt);

        UPDATE Borrower
        SET Status = 'R'
        WHERE Roll_no = v_roll_no AND Book_name = v_book_name;

        DBMS_OUTPUT.PUT_LINE('Fine Amount: Rs ' || v_fine_amt);
    ELSE
        RAISE_APPLICATION_ERROR(-20001, 'Book not issued or already returned');
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Book not found for the given Roll_no and Book_name');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('An error occurred: ' || SQLERRM);
END;
/
