def setup(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Niup123$%&@localhost:5432/flask"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = "TRUE"
    app.config['SECRET_KEY'] = "|/string\|/secreto\|"