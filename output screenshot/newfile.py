import sqlite3 
con=sqlite3.connect("s.db")
print("***********************")
print("*CONNECTED WITH ORACLE*")
print("***********************")
print("\n")
cur=con.cursor()
print("****************")
print("*cursor created*")
print("****************")
print("\n")
class student:    
    def register(self):
        name=input("Enter the username:")
        word=input("Enter the password:")
        c=0
        d=0
        n=0
        if(len(word)>=5):
    
            for i in range(0,len(word)):
                if(word[i].isupper()):
                    c=c+1
                elif(word[i].islower()):
                    d=d+1
                else:
                    n=n+1
            if(2<=c and d!=0 and n!=0):
                rows=[name,word]
                cur.execute("insert into stureg (username,password) values (:1,:2)",rows)
                cur.execute("commit")
                print("\n")
                print("**********************")
                print("*Register sucessfully*")
                print("**********************")
                print("\n")
            else:
                print("\n")
                print("*************************************************************")
                print("*you entered 2 uppercase,atleast one lowercase and one numer*")
                print("*************************************************************")
                print("\n")
        else:
            print("\n")
            print("*****************")
            print("*max 5 character*")
            print("*****************")
            print("\n")
    def login(self):
        a=input("Enter The Username:")
        b=input("Enter The Password:")
        cur.execute("select count(*) from stureg")
        row=cur.fetchone()
        o=0
        m=0
        for i in range(0,row[0]):
            j=0
            cur.execute("select * from stureg")
            row=cur.fetchall()
            if(row[i][j]==a and row[i][j+1]==b):
                print("\n")
                print("*******************")  
                print("*Login sucessfully*")
                print("*******************")
                print("\n")
                cur.execute("select count(*) from course")
                row1=cur.fetchone()
                cur.execute("select * from course")
                row=cur.fetchall()
                print("\n")
                print("********************************")
                print("NAME || ID || AMOUNT || DURATION || PHNO ||")
                for i in range(0,row1[0]):
                    for j in range(0,5):
                        print(row[i][j],end="   ||")
                    print("\n")
                print("********************************")
                print("\n")
                op=int(input("Enter the option (OR) Coursecode"))
                for i in range(0,row1[0]):
                    o=1
                    cur.execute("select * from course")
                    row=cur.fetchall()
                    if(row[i][1]==op):
                        print("\n")
                        print("********************************")
                        print("*YOU HAVE SELECT CORRECT OPTION*")
                        print("********************************")
                        print("\n")
                        n=1
                        student_name=input("Enter your Name:")
                        student_id=input("Enter your Rollnumber:")
                        addr=input("Enter your Address:")
                        phno=input("Enter your Phno:")
                        rows=[student_name,student_id,op,addr,phno]
                        cur.execute("""insert into student (student_name,student_id,course_id,addr,phno) values(:1,:2,:3,:4,:5)""",rows)
                        cur.execute("commit")
                        print("\n")
                        print("********************************************")
                        print("  payment pay using Bank amount=",row[i][2])
                        print("********************************************")
                        print("\n")
                        bn=input("Enter your BankName:")
                        ac=int(input("Enter your Account no:"))
                        am=int(input("Enter your Amount:"))
                        cur.execute("select count(*) from bank")
                        row=cur.fetchone()
                        for i in range(0,row[0]):
                            cur.execute("select * from bank")                
                            row=cur.fetchall()
                            if(row[i][0]==ac and row[i][2]==bn):
                                    money=row[i][1]-am
                                    m=1;
                                    print("\n")
                                    print("**********************")
                                    print("*Pay FEES Sucessfully*")
                                    print("**********************")
                                    print("\n")
                                    print("*****************************")
                                    print("*Course Register Sucessfully*")
                                    print("*****************************")
                                    print("\n")
                                    sql="""update bank set amount = (?) where acno = (?)"""
                                    data=(money,ac)
                                    cur.execute(sql, data)
                                    con.commit()
                            
                        if(m!=1):
                            print("\n")
                            print("*************************")
                            print("*you select invalid acno*")
                            print("*************************")
                            print("\n")
                if(n!=1):
                    print("\n")
                    print("*****************************")
                    print("*you select invalid courseid*")
                    print("*****************************")
                    print("\n")
        if(o!=1):
            print("\n")
            print("**************")
            print("*invalid user*")
            print("**************")
            print("\n")
