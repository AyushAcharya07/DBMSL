from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017")
database=client.StudentDB
collection=database.Students

while (True):
    print("*" * 10, "MENU", "*" * 10)
    print("1.Add data to database\n2.Read data from database\n3.Update data\n4.Delete records from database\n5.Exit")
    ch = int(input("Enter your choice : "))

    if ch==1:
        n=int(input("Enter the no. of records to be inserted : "))
        for i in range(n):
            Roll=int(input("Enter the Roll No. : "))
            Name=input("Enter the Name : ")
            Div=input("Enter the Class and Division : ")
            Marks=int(input("Enter the Marks : "))
            collection.insert_one({"Roll_No":Roll,"Name":Name,"Class":Div,"Marks":Marks})

    elif ch==2:
        val=input("\nA.Search for all data\nB.Search specific data\nEnter your choice : ")
        if val=="A":
            cursor=collection.find({})
            for i in cursor:
                print("Roll No.: ",i["Roll_No"])
                print("Name : ",i["Name"])
                print("Class and Division :",i["Class"])
                print("Marks : ",i["Marks"])
                print("")

        elif val=="B":
            roll=int(input("Enter the Roll No. to be searched: "))
            document = collection.find_one({"Roll_No": roll})
            if document:
                print("Roll No:", document["Roll_No"])
                print("Name:", document["Name"])
                print("Class and Division:", document["Class"])
                print("Marks:", document["Marks"])
            else:
                print("Record not found.")



    elif ch == 3:
        roll = int(input("Enter the Roll No. to be updated: "))
        document = collection.find_one({"Roll_No": roll})
        if document:

            new_name = input("Enter the new Name: ")
            new_class = input("Enter the new Class and Division: ")
            new_marks = int(input("Enter the new Marks: "))  # Add a closing parenthesis here
            updated_data = {
                "$set": {
                    "Name": new_name,
                    "Class": new_class,
                    "Marks": new_marks
                }
            }
            collection.update_one({"Roll_No": roll}, updated_data)
            print("Record updated successfully!")
        else:
            print("Record not found.")

    elif ch==4:
        roll = int(input("Enter the Roll No. to be deleted: "))
        result = collection.delete_one({"Roll_No": roll})
        if result.deleted_count > 0:
            print("Record deleted successfully!")
        else:
            print("Record not found.")

    elif ch==5:
        print("Exiting Successfully!!")
        break

    else:
        print("\nWrong Choice enetered !!\nPlease Try Again!!")

client.close()
