from flask import render_template, flash, redirect
from flask import Flask, request
from forms import LoginForm
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username':'Suresh'}
    return render_template('index.html',title='Learning AWS', user=user)


@app.route('/login')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_form_post():
    username= request.form['username']
    password= request.form['password']
    if username=='admin' and password=='admin123':
        return render_template('index.html',title='Learning AWS', user={'username':username})
    else:
        return "Authorization failed, Invalid credentials"

#def login():
 #   form = f.LoginForm()
  #  if form.validate_on_submit():
   #     flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    #    return redirect('/index')
#    return render_template('login.html', title='Sign In', form=form)

@app.route('/uc')
def uc():
    user = {'username':'Suresh'}
    return render_template('lambda.html',title='Learning AWS', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
