from flask import Flask
from db import db
from routes.produto_routes import produto_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(produto_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)