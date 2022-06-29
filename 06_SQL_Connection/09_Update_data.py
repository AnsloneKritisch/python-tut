try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307',database='school')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")
    
    
sql = "UPDATE student set Name= 'Shayam Kumar Das' , Fees=1500.6 where srno=3"
myc = conn.cursor()

try:
    myc.execute(sql)
    print("Data Updated Sucessfully")
    # we need to commit to insert data into table
    conn.commit()
    

except:
    print("Data Update Error")
    myc.close()
    
conn.close()


