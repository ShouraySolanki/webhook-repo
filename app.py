from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_route():
    return 'Welcome guys'

@app.route('/github', methods=['POST'])
def api_github_message():
    if request.headers['Content-Type'] == 'application/json':
        info = json.dumps(request.json)
        print(info)
        return info

if __name__ == '__main__':
    app.run(debug=True)            