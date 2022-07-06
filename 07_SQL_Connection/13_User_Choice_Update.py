from requests import delete


try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307',database='school')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")


# Codes For Showing The Table
print()

sql = "select * from student"
myc = conn.cursor()

try:
    myc.execute(sql)
    row = myc.fetchone()
    print("Srno  Name  Fees")
    while row is not None :
        Srno = row[0]
        Name = row[1]
        Fees = row[2]
        print(Srno , end=" ")
        print(Name , end=" ")
        print(Fees , end=" ")
        row = myc.fetchone()
        print(myc.rowcount)
    
except:
    print("Data Update Error")
    myc.close()
    
    

# Data Update Codes


print()
print("Choose Serial no. from the table you want to update \n")
Name = input("Enter the Name : ")
Fees = input("Enter the Fees : ")
Srno = input("Enter the Srno : ")
value = (Name , Fees , Srno)

   
sql = "UPDATE student set Name= %s , Fees=%s where srno = %s"
myc = conn.cursor()

try:
    myc.execute(sql,value)
    print("Data Updated Sucessfully")
    # we need to commit to insert data into table
    conn.commit()
    

except:
    print("Data Update Error")
    myc.close()
    



conn.close()

