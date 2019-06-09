from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "สวัสดี"

if __name__ == '__main__':
    app.run()