from flask import Flask, render_template, request, jsonify
import chain
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html')

@app.route('/chain', methods=['GET'])
def chaining():
    data = chain.start() 
    print request.get_json()
    return jsonify(data)