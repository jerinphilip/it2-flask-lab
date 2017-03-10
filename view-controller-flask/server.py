# File: server.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    # templates/layout.html
   return render_template('layout.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)
