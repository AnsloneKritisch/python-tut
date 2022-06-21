

try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307',database='school')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")
    
    
sql = "create table student(srno int(10) AUTO_INCREMENT PRIMARY KEY ,Name varchar(80),fees dec(10,2))"
myc = conn.cursor()

try:
    myc.execute(sql)
    print("Table Created Sucessfully")
    

except:
    print("Table Not Created")