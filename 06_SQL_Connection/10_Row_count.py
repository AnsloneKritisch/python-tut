try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307',database='school')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")
    
    
sql = "select * from student"
myc = conn.cursor()

try:
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None :
        print("Srno  Name  Fees")
        Srno = row[0]
        Name = row[1]
        Fees = row[2]
        row = myc.fetchone()
        print(nyc.rowcount)
    
    

except:
    print("Data Update Error")
    myc.close()
    
conn.close()


