#Modules Imported------------------------------------------------------------------------------------------------------------------------------
import mysql.connector as tor      #pip install mysql.connector             #used here for python-mysql connection
from clrprint import *                   #pip install clrprint                            #used here to print coloured results
import random                                                                                         #used generating random passwords for each student
import webbrowser as wb                                                                       #used here opening a site
import sys                                                                                                #used here for exiting the process
import string                                                                                            #used here to generate password
import csv                                                                                                #used here to create a csv file and store the passwords in it
import datetime                                                                                        #used here to store current date values
from prettytable import PrettyTable as PT     #pip install prettytable      #used here to print result in a table
from datetime import datetime as dfg                                                      #used here to store current time values
import time as qwerty
#----------------------------------------------------------------------------------------------------------------------------------------------
date=datetime.date.today()
now=dfg.now()
time=now.strftime("%H:%M")
tdelta=datetime.timedelta(days=90)
duedate=date+tdelta
#Connection------------------------------------------------------------------------------------------------------------------------------------
try:
    mycon=tor.connect(host="localhost",user="root",passwd="13")            #My MySQL password
except Exception:
    a=input("Enter MySQL Password : ")                                                  #If above passwords are not same as yours
    try:
        mycon=tor.connect(host="localhost",user="root",passwd=a)        
        if mycon.is_connected():
            pass
    except Exception:
        print("Wrong Password..........")                                                    #If you input your password wrong
        qwerty.sleep(5)
        ys.exit()
            
cursor=mycon.cursor()
cursor.execute("create database if not exists Student_Management_System")
cursor.execute("use Student_Management_System")
#----------------------------------------------------------------------------------------------------------------------------------------------

def password_generator():                       #Generates random password i.e, SCHOOL ID
    global regp,s3l,s4l
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s3l=list(s3)
    s4 = string.punctuation
    s4l=list(s4)
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    regp="".join(s[0:5])
    return regp

password_generator()

def adnogiver():                        #Finds out if any admission no. is missing and if found it allotes that admission no. to the student
    l=[]
    s=[]
    k=[]
    for i in range(1,10000):
        l.append(i)
    slt="select adno from stu_register"
    cursor.execute(slt)
    f=cursor.fetchall()
    for i in f:
        for j in i:
            s.append(j)
    for j in s:
        if j in l:
            l.remove(j)
    if l!=[] and l[0] not in s:       
        adno=l[0]
        ins1="insert into stu_register(stid,adno,sname,class,section,phno,adm_date) values (%s, %s, %s, %s, %s,%s,%s)"
        info_st=(regp,adno,sname,cls,sec,phno,date)
        cursor.execute(ins1,info_st)
        mycon.commit()
    else:
        info_st=(regp,sname,cls,sec,phno,date)
        cursor.execute(ins2,info_st)
        mycon.commit()
    sltadno="select adno from stu_register where stid=%s"
    cursor.execute(sltadno,b)
    f=cursor.fetchall()
    for i in f:
        print("Your ADM NO. is : ",i[0])
    clrprint("You Have Successfully Registered",clr = "Purple")
                    
def createcommands():           #Creates these tables if they do not exist
    sql1='''create table if not exists fee_structure(class int(2) primary key, annual decimal(7,2), monthly decimal(6,2),
    total decimal(7,2))'''
    cursor.execute(sql1)
    
    sql2='''create table if not exists stu_register (stid char(5),adno int auto_increment primary key, sname varchar(30),
    class int(2), section char(1) null, phno bigint(12), adm_date date)'''
    cursor.execute(sql2)
    
    sql3='''create table if not exists fee_pay(stid char(5),sname varchar(30),class int(2), fee_sub decimal(7,2),
    fee_due decimal(7,2),date_of_feesub date,due_date date null)'''
    cursor.execute(sql3)
    
createcommands()

