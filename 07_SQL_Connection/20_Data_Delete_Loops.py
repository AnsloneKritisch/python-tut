def user_input():
    try:
        import mysql.connector

        conn = mysql.connector.connect(
            host='localhost', user='root', password='anshu', port='3307', database='school')

        if(conn.is_connected()):
            print()

    except:
        print("Connection Failed")

    print("\nCheck The Table and Insert Data\n")

    sql = "select * from student"
    myc = conn.cursor()

    try:
        myc.execute(sql)
        row = myc.fetchone()
        print("Srno  Name  Fees")
        while row is not None:
            Srno = row[0]
            Name = row[1]
            Fees = row[2]
            print(Srno, end=" ")
            print(Name, end=" ")
            print(Fees, end=" ")
            row = myc.fetchone()
            print(myc.rowcount)

    except:
        print("Data Update Error")
        myc.close()


    print()    
    Srno = input("\nEnter the Srno : ")
    value = (Srno,)
    sql = "DELETE from student where srno= %s"
    myc = conn.cursor()
    
    try:
        myc.execute(sql, value)
        print("Data Deleted Sucessfully")
        conn.commit()
        
    except:
        print("Data delete Error")
        myc.close()


while True:
    user_input()

    ch = input("\nDo you want to exit[y/n] : ")

    if(ch == "y" or ch == "Y"):
        break
    else:
        continue
