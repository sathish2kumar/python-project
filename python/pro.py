class start:
	def register(self):
		name=input("enter the usename")
		word=input("enter the password")
		cur.execute("""insert into register values(self.name,self.word)""")
		print("register sucessfully")
	def registeradmin(self):
		name_ad=input("enter the usename")
		word_ad=input("enter the password")
		cur.execute("""insert into register1 values(self.name_ad,self.word_ad)""")
		print("register sucessfully")	
        def login(self):
                self.a=input("enter the usename")
		self.b=input("enter the password")
		self.c=cur.execute("""select username from register where username=self.a""")
                self.d=cur.execute("""select password from register where password=self.b""")
	        if(self.c==self.a or self.d==self.b):
			print("login sucessfully")
                        cur.execute("""select * from course""")
                        cur.fetchall()
                        self.op=input("enter the option")
			self.option=cur.execute("""select option from course where option=self.op""")
                        if(self.option==self.op):
				print("select valid option")
				self.student_name=input("enter your name")
                                self.student_id=input("enter your rollnumber")
                                cur.execute("""insert into student values(self.student_name,self.student_id,self.option)""")
                                cur.execute("""select * from student""")
				cur.fetchall()
				print("register sucessfully")
                        else:
                                print("select course not valid")
                 else:
                        print("you have not valid user")
        def admin(self,f,g):
                self.f=input("enter the usename")
		self.g=input("enter the password")
		self.h=cur.execute("""select username from register where username=self.f""")
                self.l=cur.execute("""select password from register where password=self.g""")
	        if(self.h==self.f or self.l==self.g):
			print("login sucessfully")
                        print("1.insert course")
                        print("2.add course")
                        print("3.delete course")
                        choice=input("enter your choice")
                        if(choice==1):
                        	print("insert course table")
                        	course_name=input("enter course name")
                        	course_id=input("enter course id")
                        	cur.execute("insert into values(course_name,course_id)")          			 
			if(choice==2):
				print("add course table")
				course_name=input("enter course name")
                        	course_id=input("enter course id")
                        	cur.execute("alter table student add values(course_name,course_id)")
			if(choice==3):
                                print("delete values in table")
                                cur.execute("druncate table student")
				print("table delete sucessfully")
		else:
			print("you have not valid admin")

obj=start()
print("1.register form")
print("2.login form")
print("3.admin register form")
print("4.admin login form")
choose=int(input("enter choice")
if(choose == 1):
	obj.register()
if(choose == 2):
        obj.login()
if(choose == 3):
	obj.registeradmin()
if(choose == 4):
        obj.admin()
  
				