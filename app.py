from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///funccforce.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Funccforce(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    coll = db.Column(db.String(200), nullable = False)
    dept = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__ (self) -> str:
        return f"{self.sno} - {self.name}"
  
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        name = request.form['name']
        coll = request.form['coll']
        dept = request.form['dept']
        funccforce = Funccforce(name=name, coll=coll, dept=dept)
        db.session.add(funccforce)
        db.session.commit()
    allFunccforce=Funccforce.query.all()
    return render_template('index.html', allFunccforce=allFunccforce)

@app.route('/info')
def info():
    allFunccforce = Funccforce.query.all()
    print(allFunccforce)
    return 'info page' 
 

if __name__ == "__main__":
     app.run(debug=True, port=8000) 