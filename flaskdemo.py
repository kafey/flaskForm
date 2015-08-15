from flask import Flask , jsonify, render_template, request, jsonify, url_for, redirect
import json
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def index():
	online_users = mongo.db.users.find({'online': True})
	return render_template('index.html', online_users=online_users)


@app.route('/echo/', methods=['POST'])
def echo():
	data = request.data

	varRetrun = {'msg':'succes','code':'200'}
	varjsonReturn = json.dumps(varRetrun)
	return varjsonReturn

@app.route('/berhasil/')
def berhasil():
	data1 = [1, 2, 3, 4]
	return render_template('berhasil.html', data1=data1)



if __name__ == '__main__':
	app.run(port=8080, debug=True)
	
	


