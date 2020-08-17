from flask import Flask, request
from json import loads
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def generate_invocie_df():
	x = {"info":"Executing right now {}".format(datetime.now())}
	return loads(x)

if __name__ =="main":
	app.run(host='0.0.0.0', port='5000')
