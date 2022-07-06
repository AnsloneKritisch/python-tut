def user_input():
    try:
        import mysql.connector

        conn = mysql.connector.connect(
            host='localhost', user='root', password='anshu', port='3307', database='school')

        if(conn.is_connected()):
            print()

    except:
        print("Connection Failed")

    print("\nCheck The Table and Update Data\n")

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
            print()
    except:
        print("Data Update Error")
        myc.close()


    print()    
    print()   
    
    print("Enter the Srno you want to change \n")
    Srno = input("Enter the Srno : ")
    Name = input("Enter the Name : ")
    Fees = input("Enter the Fees : ")
    
    value = (Name , Fees , Srno)

    
    sql = "UPDATE student set Name= %s , Fees=%s where srno = %s"
    myc = conn.cursor()

    try:
        myc.execute(sql,value)
        print("Data Updated Sucessfully")
        conn.commit()
        

    except:
        print("Data Update Error")
        myc.close()
        




while True:
    user_input()

    ch = input("\nDo you want to exit[y/n] : ")

    if(ch == "y" or ch == "Y"):
        break
    else:
        continue
