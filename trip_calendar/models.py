from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import secrets
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Divvy(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.Integer, nullable=False)
    stoptime = db.Column(db.Integer, nullable=False)
    bikeid = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String)
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String)
    usertype = db.Column(db.String)
    gender = db.Column(db.String, nullable=True)
    birthday = db.Column(db.Integer, nullable=True)
    trip_duration = db.Column(db.Integer)

    def __init__(self, trip_id, starttime, stoptime, bikeid, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthday, trip_duration):
        self.trip_id = trip_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_duration

    def __repr__(self):
        return f'The following Trip has been added: {self.trip_id}'


class TripSchema(ma.Schema):
    class Meta:
        fields = ['tripid', 'starttime', 'stoptime',
                  'bikeid', 'from_station_id', 'from_station_name', 'to_station_id',
                  'to_station_name', 'usertype', 'gender', 'birthday', 'trip_duration']


trip_schema = TripSchema()
trips_schema = TripSchema(many=True)
