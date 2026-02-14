from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hellooo0022!, world!'

if __name__ == '__main__':
    app.run()

