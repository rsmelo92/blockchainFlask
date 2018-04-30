from flask import Flask, render_template, request, jsonify
import chain
app = Flask(__name__)

@app.route("/")
def hello():
    # Generate genesis block on page load
    genesis = jsonify(chain.create_genesis_block());
    return render_template('main.html', genesis=genesis)

@app.route('/chain', methods=['POST'])
def chaining():
    previous_block = {
                        'index':request.form['index'],
                        'data':request.form['data'],
                        'hash':request.form['hash'],
                        'timestamp':request.form['timestamp'],
                     }
    data = chain.next_block(previous_block)
    return jsonify(data)