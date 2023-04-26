from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template("admin_home.html")


@admin.route('/admin_manage_student',methods=['get','post'])
def admin_manage_student():
	
	data={}
	q="SELECT * FROM student "
	res=select(q)
	data['mem']=res

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		uname=request.form['username']
		pas=request.form['password']

		q="insert into login values(null,'%s','%s','student')"%(uname,pas)
		id=insert(q)
		q="insert into student values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
		insert(q)
		flash('inserted successfully')
		return redirect(url_for('admin.admin_manage_student'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="delete":
		q="delete from student  where student_id='%s'"%(id)
		update(q)
		flash('deleted successfully')
		return redirect(url_for('admin.admin_manage_student'))

	if action=="update":
		q="select * from student where student_id='%s'"%(id)
		print(q)
		res=select(q)
		data['updater']=res

	if 'update' in request.form:
		
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		
	
	
		q="update student set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where student_id='%s'"%(fname,lname,place,phone,email,id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('admin.admin_manage_student'))
	

	return render_template('admin_manage_student.html',data=data)


@admin.route('/admin_manage_staff',methods=['get','post'])
def admin_manage_staff():
	
	data={}
	q="SELECT * FROM teacher "
	res=select(q)
	data['mem']=res

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		sub=request.form['sub']
		uname=request.form['username']
		pas=request.form['password']

		q="insert into login values(null,'%s','%s','teacher')"%(uname,pas)
		id=insert(q)
		q="insert into teacher values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email,sub)
		insert(q)
		flash('inserted successfully')
		return redirect(url_for('admin.admin_manage_staff'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="delete":
		q="delete from teacher  where teacher_id='%s'"%(id)
		update(q)
		flash('deleted successfully')
		return redirect(url_for('admin.admin_manage_staff'))

	if action=="update":
		q="select * from teacher where teacher_id='%s'"%(id)
		print(q)
		res=select(q)
		data['updater']=res

	if 'update' in request.form:
		
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		
	
	
		q="update teacher set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where teacher_id='%s'"%(fname,lname,place,phone,email,id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('admin.admin_manage_staff'))
	

	return render_template('admin_manage_staff.html',data=data)

@admin.route('/admin_view_exam',methods=['get','post'])
def admin_view_exam():
	
	data={}
	q="SELECT * FROM exam "
	res=select(q)
	data['mem']=res
	return render_template('admin_view_exam.html',data=data)


@admin.route('/admin_view_qn',methods=['get','post'])
def admin_view_qn():
	
	data={}
	id=request.args['id']
	q="SELECT * FROM question where exam_id='%s' "%(id)
	res=select(q)
	data['qn']=res
	return render_template('admin_view_qn.html',data=data)

@admin.route('/admin_view_mark',methods=['get','post'])
def admin_view_mark():
	
	data={}
	id=request.args['id']
	q="SELECT * FROM  exam INNER JOIN question USING(exam_id) INNER JOIN answer USING(question_id) INNER JOIN student ON student.student_id=answer.user_id where question_id='%s' "%(id)
	res=select(q)
	data['mem']=res
	return render_template('admin_view_mark.html',data=data)