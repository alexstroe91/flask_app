from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from sqlalchemy import true
from models import *
from config import *
from werkzeug.security import check_password_hash
from datetime import datetime

app = Flask(__name__)
setup(app)
migrate = Migrate(app, db)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Necesitas iniciar sesión para ver esta página"

eventos = [
        {
            "id": "asdasd",
            "title": "Title1",
            "start": str(datetime.today().strftime('%Y-%m-%d')) + "00:00",
            "end": "2022-04-20 15:30"
        },
         {
            "id": "asdasd123",
            "title": "Title2",
            "start": datetime.today().strftime('%Y-%m-%d'),
            "end": "2022-04-18 12:30"
        }
    ]

db.init_app(app)

@app.route('/')
def index():
    #ELIMINAR O EDITAR A POSTERIORI, AHORA CON ACCESO A PÁGINAS PARA TESTEO
    return render_template('index.html')

#Login
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))


    #Inicia con el método GET
    email = request.form.get('email')
    password = request.form.get('password')
    user = UserModel.query.filter_by(email = email).first()

    #Al rellenar el formulario y presionar el botón pasa por la verficación
    if request.method == 'POST':
        if user and check_password_hash(user.password, password):
            login_user(user, remember = request.form.get('remember'))
            return redirect(url_for('saludo'))
        elif not user:
            flash("Usuario no encontrado")
        elif not check_password_hash(user.password, password):
            flash("Contraseña incorrecta")
        return render_template('login.html') 
    #Carga de HTML del método GET
    return render_template('login.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    created = False
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')
        
        #Verifica si el email está en uso o no
        emailRegistered = UserModel.query.filter_by(email = email).first()
        #Verifica si el nombre está en uso o no
        nameInUse = UserModel.query.filter_by(name = username).first()

        #Validación del registro
        if password != confirmpassword:
            flash("Las contraseñas no coinciden")
        elif emailRegistered:
            flash("Email ya registrado")
        elif nameInUse:
            flash("Nombre ya en uso")
        #Si está todo bien crea el usuario
        else:
            new_user = UserModel(name = username, email = email, password = password)
            db.session.add(new_user)
            db.session.commit()
            created = True
            flash("Usuario registrado exitosamente")

        return render_template('signup.html', created = created)
    #Carga de HTML del método GET
    return render_template('signup.html', created = created)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/saludo')
@login_required
def saludo():
    return render_template('pruebaLoginRequired.html')


@app.route('/modal')
def modal():
    
    return render_template('modal.html')

@app.route('/calendario', methods = ['GET', 'POST'])
@login_required
def calendario():
    if request.method == 'POST':
        app.logger.debug("Title: " + str(request.form.get('title')))
        app.logger.debug("StartDate: " + str(request.form.get('startDate')))
        app.logger.debug("EndDate: " + str(request.form.get('endDate')))
        app.logger.debug("StartTime: " + str(request.form.get('startTime')))
        app.logger.debug("EndTime: " + str(request.form.get('endTime')))

        title = request.form.get('title')
        start = str(request.form.get('startDate')) + " " + str(request.form.get('startTime'))
        end = str(request.form.get('endDate')) + " " + str(request.form.get('endTime'))

        new_event = EventModel(title = title, start = start, end = end)
        db.session.add(new_event)
        db.session.commit()
        return render_template('index.html')




    app.logger.debug("Prueba flask log")
    return render_template('calendario.html', today = datetime.today().strftime('%Y-%m-%d'))







#Extra
@login_manager.user_loader
def load_user(user_id):
    user = UserModel.query.filter_by(id = user_id).first()
    if user:
        return user
    return None  

if __name__ == "__main__":
    app.run(debug = true)
