import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3306')

if(conn.is_connected()):
    print("Connection Succed")
    
else:
    print("Connection Failed")