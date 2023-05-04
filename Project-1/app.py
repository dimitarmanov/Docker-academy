from datetime import datetime

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return jsonify({
        "status": "OK",
        "time": datetime.now()
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")