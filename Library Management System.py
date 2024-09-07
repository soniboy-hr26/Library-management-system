import mysql.connector as a
con=a.connect(host='localhost',user='root',passwd='gauti@1999',auth_plugin='mysql_native_password',database='library')


def addbook():
    bn =input("Enter Author name: ")
    c =input("Enter Book code: ")
    t =input("Total books: ")
    s =input("Enter Subject: ")
    data=(bn,c,t,s)
    sql="Insert into books values (%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-----------------------------------------------------------<")
    print("Data Entered Successfully")
    main()

def issueb():
    n =input("Enter Name: ")
    r =input("Enter Reg NO: ")
    co =input("Enter Book code: ")
    d =input("Enter Date: ")
    a="insert into issue values (%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">----------------------------------------------------------<")
    print("Book issued to: ",n)
    bookup(co,-1)

def submitb():
    n =input("Enter Name: ")
    r =input("Enter Reg NO: ")
    co =input("Enter Book code: ")
    d =input("Enter Date: ")
    a="insert into submit values (%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">----------------------------------------------------------<")
    print("Book submitted from: ",n)
    bookup(co,1)

def bookup(co,u):
    a="Select TOTAL from books where bcode=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0] + u
    sql="UPDATE books SET total=%s WHERE bcode =%s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac=input("Enter book code: ")
    a="Delete from books where bcode=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def dispbook():
    a="Select * from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Author name: ",i[0])
        print("Book code: ",i[1])
        print("Total: ",i[2])
        print("Subject: ",i[3])
        print(">-----------------------------------------------------<")
    main()


def main():
    print('''-------------------WELCOME TO LIBRARY MANAGER------------------
    1. ADD BOOK
    2. ISSUE BOOK
    3. SUBMIT BOOK
    4. DELETE BOOK
    5. DISPLAY BOOK
    ''')
    choice=input("Enter Task No: ")
    print(">---------------------------------------------------------<")
    if(choice=='1'):
        addbook()
    elif(choice=='2'):
        issueb()
    elif(choice=='3'):
        submitb()
    elif(choice=='4'):
        dbook()
    elif(choice=='5'):
        dispbook()
    else:
        print("Wrong choice.........")
        main()


def pswd():
    ps=input("Enter Password: ")
    if ps=="aman123":
        main()
    else:
        print("Wrong Password")
        pswd()
pswd()
    