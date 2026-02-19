from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Destino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(100), nullable=False)
    país = db.Column(db.String(200), nullable=False)
    nota = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "destino": self.destino,
            "país": self.país,
            "nota": self.nota
        }