class admin:
    def adminlogin(self):
        f=input("Enter the username:")
        g=input("Enter the password:")
        cur.execute("select count(*) from register")
        row=cur.fetchone()
        v=0
        for i in range(0,row[0]):
            j=0
            cur.execute("select * from register")
            row=cur.fetchall()
            if(row[i][j]==f and row[i][j+1]==g):
                print("\n")
                print("*******************")  
                print("*Login sucessfully*")
                print("*******************")
                print("\n")
                v=1
                while(1):
                    print("\n")
                    print("*****************************************")
                    print("*   1.INSER COURSE                      *")
                    print("*   2.DELETE COURSE                     *")
                    print("*   3.STUDENT SELECTED COURSE DISPLAY   *")
                    print("*   4.exit                              *")
                    print("*****************************************")
                    print("\n")
                    choice=int(input("Entr your choice:"))
                    if(choice==1):
                        print("\n")
                        print("*********************")
                        print("*Insert course Table*")
                        print("*********************")
                        print("\n")
                        course_name=input("Enter course name:")
                        course_id=input("Enter course id:")
                        fees=input("Enter fees:")
                        dur=input("Enter course duration:")
                        phno=input("Enter course phno:")
                        rows=[course_name,course_id,fees,dur,phno]
                        cur.execute("insert into course (course_name,course_id,amount,duration,phno) values(:1,:2,:3,:4,:5)",rows)
                        cur.execute("commit")
                        print("\n")
                        print("********************************")
                        print("* Add course detail Sucessfully*")
                        print("********************************")
                        print("\n")
                    if(choice==2):
                        print("\n")
                        print("*****************************************")
                        print("*   1.FULL TABLE                        *")
                        print("*   2.SELECTED ROW                      *")
                        print("*****************************************")
                        print("\n")
                        ch=int(input("Entr your choice:"))
                        if(ch==1):
                            cur.execute("delete from course")
                            cur.execute("commit")
                            print("\n")
                            print("*******************************")
                            print("*Table delete full sucessfully*")
                            print("*******************************")
                            print("\n")
                        if(ch==2):
                            cname=input("Enter Course Name:")
                            cur.execute("delete from course where course_name = ?",[cname]);
                            cur.execute("commit")
                            print("\n")
                            print("*********************************")
                            print("*Delete selected row sucessfully*")
                            print("*********************************")
                            print("\n")
                    if(choice==3):
                        print("\n")
                        print("*****************************************")
                        print("*   1.FULL TABLE                        *")
                        print("*   2.SELECTED ROW                      *")
                        print("*****************************************")
                        print("\n")
                        ch=int(input("Enter your choice:"))
                        if(ch==1):
                            cur.execute("select count(*) from student")
                            row1=cur.fetchone()
                            cur.execute("select * from student order by course_id")
                            row=cur.fetchall()
                            print("\n")
                            print("********************************")
                            print("NAME||  ID||  COURSEID||  ADDR||  PHNO||")
                            for i in range(0,row1[0]):
                                for j in range(0,4):
                                    print(row[i][j],end="  ||")
                                print("\n")
                            print("********************************")
                            print("\n")
                            print("*****************************************")
                            print("*      ENTER COURSE ID IT COUNT         *")
                            print("*****************************************")
                            print("\n")
                            cid=int(input("Enter Course Id"))
                            cur.execute("select count(course_id) from student where course_id = ?",[cid])
                            row=cur.fetchone()
                            print("COUNT =",row[0])
                        if(ch==2):
                            cid=int(input("Enter Course Id:"))
                            cur.execute("select count(course_id) from student where course_id = ?",[cid])
                            row1=cur.fetchone()
                            cur.execute("select * from student group by student_id having course_id = ?",[cid])
                            row=cur.fetchall()
                            print("NAME||  ID||  COURSEID||  ADDR|| PHNO||")
                            for i in range(0,row1[0]):
                                for j in range(0,4):
                                    print(row[i][j],end="   ||")
                                print("\n")
                            
                            
                    if(choice==4):
                        break
        if(v!=1):
             print("\n")
             print("**************")
             print("*invalid user*")
             print("**************")
             print("\n")
                    

obj=student()
oad=admin()
while(1):
    print("*****************************************")
    print("*   1.ADMIN LOGIN                       *")
    print("*   2.STUDENT REGISTER                  *")
    print("*   3.STUDENT LOGIN                     *")
    print("*   4.exit                              *")
    print("*****************************************")
    print("\n")
    choose=int(input("Enter Your Choice:"))
    if(choose == 1):
        oad.adminlogin()  
    if(choose == 2):
        obj.register()
    if(choose == 3):
        obj.login()
    if(choose == 4):
        print("\n")
        print("*********************************")
        print("*      T H A N K Y O U!!!       *")
        print("*********************************")
        print("\n")
        break
  
                

            
            
            
            
            
            