def insertcommands():           #Inserts the following records if they do not exist in the table fee_structure
    fee1='''insert into fee_structure(class,annual,monthly,total) select* from(select 1 as Class,11500.00 as annual,
    1150.00 as monthly,25300.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 1) LIMIT 1'''
    
    fee2='''insert into fee_structure(class,annual,monthly,total) select* from(select 2 as Class,12000.00 as annual,
    1200.00 as monthly,26400.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 2) LIMIT 1'''

    fee3='''insert into fee_structure(class,annual,monthly,total) select* from(select 3 as Class,12000.00 as annual,
    1250.00 as monthly,27000.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 3) LIMIT 1'''
    
    fee4='''insert into fee_structure(class,annual,monthly,total) select* from(select 4 as Class,12000.00 as annual,
    1350.00 as monthly,28200.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 4) LIMIT 1'''

    fee5='''insert into fee_structure(class,annual,monthly,total) select* from(select 5 as Class,12000.00 as annual,
    1400.00 as monthly,28800.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 5) LIMIT 1'''
    
    fee6='''insert into fee_structure(class,annual,monthly,total) select* from(select 6 as Class,13000.00 as annual,
    1450.00 as monthly,30400.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 6) LIMIT 1'''
    
    fee7='''insert into fee_structure(class,annual,monthly,total) select* from(select 7 as Class,13000.00 as annual,
    1500.00 as monthly,31000.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 7) LIMIT 1'''
    
    fee8='''insert into fee_structure(class,annual,monthly,total) select* from(select 8 as Class,15000.00 as annual,
    1600.00 as monthly,34200.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 8) LIMIT 1'''
    
    fee9='''insert into fee_structure(class,annual,monthly,total) select* from(select 9 as Class,19000.00 as annual,
    2000.00 as monthly,43000.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 9) LIMIT 1'''
    
    fee10='''insert into fee_structure(class,annual,monthly,total) select* from(select 10 as Class,19000.00 as annual,
    2100.00 as monthly,44200.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 10) LIMIT 1'''
    
    fee11='''insert into fee_structure(class,annual,monthly,total) select* from(select 11 as Class,27500.00 as annual,
    2200.00 as monthly,53900.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 11) LIMIT 1'''
    
    fee12='''insert into fee_structure(class,annual,monthly,total) select* from(select 12 as Class,27500.00 as annual,
    2500.00 as monthly,57500.00 as total) as abc where not exists(SELECT class FROM fee_structure
                                                                  WHERE class = 12) LIMIT 1'''
    
    cursor.execute(fee1)
    cursor.execute(fee2)
    cursor.execute(fee3)
    cursor.execute(fee4)
    cursor.execute(fee5)
    cursor.execute(fee6)
    cursor.execute(fee7)
    cursor.execute(fee8)
    cursor.execute(fee9)
    cursor.execute(fee10)
    cursor.execute(fee11)
    cursor.execute(fee12)
    mycon.commit()
    
insertcommands()

def feestructure():             #Displays the specific fee structure of a class
    global lfee,cfee
    lfee=["Annual fee (To be paid at once) : ","Monthly fee : ","Total fees to be paid in Class"]
    clses=[1,2,3,4,5,6,7,8,9,10,11,12]
    a=int(clrinput("\nEnter Class : ",clr="green"))
    b=(a,)
    if a not in clses:
        clrprint("School affiliated from 1 to 12..........",clr="red")
        tasks()
    elif a<1:
        clrprint("Invalid Value ..........",clr="red")
    else:
        slt="select * from fee_structure where class=%s"
        cursor.execute(slt,b)
        f=cursor.fetchall()
        for i in f :
            for j in i:
                lfee.append(j)
        print()
        clrprint(lfee[0],"₹",lfee[4],clr="blue")
        print(lfee[1],"₹",lfee[5])
        clrprint(lfee[2],a,": ","₹",lfee[6],clr="green")
    
