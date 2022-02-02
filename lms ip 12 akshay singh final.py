import mysql.connector as a
con = a.connect(host="localhost", user="root",passwd="1234",database="library")

def addbook():
    bn = input("Enter the book's name:")
    c = input("Enter the book code:")
    t = input("Total books:")
    s = input("Enter Subject:")
    data =(bn,c,t,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------------<")
    print("Data Entered successfully")
    main()

def issueb():
    n = input("Enter Name:")
    r = input("Enter registration number:")
    co = input("Enter Book code:")
    d = input("Enter date:")
    a = "insert into issue values(%s,%s,%s,%s)"
    data =(n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">--------------------------------------------------------------------<")
    print("Book issued to:",n)
    bookup(co,-1)

def submitb():
    n = input("Enter Name:")
    r = input("Enter registration number:")
    co = input("Enter Book code:")
    d = input("Enter date:")
    a = "insert into issue values(%s,%s,%s,%s)"
    data =(n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">--------------------------------------------------------------------<")
    print("Book submitted from:",n)
    bookup(co,1)

def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data =(co,)
    c =con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    t = myresult[0]+ u
    sql ="update books set TOTAL =%s where BCODE =%s"
    d =(t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac = input("Enter Book code:")
    a ="delete from books where BCODE=%s"
    data =(ac,)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def dispbook():
    a ="select* from books"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Book name:",i[0])
        print("Book code:",i[1])
        print("Total:",i[2])
        print(">----------------------<")
    main()

def main():
    print("""
                                                                               LIBRARY MANAGER
    1. ADD A BOOK
    2. ISSUE A BOOK
    3. SUBMIT A BOOK
    4. DELETE BOOK
    5. DISPLAY BOOKS
                                                                                                                                              by- Akshay Singh &
                                                                                                                                                  M.karkon.
    """)
    choice = input("Enter Task number:")
    print(">--------------------------------------------------------------------<")
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
        print("The number written does not match the given options...........")
        main()

def pswd():
    ps = input("Enter the password:")
    if ps  =="1234":
        main()
    else:
        print("The written password is incorrect! please try again......")
        pswd()
pswd() 
        
