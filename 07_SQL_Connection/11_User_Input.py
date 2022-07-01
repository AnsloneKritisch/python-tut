# Parameterized Query

try:
    import mysql.connector

    conn = mysql.connector.connect(
        host='localhost', user='root', password='anshu', port='3307', database='school')

    if(conn.is_connected()):
        print("Connection Succed")

except:
    print("Connection Failed")

Name = input("Enter the Name : ")
Fees = input("Enter the Fees : ")
value = (Name, Fees)

sql = "insert into student (Name,Fees)Values(%s,%s)"
myc = conn.cursor()

try:
    myc.execute(sql, value)
    print("Data Inserted Sucessfully")
    # we need to commit to insert data into table
    conn.commit()


except:
    print("Data doesn't Inserted")
    myc.close()

conn.close()
