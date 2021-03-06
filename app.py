# APP.PY
import os
from flask import Flask, request, jsonify

from script import mainFunction

app = Flask(__name__)

@app.route('/')
def home():
    text = request.args.get('text', type=str)
    result = mainFunction(text)
    return result

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
