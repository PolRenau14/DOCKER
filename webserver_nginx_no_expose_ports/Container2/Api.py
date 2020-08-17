from flask import Flask, request
from json import loads
app = Flask(__name__)

@app.route('/')
def generate_invoice_df():
    x =  '{ "name":"Container2", "age":2, "city":"Container2"}'

    # parse x:
    y = loads(x)

    return y


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
