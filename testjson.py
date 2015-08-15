import json

def json_dict():
	dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
	data = json.dumps(dict)
	return data

def dict_jason():
	data = json_dict()
	data = json.loads(data)
	return data

if __name__ == '__main__':
	print dict_jason()