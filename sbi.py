import os
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='',database='dbit')
cur=con.cursor()
os.system("cls");
print("Press 1. Create Account")
print("Press 2. Deposit Money")
print("Press 3. Withdrawal Money")
print("Press 4. Check balance")
print("Press 5. Tranfser money")
print("Press 6. Change pin")
print("Press 7. Exit ")

n=int(input("enter the choice : "))

if n==1:
     p=input("enter the password : ")
     na=input("enter the name : ")
     a=input("enter the address : ")
     g=input("enter the gender : ")
     ph=int(input("enter the phone number : "))
     e=input("enter the email : ")
     c=input("enter the country : ")
     st=input("enter the state : ")
     ct=input("enter the city : ")
     amt=int(input("enter the opening amount : "))
     ac="SBI"
     x=0
     s="select * from sbi"
     cur.execute(s)
     for dt in cur:
         x=x+1
     if x>0:
             x=x+1
             x=x+100
             ac=ac+str(x)
     else:
             ac="SBI101"

     q="insert into sbi values('"+ac+"','"+p+"','"+na+"','"+a+"','"+g+"',"+str(ph)+",'"+e+"','"+c+"','"+st+"','"+ct+"',"+str(amt)+")"
     cur.execute(q)
     con.commit()
     print("account created")


if n==3:
    a=input("enter the account number : ")
    p=input("enter the password : ")
    s="select * from sbi where acno='"+a+"' and pass='"+p+"'"
    camt=0
    x=0
    cur.execute(s)
    for d in cur:
        x=x+1
        camt=int(d[10])
    if x>0:
        wamt=int(input("enter the amount to withdrwal : "))
        if wamt<=camt:
            s="update sbi set cnt="+str(camt-wamt)+" where acno='"+a+"'"
            cur.execute(s)
            con.commit()
            print("after withdrawal ",(wamt),":","your current balance is :",camt-wamt)
        else:
            print("insufficient balance ")
    else:
        print("invalid account")

if n==2:
    a=input("enter account number : ")
    p=input("enter the password : ")
    s="select * from sbi where acno='"+a+"' and pass='"+p+"' "
    cur.execute(s)
    camt=0
    x=0
    for d in cur:
        x=x+1
        camt=int(d[10])
    if x>0:
        damt=int(input("enter the amount to deposit : "))
        damt=damt+camt
        s="update sbi set cnt="+str(damt)+" where acno='"+a+"' "
        cur.execute(s)
        con.commit()
        print("amount succefully deposited")
    else:
        print("invalid account")



if n==4:
    a = input("enter the account number : ")
    p = input("enter the password : ")
    s = "select * from sbi where acno='"+a+"' and pass='"+p+"' "
    cur.execute(s)
    x=0
    for dt in cur:
        x=x+1
    if x>0:
        print(dt[0],"\t",dt[1],"\t",dt[2],"\t",dt[3],"\t",dt[4],"\t",dt[5],"\t",dt[6],"\t",dt[7],"\t",dt[8],"\t",dt[9],"\t",dt[10])
    else:
        print("invalid account")


if n==5:
    a=input("enter the account : ")
    p=input("enter the password : ")
    s="select * from sbi where acno='"+a+"' and pass='"+p+"' "
    cur.execute(s)
    x=0
    camt=0
    for d in cur:
        x=x+1
        camt=int(d[10])
    if x>0:
        b=input("enter the account number for transfer : ")
        s="select * from sbi where acno='"+b+"' "
        cur.execute(s)
        z=0
        samt=0
        for d in cur:
             z=z+1
             samt=int(d[10])
        if  z>0:
            tamt=0
            tamt=int(input("enter the amount to tranfer"))
            if tamt<=camt:
                zamt=samt+tamt
                z="update sbi set cnt="+str(zamt)+" where acno='"+b+"' "
                cur.execute(z)
                con.commit()
                xamt=camt-tamt
                x = "update sbi set cnt="+str(xamt)+" where acno='"+a+"' "
                cur.execute(x)
                con.commit()
                print("money transferd")
            else:
                print("insufficient money to transfer")
        else:
            print("invalid account")
    else:
        print("invalid account")


if n==6:
    a=input("enter the account : ")
    p=int(input("enter the pin : "))
    d=" select * from sbi where acno='"+a+"' and pass="+str(p)+" "
    cur.execute(d)
    x=0
    for d in cur:
        x=x+1
    if x>0:
         pin=int(input("enter the new pin : "))
         s="update sbi set pass="+str(pin)+" where acno='"+a+"' "
         cur.execute(s)
         con.commit()
         print("password succesfully changed")
    else:
         print("invalid account")

if n==7:
    print("thank u")
    os.system("exit");
    
