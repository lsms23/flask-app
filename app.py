from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello MSOE, my applicayion has been enhanced! :)'

