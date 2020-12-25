import flask

app = flask.Flask(__name__)
api = Api(app)

stores: str = 'My first store'


# @app.route('/store', methods=['DELETE'])
def delete_store():
    return "In delete store"


api.add_resource(Student, '/stores1/<string_name>')

app.run(port=5000)
