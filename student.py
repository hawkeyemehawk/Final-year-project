from flask import *
from database import *
from test import *
import uuid
import pytesseract
import cv2
from PIL import Image


student=Blueprint('student',__name__)

def ocrgenerate(path):
    print("path===",path)
    image = cv2.imread(path)
    # print(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Store grayscale image as a temporary file to apply OCR
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)

    # Load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename))

    print("OCR Text is " + text.strip())
    # val=text.strip().split('D')
    # atte=val[0].split(',')
    # print(atte[0],atte[1])
    # # print(val[1])
    return  text.strip()


@student.route('/student_home')
def student_home():
	return render_template("student_home.html")

@student.route('/student_view_exam')
def student_view_exam():
	data={}
	q="select * from exam"
	data['exam']=select(q)
	return render_template("student_view_exam.html",data=data)


@student.route('/student_attend',methods=['get','post'])
def student_attend():
	
	data={}
	id=request.args['id']
	
	q="select * from exam"
	data['ex']=select(q)

	q="SELECT * FROM exam inner join participate using(exam_id) where student_id='%s'"%(session['sid'])
	res=select(q)
	data['exam']=res

	if 'submit' in request.form:
		
		lname=request.form['ex']
		q="insert into participate values(null,'%s','%s')"%(session['sid'],id)
		insert(q)
		flash('attended successfully')
		return redirect(url_for('student.student_view_qn',id=id))

	return render_template("student_attended.html",data=data)

@student.route('/student_view_qn',methods=['get','post'])
def student_view_qn():
	
	data={}
	id=request.args['id']

	q="SELECT * FROM exam inner join question using(exam_id)"
	res=select(q)
	data['qn']=res

	# if 'submit' in request.form:
		
	# 	lname=request.form['ex']
	# 	q="insert into participate values(null,'%s','%s')"%(session['sid'],id)
	# 	insert(q)
	# 	flash('inserted successfully')
	# 	return redirect(url_for('student.student_attend',id=id))
	
	
	# if 'submit' in request.form:
	# 	print("test..")
	# 	lname=request.form['ans'+str(i)]
	# 	qid=request.form['qid'+str(i)]
	# 	q="insert into answer values(null,'%s','%s')"%(qid,lname)
	# 	print(q)
	# 	insert(q)
	# 	flash('Answered..!')
	# 	return redirect(url_for('student.student_view_qn',id=id))

	return render_template("student_view_qn.html",data=data)


@student.route('/student_answer',methods=['get','post'])
def student_answer():
	
	data={}
	id=request.args['id']

	q="SELECT * FROM  question where question_id='%s' " %(id)
	res=select(q)
	data['mem']=res

	

	if 'submit' in request.form:
		lname=request.files['ans']
		path='static/uploads'+str(uuid.uuid4())+lname.filename
		lname.save(path)
		test=ocrgenerate(path)
		ans=data['mem'][0]['answer']

		out=checkans(ans,test)
		print(out)

		q="select * from answer where question_id='%s' and user_id='%s'"%(id,session['sid'])
		re=select(q)
		if re:
			flash("already Answered....!")
		else:

			q="insert into answer values(null,'%s','%s','%s','%s')"%(id,path,session['sid'],out)
			insert(q)
			flash('Answered..!')
			return redirect(url_for('student.student_view_qn',id=id))

	return render_template("student_answer.html",data=data)

@student.route('/std_ans')
def std_ans():
	data={}
	q="SELECT * FROM exam inner join question using(exam_id) inner join answer using(question_id) where user_id='%s'"%(session['sid'])
	data['exam']=select(q)
	return render_template("std_ans.html",data=data)