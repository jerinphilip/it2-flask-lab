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
@app.route("/addUser")
def add_user():
  name = request.args.get("name")
  email = request.args.get("email")
  print(name, email)

  user = User(name, email)
  db.session.add(user)
  db.session.commit()
  return "Successfully added"

@app.route("/users")
def get_users():
  users = User.query.all()
  return render_template('layout2.html', users=users)

db.create_all()

if __name__ == "__main__":
  app.run()
