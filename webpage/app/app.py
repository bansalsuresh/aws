from flask import render_template
from flask import Flask
from forms import LoginForm
app = Flask(__name__)

@app.route('/')
def hello_world():
    user = {'username':'Suresh'}
    return render_template('index.html',title='Learning AWS', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