def displayer():                    #Displays the student details in a tabular form
    e=int(clrinput("\nEnter Class : ",clr="green"))
    if e>12:
        clrprint("School affiliated till 12...",clr="red")
        tasks()
    elif e<1:
        clrprint("Invalid Value ..........",clr="red")
    f=clrinput("Enter Section : ",clr="green")
    if f.lower() not in ["a","b","c","d"]:
        clrprint("Only 4 sections (A,B,C,D) available .......TRY AGAIN !!!",clr="red")
        tasks()
    data=(e,f)
    select="select sname,phno from stu_register where class=%s and section=%s order by sname"
    cursor.execute(select,data)
    fetcher=cursor.fetchall()
    print()
    p=PT()
    p.field_names=["Name","Phone Number"]
    for i in fetcher:
        p.add_row([i[0],i[1]])
    print(p)
              
def adnofinder():         #Checks if the inputted School ID is correct or not when doing admission      
    global b
    a=input("Enter ID : ")
    b=(a,)
    idcheck="select stid from stu_register"
    cursor.execute(idcheck)
    ids=cursor.fetchall()
    l=[]
    while True:
        for i in ids:
            for j in i:
                l.append(j)
        if a==regp:
            pass
        else:
            clrprint("Wrong ID..........TRY AGAIN",clr="red")
            adnofinder()
        break

#Insertion command
ins2="insert into stu_register(stid,sname,class,section,phno,adm_date) values (%s, %s, %s, %s, %s,%s)"

def checker():              #Checks whether the records of the student is already present or not
    global name,mobno
    selector="select sname, phno from stu_register"
    cursor.execute(selector)
    result=cursor.fetchall()
    for i in result:
        name=i[0]
        mobno=i[1]
        if phno==mobno:
            clrprint("Phone Number already registered..........",clr="red")
            tasks()
             
def adds():             #Adds the info of the new students
    global sname,phno,cls,sec
    sname=clrinput("\nEnter your name : ",clr="green")
    for i in sname:
        if i in s3l or i in s4l:
            clrprint("Inapproapriate Name..........TRY AGAIN",clr="red")
            tasks()
    phno=int(clrinput("Enter your mobile no. : ",clr="green"))
    checker()
    sec=""    
    if phno>999999999999 or phno<1000000000:
        clrprint("Invalid MobNo..........TRY AGAIN",clr="red")
        print()
        tasks()
    cls=int(clrinput("Enter class : ",clr="green"))
    if cls==11 or cls ==12:
        sub=int(clrinput("Enter 1. for PURE - SCIENCE   2. for BIO - SCIENCE   3. COMMERCE : ",clr="green"))
        if sub==2:
            sec="B"
        elif sub==1:
            sec="A"
        elif sub==3:
            l=["C","D"]
            random.shuffle(l)
            sec="".join(l[0])
        else:
            clrprint("Invalid Input..........Try Again !!",clr="red")
            print()
            tasks()
    elif cls>12:
        clrprint("School affiliated from 1 to 12..........",clr="red")
        print()
        tasks()
    elif cls<1:
        clrprint("Invalid Input ..........",clr="red")
        tasks()
    elif cls>=1 and cls<=10:
        l=["A","B","C","D"]
        random.shuffle(l)
        sec="".join(l[0])
    clrprint("Your School ID is : ",password_generator(),"\t\t......Remember It",clr="red")
    adnofinder()
    adnogiver()

def select():                   #For checking if student is registered before taking TC
    global lstids
    lstids=[]
    slt="select stid from stu_register"
    cursor.execute(slt)
    f=cursor.fetchall()
    for i in f:
        for j in i:
            lstids.append(j)

