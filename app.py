from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html', name=request.args.get("name"))



if __name__ == "__main__":
     app.run(debug=True, port=8000) 