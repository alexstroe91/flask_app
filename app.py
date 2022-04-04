
from flask import Flask, render_template, request, Markup, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Niup123$%&@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = "TRUE"


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UserModel(db.Model, UserMixin):
    __tablename__ = 'Usuarios'

    id = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String(), nullable = False, unique = True)
    name = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)

    def __init__(self, name, email, password):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<Nombre: {self.name} - Email: {self.email}>"



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

    
