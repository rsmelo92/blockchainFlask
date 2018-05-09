from flask import Flask, render_template, request, jsonify
import chain
app = Flask(__name__)

@app.route("/<hashType>")
def hello(hashType):
    print hashType
    # Generate genesis block on page load
    genesis = jsonify(chain.create_genesis_block(hashType));
    return render_template('main.html', genesis=genesis, param=hashType)

@app.route('/chain/<hashType>', methods=['POST'])
def chaining(hashType):
    previous_block = {
                        'index':request.form['index'],
                        'data':request.form['data'],
                        'hash':request.form['hash'],
                        'timestamp':request.form['timestamp'],
                     }
    data = chain.next_block(previous_block, hashType)
    return jsonify(data)