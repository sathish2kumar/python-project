import sqlite3
con=sqlite3.connect("s.db")
print("connected with oracle")
cur=con.cursor()
print("cursor created")
class start:    
    def register(self):
        name=input("enter the username")
        word=input("enter the password")
        rows=[name,word]
        cur.execute("insert into register (username,password) values (:1,:2)",rows)
        cur.execute("commit")
        print("register sucessfully")
    def registeradmin(self):
        name_ad=input("enter the usename")
        word_ad=input("enter the password")
        rows=[name_ad,word_ad]
        cur.execute("insert into register1 (username,password) values (:1,:2)",rows)
        cur.execute("commit")
        print("register sucessfully")
    def login(self):
        a=input("enter the usename")
        b=input("enter the password")
        cur.execute("select count(*) from register")
        row=cur.fetchone()
        o=0
        m=0
        for i in range(0,row[0]):
            for j in range (0,2):
                cur.execute("select * from register")
                row=cur.fetchall()
                if(row[i][j]==a and row[i][j+1]==b):
                  
                    print("hellooo sucessfully")
                    m=1
                    cur.execute("select * from course")
                    row=cur.fetchall()
                    print(row)
                    op=int(input("enter the option"))
                    cur.execute("select count(*) from course")
                    row=cur.fetchone()
                    for i in range(0,row[0]):
                        cur.execute("select * from course")
                        row=cur.fetchall()
                        if(row[i][1]==op):
            
                            print("select valid option")
                            o=1
                            student_name=input("enter your name")
                            student_id=input("enter your rollnumber")
                            rows=[student_name,student_id,op]
                            cur.execute("""insert into student (student_name,student_id,course_id) values(:1,:2,:3)""",rows)
                            cur.execute("commit")
                            cur.execute("""select * from student""")                
                            rows=cur.fetchall()
                            print(rows)
                            print("register sucessfully")
                    if(o!=1):            
                        print("select course not valid")
        if(m!=1):
            print("you have not valid user")
    def admin(self):
        f=input("enter the usename")
        g=input("enter the password")
        cur.execute("select count(*) from register1")
        row=cur.fetchone()
        v=0
        for i in range(0,row[0]):
            for j in range (0,2):
                cur.execute("select * from register1")
                row=cur.fetchall()
                if(row[i][j]==f and row[i][j+1]==g):
                    
                    print("login sucessfully")
                    v=1
                    print("1.insert course")
                    print("2.delete course")
                    choice=int(input("enter your choice"))
                    if(choice==1):
                        print("insert course table")
                        course_name=input("enter course name")
                        course_id=input("enter course id")
                        rows=[course_name,course_id]
                        cur.execute("insert into course (course_name,course_id) values(:1,:2)",rows)
                        cur.execute("commit")
                        print("add sucessfully")
                    if(choice==2):
                        print("delete values in table")
                        cur.execute("druncate table student")
                        print("table delete sucessfully")
        if(v!=1):
            print("you have not valid admin")

obj=start()
while(1):
    print("1.register form")
    print("2.login form")
    print("3.admin register form")
    print("4.admin login form")
    choose=int(input("enter choice"))
    if(choose == 1):
        obj.register()  
    if(choose == 2):
        obj.login()
    if(choose == 3):
        obj.registeradmin()
    if(choose == 4):
        obj.admin()
  
                

            
            
            
            
            
            
