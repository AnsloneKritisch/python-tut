def user_input():
    try:
        import mysql.connector

        conn = mysql.connector.connect(host='localhost', user='root', password='anshu', port='3307', database='school')

        if(conn.is_connected()):
            print("Connetion Succed")
    
    except:
        print("Connection Failed")


    Name = input("Enter the Name :")
    Fees = input("Enter the Fees :")
    value = (Name,Fees)

    sql = "insert into student (Name,Fees) Values(%s,%s)"
    myc = conn.cursor()

    try:
        myc.execute(sql,value)
        print("Data Inserted Sucessfully")
        conn.commit()

    except:
        print("Data Does't Inserted")
        myc.close()
    
    conn.close()
    

while True:
    user_input()

    ch = input("Do you want to exit[y/n] : ")

    if(ch == "y" or ch == "Y"):
        break
    else:
        continue

