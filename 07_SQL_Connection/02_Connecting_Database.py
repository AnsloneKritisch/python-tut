# Writing Normally will show so manty errors and its quit hard to under the problems
# So we use try and except methord to solve this problem 

try:
    import mysql.connector

    conn = mysql.connector.connect(host='localhost',user='root',password='anshu',port='3307')

    if(conn.is_connected()):
        print("Connection Succed")
        
except:
    print("Connection Failed")
    
    
# Close the Database Connection
conn.close()

