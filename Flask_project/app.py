from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error adding the task. Please try again'
        
    else:
        tasks = Todo.query.order_by(Todo.created_at).all()
        return render_template("index.html", tasks=tasks)

@app.route('/delete/<int:id>')

def delete(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting the task. Please try again'

@app.route('/update/<int:id>', methods=['POST', 'GET'])

def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        pass
        
    else:
        return render_template("update.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)



