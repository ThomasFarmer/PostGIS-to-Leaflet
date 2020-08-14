from flask import Flask, render_template, redirect

from db import DbHandler
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET'])
def redirecttohome():
    return redirect("/home/", code=302)

@app.route('/home/', methods=['GET'])
def homepage():
    jsonstuff = d.get_stuff('poc_vienna_selection_fixed')
    return render_template('base.html', jsonstuff=jsonstuff)


if __name__ == '__main__':
    d = DbHandler()
    app.run(debug=True)

