from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
	return 'Hello world from Flask!'

app.run(debug=True,host='localhost',port=5000)
