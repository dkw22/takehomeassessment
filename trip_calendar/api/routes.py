from flask import Blueprint, request, jsonify
from trip_calendar.models import db, Divvy, trip_schema, trips_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return {'some': 'value'}

# CREATE CHARCTER ENDPOINT


@api.route('/insert-trips', methods=['POST'])
def create_trip():
    trip_id = request.json['trip_id']
    starttime = request.json['starttime']
    stoptime = request.json['stoptime']
    bikeid = request.json['bikeid']
    from_station_id = request.json['from_station_id']
    from_station_name = request.json['from_station_name']
    to_station_id = request.json['to_station_id']
    to_station_name = request.json['to_station_name']
    usertype = request.json['usertype']
    gender = request.json['gender']
    birthday = request.json['birthday']
    trip_duration = request.json['trip_duration']

    trip = Divvy(trip_id, starttime, stoptime, bikeid, from_station_id, from_station_name,
                 to_station_id, to_station_name, usertype, gender, birthday, trip_duration)

    db.session.add(trip)
    db.session.commit()

    response = trip_schema.dump(trip)
    return jsonify(response)


@api.route('/trips', methods=['GET'])
def get_trips():
    trips = Divvy.query.all()
    response = trips_schema.dump(trips)
    print(response)
    print(trips)
    return jsonify(response)


@ api.route('/trips/<trip_id>', methods=['GET'])
def get_trip(trip_id):
    trip = Divvy.query.get(trip_id)
    response = trip_schema.dump(trip)
    return jsonify(response)
