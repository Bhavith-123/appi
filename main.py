from flask import *
app = Flask(__name__)
app.secret_key = 'loginsessionwithb344’

@app.route('/')
def index():
   return render_template(url_for('login.html'))

@app.route('/login', methods = ['POST'])
def login ():
   if request.form['username'] = 'admin':
      return redirect(url_for('index.html'))
   return redirect(url_for('login.html'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
