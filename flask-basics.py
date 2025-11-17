from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! Let's build Flask apps."

if __name__ == '__main__':
    app.run(debug=True)