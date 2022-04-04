from flask import Flask, redirect, render_template, request, Markup
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Niup123$%&@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = "TRUE"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class CarsModel(db.Model):
    __tablename__ = 'carsPrueba'

    matricula = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(), nullable = False)
    model = db.Column(db.String(), nullable = False)
    doors = db.Column(db.Integer(), nullable = False)

    def __init__(self, matricula, name, model, doors):
        self.matricula = matricula
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Matricula: {self.matricula} - Marca: {self.name} - Modelo: {self.model} - Puertas: {self.doors}>"



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cars', methods=['POST', 'GET'])
def handle_cars():
    error = ""
    message = ""
    try:
        if request.method == 'POST':
        
                new_car = CarsModel(
                    matricula=request.form['matricula'].upper(),
                    name=request.form['name'].upper(), 
                    model=request.form['model'].upper(), 
                    doors=int(request.form['doors']))

                db.session.add(new_car)
                db.session.commit()

                message = f"{new_car.name} añadido"
                return redirect('/cars')
        if request.method == 'GET':
            cars = CarsModel.query.all()
            coches = ""
            for car in cars:
                coches += "|" + str(car) + "|" + Markup("<br>")


    except Exception as ex:
            error = "No se pudo añadir el coche. Revise todos los campos"
            return render_template('pruebaPostCoche.html', error = error, message = message, results = coches)

    return render_template('pruebaPostCoche.html', error = error, message = message, results = coches)






@app.route('/cars/<car_id>', methods = ['GET', 'PUT', 'DELETE'])
def handle_car(car_matricula):
    car = CarsModel.query.get_or_404(car_matricula)

    if request.method == 'GET':
        response = {
            "matricula": car.matricula,
            "name": car.name,
            "model": car.model,
            "doors": car.doors
        }
        return {"message": "success", "car": response}
    
    elif request.method == 'DELETE':
        db.session.delete(car)
        db.session.commit()
        return {"message": f"Car {car.matricula} successfully deleted"}

if __name__ == "__main__":
    app.run(debug = True)
