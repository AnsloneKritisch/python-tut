

try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307',database='school')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")
    
   
sql = "DELETE from student where srno=3"
myc = conn.cursor()

try:
    myc.execute(sql)
    print("Data Deleted Sucessfully")
    # we need to commit to insert data into table
    conn.commit()
    

except:
    print("Data delete Error")
    myc.close()
    
conn.close()


