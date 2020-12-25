from flask import Flask,render_template 
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/login')
def login():
   return render_template('auth/login.html')

@app.route('/register')
def register():
   return render_template('auth/register.html')

if __name__ == '__main__':
   app.debug = True
   app.run()