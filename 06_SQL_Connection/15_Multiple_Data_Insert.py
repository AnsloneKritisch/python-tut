

try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307',database='school')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")
    
# sql = "insert into student (Name,Fees)Values('Ram',1200.50),('Ram Das',1500.50),('Shyam',2200.50),('Ramia',1200.50),('Ramlena Das',1500.50),('Shyami',2200.50),(%s,%s)"
sql = "insert into student (Name,Fees)Values(%s,%s)"
value = [('Ramu',1200.50),('Rami Das',1500.50)]
myc = conn.cursor()

try:
    myc.executemany(sql,value)
    print("Data Inserted Sucessfully")
    # we need to commit to insert data into table
    conn.commit()
    

except:
    print("Data doesn't Inserted")
    myc.close()
    
conn.close()


