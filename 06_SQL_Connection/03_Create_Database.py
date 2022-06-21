# Creating Databse using Codes

try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")
    
    
sql = "create database school"
myc = conn.cursor()

try:
    myc.execute(sql)
    print("Database Created Sucessfully")
    

except:
    print("Database Not Created")