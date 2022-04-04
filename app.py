
from flask import Flask, render_template, request
from models import *
from config import *
from werkzeug.security import check_password_hash


app = Flask(__name__)
setup(app)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = UserModel.query.filter_by(email = email).first()
    if request.method == 'POST':
        if user and check_password_hash(user.password, password):
            return render_template('index.html')
        else:
            return render_template('login.html', msg = "Revise sus credenciales.") 
    
    return render_template('login.html')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')

        emailRegistered = UserModel.query.filter_by(email = email).first()
        nameInUse = UserModel.query.filter_by(name = username).first()

        if password != confirmpassword:
            return render_template('signup.html', msg = "Las contraseñas no coinciden")
        elif emailRegistered:
            return render_template('signup.html', msg = "Email ya registrado")
        elif nameInUse:
            return render_template('signup.html', msg = "Nombre en uso")
            
        else:
            new_user = UserModel(name = username, email = email, password = password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('signup.html', msg = "Usuario creado")

    return render_template('signup.html')



if __name__ == "__main__":
    app.run(debug = True)

    
