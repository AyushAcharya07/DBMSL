import mysql.connector 
p=mysql.connector.connect(
    host="localhost",
    user="root",
    database="connect"
)

func=p.cursor()
#var="INSERT INTO data VALUES(1,'AYUSH ACHARYA')"
#func.execute(var)
'''n=int(input("Enter the no. of entries : "))
for i in range(n):
  roll=int(input("Enter the roll no. to be inserted : "))
  name=input("Enter the name : ")
  var2="INSERT INTO data VALUES("+str(roll)+",'"+name+"')"
  func.execute(var2)
  print(func.rowcount, "record inserted.")'''
  
info=input("Enter the roll no to be deleted : ")
var3="DELETE FROM data WHERE Roll_No="+info
func.execute(var3)
p.commit()
print(func.rowcount, "record deleted.")


