from flask import *
from database import *
import uuid
teacher=Blueprint('teacher',__name__)

@teacher.route('/teacher_home')
def teacher_home():
	return render_template("teacher_home.html")

@teacher.route('/teacher_manage_exam',methods=['get','post'])
def teacher_manage_exam():
	
	data={}
	q="SELECT * FROM exam "
	res=select(q)
	data['mem']=res

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		q="insert into exam values(null,'%s','%s')"%(fname,lname)
		insert(q)
		flash('inserted successfully')
		return redirect(url_for('teacher.teacher_manage_exam'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="delete":
		q="delete from exam  where exam_id='%s'"%(id)
		update(q)
		flash('deleted successfully')
		return redirect(url_for('teacher.teacher_manage_exam'))

	if action=="update":
		q="select * from exam where exam_id='%s'"%(id)
		print(q)
		res=select(q)
		data['updater']=res

	if 'update' in request.form:
		
	
		lname=request.form['lname']
		place=request.form['place']
		
		
	
	
		q="update exam set exam='%s',detail='%s' where exam_id='%s'"%(fname,lname,id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('teacher.teacher_manage_exam'))
	

	return render_template('teacher_manage_exam.html',data=data)

@teacher.route('/teacher_manage_qn',methods=['get','post'])
def teacher_manage_qn():
	
	data={}
	q="SELECT * FROM exam "
	res=select(q)
	data['exam']=res


	q="SELECT * FROM question "
	res=select(q)
	data['qn']=res

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['ex']
		ans=request.form['lname']
		q="insert into question values(null,'%s','%s','%s')"%(lname,fname,ans)
		insert(q)
		flash('inserted successfully')
		return redirect(url_for('teacher.teacher_manage_qn'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="delete":
		q="delete from question  where question_id='%s'"%(id)
		update(q)
		flash('deleted successfully')
		return redirect(url_for('teacher.teacher_manage_qn'))

	if action=="update":
		q="select * from question where question_id='%s'"%(id)
		print(q)
		res=select(q)
		data['updater']=res

	if 'update' in request.form:
		
	
		fname=request.form['fname']
		ans=request.form['lname']
	
		q="update question set question='%s',answer='%s' where question_id='%s'"%(fname,ans,id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('teacher.teacher_manage_qn'))
	

	return render_template('teacher_manage_qn.html',data=data)


@teacher.route('/teacher_manage_ans',methods=['get','post'])
def teacher_manage_ans():
	
	data={}
	id=request.args['id']
	


	q="SELECT * FROM answer where question_id='%s'"%(id)
	res=select(q)
	data['mem']=res

	if 'submit' in request.form:
		
		lname=request.form['ex']
		q="insert into answer values(null,'%s','%s')"%(id,lname)
		insert(q)
		flash('inserted successfully')
		return redirect(url_for('teacher.teacher_manage_ans',id=id))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		
	else:
		action=None

	if action=="delete":
		q="delete from answer  where answer_id='%s'"%(id)
		update(q)
		flash('deleted successfully')
		return redirect(url_for('teacher.teacher_manage_ans'))

	if action=="update":
		q="select * from answer where question_id='%s'"%(id)
		print(q)
		res=select(q)
		data['updater']=res

	if 'update' in request.form:
		
	
		fname=request.form['ex']
		
		
		
	
	
		q="update answer set answer='%s' where answer_id='%s'"%(fname,id)
		update(q)
		flash('updated successfully')
		return redirect(url_for('teacher.teacher_manage_ans'))
	

	return render_template('teacher_manage_ans.html',data=data)


@teacher.route('/teacher_view_part',methods=['get','post'])
def teacher_view_part():
	
	data={}
	q="SELECT * FROM participate INNER JOIN student USING(student_id) INNER JOIN exam USING(exam_id) INNER JOIN question USING(exam_id) group by(student_id)"
	res=select(q)
	data['mem']=res
	return render_template('teacher_view_attend.html',data=data)


@teacher.route('/teacher_view_mark',methods=['get','post'])
def teacher_view_mark():
	
	data={}
	id=request.args['id']
	q="SELECT * FROM  exam INNER JOIN question USING(exam_id) inner join answer USING(question_id) "
	res=select(q)
	data['mem']=res
	return render_template('teacher_view_mark.html',data=data)
