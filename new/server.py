import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import random
app = Flask(__name__)


data = [
{
	"id": "1",
	"title": "banana peanut butter smoothie",
	"image": "",
	"Ingredients":["Banana", "Peanut butter", "soymilk", "honey"],
	"About": "Rich in protein, carbohydrates etc etc"
},
{
	"id": "2",
	"title": "Apple beetroot carrot",
	"image": "",
	"Ingredients":["Banana", "Peanut butter", "soymilk", "honey"],
	"About": "Rich in protein, carbohydrates etc etc"
},
{
	"id": "3",
	"title": "Pineapple strawberry smoothie",
	"image": "",
	"Ingredients":["Banana", "Peanut butter", "soymilk", "honey"],
	"About": "Rich in protein, carbohydrates etc etc"
},
{
	"id": "4",
	"title": "Oats whey protein smoothie",
	"image": "",
	"Ingredients":["Banana", "Peanut butter", "soymilk", "honey"],
	"About": "Rich in protein, carbohydrates etc etc"
},
]

quiz_questions = [
{
	"id" : "1",
	"question" : "Question 1",
	"option1": "Option A",
	"option2":"Option B", 
	"option3":"Option C",
	"option4": "Option D",
	"answer": "option1"

},
{
	"id" : "2",
	"question" : "Question 2",
	"option1": "Option A",
	"option2":"Option B", 
	"option3":"Option C",
	"option4": "Option D",
	"answer": "option4"

},
{
	"id" : "3",
	"question" : "Question 3",
	"option1": "Option A",
	"option2":"Option B", 
	"option3":"Option C",
	"option4": "Option D",
	"answer": "option2"

},
{
	"id" : "4",
	"question" : "Question 4",
	"option1": "Option A",
	"option2":"Option B", 
	"option3":"Option C",
	"option4": "Option D",
	"answer": "option1"

},
]

current_user = {"quiz_answers": {
"1" : "",
"2":"",
"3":"",
"4":""
}}


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/learn/<id>')
def learn(id=0):
	global data
	for item in data:
		if item['id'] == id: 
			return render_template('learn.html', item=item, id_next= str(int(id)+1))
	return learnfinish()

@app.route('/quiz/<id>')
def quiz(id=0):
	global quiz_questions
	for item in quiz_questions:
		if item['id'] == id:
			return render_template('quiz.html', item= item, quiz_id_next= str(int(id)+1))
	return quizfinish()

@app.route('/learnfinish')
def learnfinish():
		return render_template('learnfinish.html')


@app.route('/quizfinish')
def quizfinish():
		return render_template('quizfinish.html')

@app.route('/quizanswers/<id>/<option>')
def quizanswers(id, option):
	global current_user
	current_user['quiz_answers'][id] = option
	return "saved"


if __name__ == '__main__':
	app.run(debug = True)
