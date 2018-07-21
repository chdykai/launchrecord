from launchrecord import app, db
from launchrecord.models import RocketSeries, Rocket, Spaceport, Record, Country
from datetime import datetime
import csv
import argparse


def load_data(csv_file):
    with open(csv_file, encoding='utf-8') as f:
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


def insert_rocket(data):
    for row in data:
        rocket = Rocket(name_en=row[1], name_zh=row[2],
                        series_id=RocketSeries.query.fileter_by(name_zh=row[3]).id)
        db.session.add(rocket)
    db.session.commit()


def insert_record(data):
    for row in data:
        dt = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
        record = Record(rocket_id=Rocket.query.filter_by(name_zh=row[1]).id,
                        spaceport_id=Spaceport.query.filter_by(name_zh=row[2]).id,
                        launch_date=dt,
                        payload=row[4],
                        result=row[5])
        db.session.add(record)
    db.session.commit()


def cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='the directory of data file')
    parser.add_argument('-c', '--country', action='store_true', help='insert country')
    parser.add_argument('-R', '--rocketseries', action='store_true', help='insert rocketseries')
    parser.add_argument('-p', '--spaceport', action='store_true', help='insert spaceport')
    parser.add_argument('-r', '--rocket', action='store_true', help='insert rocket')
    parser.add_argument('-o', '--record', action='store_true', help='insert record')

    args = parser.parse_args()

    data = load_data(args.filename)

    if args.country:
        insert_country(data)
        print('country list insertion complete!')
    elif args.rocketseries:
        insert_rocket_series(data)
        print('rocket list insertion complete!')
    elif args.spaceport:
        insert_spaceport(data)
        print('spaceport list insertion complete!')
    elif args.rocket:
        insert_rocket(data)
        print('rocket list insertion complete!')
    elif args.record:
        insert_record(data)
        print('record list insertion complete!')
    else:
        print('use -h to see help')


if __name__ == '__main__':
    cmd()