def tc():                   #Provides TC and if student is not registered it returns approapriate error message
    schlid=clrinput("\nEnter School ID : ",clr="green")
    l=["Admission No. : ","Name : ","Class : ","Phone No. : "]
    b=(schlid,)
    select()
    if schlid in lstids:
        slt="select adno,sname,class,phno from stu_register where stid=%s"
        cursor.execute(slt,b)
        f=cursor.fetchall()
        for i in f:
            for j in i:
                l.append(j)
        print()
        clrprint(l[0],l[4],clr="blue")
        clrprint(l[1],l[5],clr="blue")
        clrprint(l[2],l[6],clr="blue")
        clrprint(l[3],l[7],clr="blue")
        dlt="delete from stu_register where stid=%s"
        cursor.execute(dlt,b)
        mycon.commit()
        clrprint("\nYou have successfully been granted TC ..........",clr="red")
    else:
        clrprint("Record not found ..........",clr="red")
        tasks()

def checkfee():     #Checks whether School ID is present or not when submitting fees
    global lstu
    selector="select stid from stu_register"
    lstu=[]
    cursor.execute(selector)
    result=cursor.fetchall()
    for i in result:
        name=i[0]
        lstu.append(name)

def dispnamefee():          #Stores the name of the student from respective School ID for inserting it in the fee_pay table
    global pqr
    slt="select sname from stu_register where stid=%s"
    x=(stuid,)
    cursor.execute(slt,x)
    f=cursor.fetchone()
    for i in f:
        pqr=i

def selectforfee():             #Stores the total amount from the fee_structure table for the respective class
    x=(clsfee,)
    slt="select total from fee_structure where class=%s"
    cursor.execute(slt,x)
    f=cursor.fetchone()
    for i in f:
        tot=float(i)
    return(tot)

def fee_paychecker():           #Stores all the records in list format of fee_pay
    global lastl
    slt="select* from fee_pay"
    lastl=[]
    cursor.execute(slt)
    f=cursor.fetchall()
    for i in f:
        for j in i:
            lastl.append(j)
            
def duer():                 #Returns money if extra cash is given mistakenly
    global due
    due=total-subfee
    if due<0:
        q=0-due
        due=0
        clrprint("Returned Amount = Rs. ",round(q,2),clr="red")
    elif due==0:
        pass

def class_():           #Stores the Class from the respective School ID of the student
    global clsfee
    slt="select class from stu_register where stid=%s"
    x=(stuid,)
    cursor.execute(slt,x)
    f=cursor.fetchone()
    for i in f:
        clsfee=i

def displaydue():               #Stores the Due value
    global xyz
    slt="select fee_due from fee_pay where stid=%s"
    x=(stuid,)
    cursor.execute(slt,x)
    f=cursor.fetchone()
    if f==None:
        pass
    else:
        for i in f:
            xyz=i
            if xyz==0:
                clrprint("You have already done full payment .......... THANK YOU",clr="blue")
                tasks()
        return xyz

