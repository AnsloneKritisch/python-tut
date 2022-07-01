# Creating Databse using Codes

try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307',database='school')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")
    
    
sql = "show tables"
myc = conn.cursor()

try:
    myc.execute(sql)
    for i in myc:
        print(i)


except:
    print("Table Not Created")