from app import db

class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=True)
    lat = db.Column(db.String(18), unique=False, nullable=False)
    lon = db.Column(db.String(18), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=True)

    def __init__(self, id, name, lat, lon, description):
        self.id = id;
        self.name = name;
        self.lat = lat;
        self.lon = lon;
        self.description = description;

    def __repr__(self):
        return '<Name: {}>'.format(self.name)