def pays():             #For the fee submission
    global stuid,subfee,total
    stuid=clrinput("\nEnter your School ID : ",clr="green")
    if len(stuid)>5:
        clrprint("Invalid ID ..........",clr="red")
        tasks()
    checkfee()
    if stuid not in lstu:
        clrprint("You Are Not Registered ..........",clr="red")
        tasks()
    class_()
    total=selectforfee()
    d=displaydue()
    displaydue()
    dispnamefee()
    a=1
    while a:
        sbfee=float(clrinput("Enter Fees : ",clr="green"))
        fee=str(sbfee)
        subfee=round(sbfee,2)
        if sbfee>99999:
            clrprint("You are exceeding amount value ..........",clr="red")
        elif sbfee<0:
            clrprint("Invalid Value ..........",clr="red")
        else:
            a=0
    fee_paychecker()
    if stuid in lastl:
        if subfee>=float(d):
            data=(d,stuid)
            x=(stuid,)
            y=(date,stuid)
            slt1="update fee_pay set fee_sub=fee_sub+%s where stid=%s"
            slt2="update fee_pay set fee_due=0 where stid=%s"
            slt3="update fee_pay set date_of_feesub=%s where stid=%s"
            slt4="update fee_pay set due_date=Null where stid=%s"
            cursor.execute(slt1,data)
            cursor.execute(slt2,x)
            cursor.execute(slt3,y)
            cursor.execute(slt4,x)
            mycon.commit()
            clrprint("\nTransaction Complete ..........","\t\tDate : ",date,"\tTime : ",time,clr="blue")
            clrprint("Returned Amount = Rs. ",(round(subfee-float(d),2)),clr="red")
            clrprint("Thanks For Full  Payment ..........",clr="green")
        else:
            data=(subfee,stuid)
            x=(subfee,stuid)
            y=(date,stuid)
            slt1="update fee_pay set fee_sub=fee_sub+%s where stid=%s"
            slt2="update fee_pay set fee_due=fee_due-%s where stid=%s"
            slt3="update fee_pay set date_of_feesub=%s where stid=%s"
            slt4="update fee_pay set due_date=Null where stid=%s"
            cursor.execute(slt1,data)
            cursor.execute(slt2,x)
            mycon.commit()
            clrprint("\nTransaction Complete ..........","\t\tDate : ",date,"\tTime : ",time,clr="blue")
            clrprint("Due : ",displaydue(),"\t\t\t\tTo be paid within : ",duedate,clr="red")
    else:
        duer()
        if subfee>total:
            subfee=total
            dedate=None
            slt2="insert into fee_pay values(%s,%s,%s,%s,%s,%s,%s)"
            data=(stuid,pqr,clsfee,subfee,due,date,dedate)
            cursor.execute(slt2,data)
            mycon.commit()
            clrprint("\nTransaction Complete ..........","\t\tDate : ",date,"\tTime : ",time,clr="blue")
            clrprint("Thanks For Full  Payment ..........",clr="green")
        elif subfee==total:
            subfee=total
            dedate=None
            slt2="insert into fee_pay values(%s,%s,%s,%s,%s,%s,%s)"
            data=(stuid,pqr,clsfee,subfee,due,date,dedate)
            cursor.execute(slt2,data)
            mycon.commit()
            clrprint("\nTransaction Complete ..........","\t\tDate : ",date,"\tTime : ",time,clr="blue")
            clrprint("Thanks For Full  Payment ..........",clr="green")            
        else:
            data=(stuid,pqr,clsfee,subfee,due,date,duedate)
            slt2="insert into fee_pay values(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(slt2,data)
            mycon.commit()
            clrprint("\nTransaction Complete ..........","\t\tDate : ",date,"\tTime : ",time,clr="blue")
            clrprint("Due : ",displaydue(),"\t\t\t\tTo be paid within : ",duedate,clr="red")
                      
def tasks():                #Main function of this code
    a=1
    try:
        while a:
            task=int(clrinput("\nEnter task no. : ",clr="purple"))
            if task==1:
                adds()
            elif task==2:
                feestructure()
            elif task==3:
                pays()
            elif task==4:
                tc()
            elif task==5:
                clrprint("Opened !!!",clr="blue")
                wb.open("www.iisasansol.org")
            elif task==6:
                displayer()
            elif task==7:
                clrprint("THANK YOU ...... VISIT AGAIN !!!",clr="green")
                fh=open("Passwords.txt","w")
                cursor.execute("select stid,sname from stu_register")
                f=cursor.fetchall()
                for i in f:
                    a=i[0]+"  "+i[1]
                    fh.write(a)
                    fh.write("\n")
                fh.close()
                qwerty.sleep(5)
                sys.exit()
            else:
                clrprint("Invalid Input..........Try Again !!!",clr="red")
    except Exception as e:
        clrprint("Invalid Input ..........",clr="red")
        tasks()
        

# ---------------------------------------------------------------MAIN-------------------------------------------------------------------------    
file=open("welcome.txt","w")
file.write('''\n********************      Welcome To INDIA INTERNATIONAL SCHOOL      ********************

                          1. New Admission    2. Fees structure
                          3. Submit Fees      4. Take TC
                          5. Open Browser     6. Display Class
                                        7. Exit''')
file.close()
file=open("welcome.txt")
r=file.read()
clrprint(r,clr="purple")

tasks()


