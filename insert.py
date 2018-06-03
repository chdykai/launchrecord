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
        spaceport = Spaceport()

