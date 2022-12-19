# project/server/main/views.py

import os
import json
from flask import render_template, Blueprint
from flask import request



main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def home():
    return render_template("main/home.html")


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")



# @main_blueprint.route("/upload", methods=['POST'])
# def uploadhc():
#     isthisFile=request.files.get('file')
#     print("@@@@@@@@@@@@@@@")
#     print (isthisFile, request)
#     #f = request.files['userFile']
#     # path = "./static/{}".format(f.filename) 
#     # f.save((f.filename))
    
#     return json.dumps({'file': "success" , 'caption': ['A guy' , 'selfie']})



@main_blueprint.route("/upload", methods=['POST'])
def uploadhc():


    isthisFile=request.files.get('file')
    print (isthisFile, request)
    return json.dumps({'file': "success" ,'caption': ['A guy' , 'selfie']})




@app.route('/hiiiiii',methods = ['POST'])
def marks():

	if request.method == 'POST':

		f = request.files['userfile']
		path = "./static/{}".format(f.filename) 
		f.save(path)

		path2 = "./static/{}".format(f.filename) + ".mp3"

		caption = Caption_it.caption_this_image(path)
		output = gTTS(text = caption, lang = 'en',slow = False)
		output.save(path2)

		result_dic = {
		'image' : path,
		'caption' : caption,
		'sound' : path2
		}

	return render_template("index.html",your_result = result_dic)



