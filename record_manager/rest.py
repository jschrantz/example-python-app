import argparse
import json

from flask import abort, Flask, request

from . import parser, sorter

def create_app():

    app = Flask(__name__)
    app.config['db'] = []

    @app.route('/records', methods=['POST'])
    def record_post():
        body = request.get_data(as_text=True)
        if not body:
            abort(400)
            return

        try:
            record_strings = json.loads(body)
            if not isinstance(record_strings, list):
                abort(400)
                return
        except ValueError:
            record_strings = [body]

        app.config['db'].extend(parser.parse_records(record_strings))

        return 'OK'

    @app.route('/records/gender', methods=['GET'])
    def get_records_by_gender():
        records = sorter.sort_records_by_gender(app.config['db'])

        return json.dumps([r.to_dict() for r in records])

    @app.route('/records/birthdate', methods=['GET'])
    def get_records_by_dob():
        records = sorter.sort_records_by_dob(app.config['db'])

        return json.dumps([r.to_dict() for r in records])

    @app.route('/records/name', methods=['GET'])
    def get_records_by_name():
        records = sorter.sort_records_by_name(app.config['db'])

        return json.dumps([r.to_dict() for r in records])

    return app

def main():
    argparser = argparse.ArgumentParser(description="Process data records")
    argparser.add_argument('--port', default=5000, type=int)

    args = argparser.parse_args()

    app = create_app()
    app.run('0.0.0.0', args.port)