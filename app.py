from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    try:
        return 'OKAY!'
    except Exception as e:
        return (str(e))

@app.route('/add/<first>/<second>')
def add(int(first), int(second)):
    return first + second

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)