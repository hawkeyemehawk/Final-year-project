from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def publichome():
	flash("Welcome...!")
	return render_template("home.html")

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['username']
		pas=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,pas)
		res=select(q)
		print(q)

		if res:
			session['login_id']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.admin_home'))
				flash("Successfully Loggin..!")
			elif res[0]['usertype']=="student":
				q="select * from student where login_id='%s'"%(session['login_id'])
				res=select(q)
				if res:
					session['sid']=res[0]['student_id']
				return redirect(url_for('student.student_home'))
				flash("Successfully Loggin..!")

			elif res[0]['usertype']=="teacher":
				q="select * from teacher where login_id='%s'"%(session['login_id'])
				res=select(q)
				if res:
					session['tid']=res[0]['teacher_id']
				return redirect(url_for('teacher.teacher_home'))
				flash("Successfully Loggin..!")
		else:
			flash("Invalid Username & Password....!")

	return render_template("login.html")

@public.route('/reg',methods=['get','post'])
def reg():
	if 'submit' in request.form:
		# fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		uname=request.form['username']
		pas=request.form['password']
		q="insert into login values(null,'%s','%s','families')"%(uname,pas)
		id=insert(q)
		q="insert into family values(null,'%s','%s','%s','%s','%s')"%(id,lname,place,phone,email)
		insert(q)
		flash("Registered Successfully...!")
		
		return redirect(url_for('public.login'))

	return render_template("reg.html")