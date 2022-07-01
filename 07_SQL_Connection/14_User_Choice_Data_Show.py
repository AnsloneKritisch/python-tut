try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307',database='school')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")

print()
Srno = input("Enter Srno. : ")
value = (Srno,)

sql = "select * from student where srno = %s"

myc = conn.cursor()

try:
    myc.execute(sql,value)
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
        print()
        
    
    

except:
    print("Data Update Error")
    myc.close()
    
conn.close()


