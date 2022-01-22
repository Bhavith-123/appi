from flask import *
app = Flask(__name__)
app.secret_key = 'loginsessionwithb344’

@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
         return render_template(url_for('index.html', username=username))
   return render_template(url_for('login.html'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index.html'))
   return redirect(url_for('login.html'))

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index.html'))

if __name__ == '__main__':
    app.run(debug=True)
