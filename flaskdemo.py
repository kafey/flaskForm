from flask import Flask , jsonify, render_template, request, jsonify, url_for, redirect
import json
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'kirim'
mongo = PyMongo(app, config_prefix='MONGO')



@app.route('/')
def index():
	# post = {"author":"mike","text":"jiii"}  
	# posts = mongo.db.posts  
	# posts.insert(post)
	# posts = posts.find()
	return render_template("index.html")


@app.route('/echo/', methods=['POST'])
def echo():
	data = request.data
	print data
	data1 = json.loads(data)
	mydict = {}
	for dic in data1:
		mydict.update( { dic['name']:dic['value'] } )
		
	mongo.db.transaksi.insert(mydict)
	varRetrun = {'msg':'succes','code':'200'}
	varjsonReturn = json.dumps(varRetrun)
	return varjsonReturn

@app.route('/berhasil/')
def berhasil():
	# nama = mongo.db.transaksi.find()
	nama = mongo.db.transaksi.find().skip(mongo.db.transaksi.count() - 1)
	# for item in nama:
	# 	print item["fname1"]
	# 	print item["frm2"]
	# 	print item["frm3"]
	return render_template('print.html', nama=nama)



if __name__ == '__main__':
	app.run(port=8080, debug=True)
	
	


