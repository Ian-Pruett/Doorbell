from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    response = {'status': 1, 'message': 'server works'}
    response = jsonify(response)
    return response, 200

if __name__ == "__main__":
    app.run()