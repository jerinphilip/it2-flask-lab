from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test3.db'
db = SQLAlchemy(app)

# Model Definitions
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name


# Controllers
@app.route("/addUser", methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        print(name, email)

        user = User(name, email)
        db.session.add(user)
        db.session.commit()
        return redirect('/users')
    else:
        return render_template('form.html')


@app.route("/users")
def get_users():
  users = User.query.all()
  return render_template('layout.html', users=users)

db.create_all()

if __name__ == "__main__":
  app.run()
