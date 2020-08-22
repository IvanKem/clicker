from flask import Flask, session, redirect, url_for, request, abort,render_template
from markupsafe import escape
import time
from config import secret
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = secret

login_dict ={}

@app.route('/')
def index():
    if 'username' in session:
        #return 'Logged in as %s' % escape(session['username'])
        return render_template('index.html')


    return redirect('/register')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        login_dict[session['username']] = session['password']

        return redirect('/')
    return '''
            <form style='text-align:center;' method="post">
                <span><h1>Регистрация</h1>
                <p><input type=text name=username placeholder = 'Login'>
                <p><input type=password name=password placeholder = 'Password'>
                <p><input type=submit value=Login></span>
            </form>
        '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not (request.form['username'] in login_dict and login_dict[request.form['username']] == request.form['password']):
            abort(401)
        session['username'] = request.form['username']
        session['password'] = request.form['password']


        return redirect('/')
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect('/')
app.run('0.0.0.0', debug=True, port=8080)