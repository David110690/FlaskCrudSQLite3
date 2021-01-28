from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Databases/tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

app.secret_key = "da8vi2.d"
@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', task = tasks)

@app.route('/create-task', methods=['POST'])
def create():
    task = Task(content=request.form['content'], title=request.form['title'], done=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('home'))
    

@app.route('/done/<id>')
def done(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete(id):
    task = Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port = 3000, debug = True)


