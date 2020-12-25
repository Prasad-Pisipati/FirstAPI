#   def post(self, name):
#       #data = request.get_json(force=True,)
#       data = request.get_json(silent=True)
#      item = {'name': name, 'price': 12.00}
#      items.append(item)
#       return item, 201

#import flask
#import flask
from flask_restful import Resource, Api
from flask import Flask,request

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return "item found", 200

        return "item not found",202

    def post(self,name):
        data = request.get_json()
#        print(data['price'])
        item = {'name': name,'price': 10.99}
        items.append(item)
        return data, 201

class Itemlist(Resource):
    def get(self):
        return {'items ': items},200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/itemlist')

app.run(port=5000, debug=True)
