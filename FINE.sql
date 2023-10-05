DECLARE
    v_roll_no NUMBER ; 
    v_book_name VARCHAR2(30); 
    v_issue_date DATE;
    v_status CHAR(1);
    v_fine_amt NUMBER;
    v_days_diff NUMBER;
BEGIN
    v_roll_no := &v_roll_no; 
    v_book_name := &v_book_name; 
    SELECT Roll_no, Date_of_issue, Status
    INTO v_roll_no, v_issue_date, v_status
    FROM Borrower
    WHERE Roll_no = v_roll_no AND Book_name = v_book_name;

    
    v_days_diff := TO_DATE('12-10-2022', 'DD-MM-YYYY') - v_issue_date;

    
    IF v_status = 'I' THEN
        IF v_days_diff <= 30 THEN
            
            v_fine_amt := v_days_diff * 5;
        ELSE
            v_fine_amt := (v_days_diff - 30) * 50 + 30 * 5;
        END IF;

        INSERT INTO Fine (Roll_no, Date_of_Return, Amount)
        VALUES (v_roll_no, TO_DATE('12-10-2022', 'DD-MM-YYYY'), v_fine_amt);

        UPDATE Borrower
        SET Status = 'R'
        WHERE Roll_no = v_roll_no AND Book_name = v_book_name;

        DBMS_OUTPUT.PUT_LINE('Fine Amount: Rs ' || v_fine_amt);
    ELSE
        DBMS_OUTPUT.PUT_LINE('Book not found for the given Roll_no and Book_name');
    END IF;

END;
/
