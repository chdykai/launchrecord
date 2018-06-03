from launchrecord import app, db
from launchrecord.models import RocketSeries, Rocket, Spaceport, LaunchComplex, Record, Country
import csv


def load_data(csv_file):
    with open(csv_file, 'rb', encoding='utf-8') as f:
        data = csv.reader(f)
        for row in data:
            yield row


def insert_country(data):
    for row in data:
        country = Country(name_en=row[1], name_zh=row[2], abbr=row[3])
        db.session.add(country)

    db.session.commit()


def insert_spaceport(data):
    for row in data:
        spaceport = Spaceport(name_en=row[1], name_zh=row[2], abbr=row[3],
                              country_id=Country.query.filter_by(name_zh=row[4]).id)
        db.session.add(spaceport)

    db.session.commit()


def insert_rocket_series(data):
    for row in data:
        rocket_series = RocketSeries(name_en=row[1], name_zh=row[2],
                                     country_id=Country.query.filter_by(name_zh=row[3]).id)
        db.session.add(rocket_series)

    db.session.commit()


def insert_launch_complex(data):
    for row in data:
        launch_complex = LaunchComplex(name_en=row[1], name_zh=row[2],
                                       spaceport_id=Spaceport.query.filter_by(name_zh=row[3]).id)
        db.session.add(launch_complex)

    db.session.commit()


def insert_rocket(data):
    for row in data:
        rocket = Rocket(name_en=row[1], name_zh=row[2],
                        series_id=RocketSeries.query.fileter_by(name_zh=row[3]).id)
        db.session.add(rocket)

    db.session.commit()


def insert_record(data):
    for row in data:
        record = Record(rocket_id=Rocket.query.filter_by(name_zh=row[1]).id,
                        complex_id=LaunchComplex.query.filter_by(name_zh=row[2]).id,
                        launch_date=Datetime(row[3]),
                        payload=row[4],
                        result=row[5]
                        )
        db.session.add(record)

    db.session.commit()

