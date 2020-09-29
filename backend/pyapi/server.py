import json
from flask import Flask
from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS

UsersList = {
        "search": '',
        "selected": [],
        "headers": [
          { "text": '名前', "value": 'name', "sortable": True, "class": "primary white--text title" },
          { "text": 'email', "value": 'email', "sortable": True, "class": "primary white--text title" },
          { "text": '状態', "value": 'status.text', "sortable": True, "class": "primary white--text title" },
          { "text": '', "value": 'actions', "sortable": False, "class": "primary white--text title" }
        ],
        "items": [
          {"id": 0, "name": 'Nam', "email":"nam@vue.nam", "status":{"value":'valid', "text":'有効'}},
          {"id": 1, "name": 'Nguyen', "email":"nguyen@vue.nam", "status":{"value":'invalid', "text":'無効'}},
          {"id": 2, "name": 'Tester 1', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 3, "name": 'Tester 2 - deleted', "email":None, "status":{"value":'deleted', "text":'削除'}},
          {"id": 4, "name": 'Tester 3', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 5, "name": 'Tester 4', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 6, "name": 'Tester 5', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 7, "name": 'Tester 6', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 8, "name": 'Tester 7', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 9, "name": 'Tester 8', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 10, "name": 'Tester 9 - deleted', "email":None, "status":{"value":'deleted', "text":'削除'}},
          {"id": 11, "name": 'Tester 10', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 12, "name": 'Tester 11', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 13, "name": 'Tester 12', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 14, "name": 'Tester 13', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 15, "name": 'Tester 14', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 16, "name": 'Tester 15', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 17, "name": 'Tester 16', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 18, "name": 'Tester 17', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 19, "name": 'Tester 18', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 20, "name": 'Tester 19', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 21, "name": 'Tester 20', "email":None, "status":{"value":'valid', "text":'有効'}},
          {"id": 22, "name": 'Tester 21', "email":None, "status":{"value":'valid', "text":'有効'}},
        ]
        ,"nextIndex": 23
        ,"editedIndex": -1
        ,"editedItem": {"id": None,  "name": None, "email":None, "status":{"value":'valid', "text":'有効'}}
        ,"defaultItem": {"id": None,  "name": None, "email":None, "status":{"value":'valid', "text":'有効'}}
}

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Blueprint('api', __name__, url_prefix='/api')

# =================================================================
# FrontEnd
# =================================================================

@app.route("/")
def home():
    return "Python API!"

@app.route('/users', methods=['GET'])
def users():
    resultSet = jsonify(UsersList["items"])
    return resultSet

def get_item(user_id=None):
    result = None
    # DBからフィルタリングして取得
    # user = User.query.filter_by(id=user_id).first()
    for user in UsersList["items"]:
        if user["id"] == user_id :
            result = user
            break

    return result

# @app.route("/users/<int:user_id>", methods=['GET']) 
# def get_user(user_id=None):
#     result = None

#     result = get_item(user_id)

#     return jsonify(result), 200

# =================================================================
# API
# =================================================================

# =================================================================
# https://qiita.com/tchnkmr/items/26d271886b46c4e52dc1
# =================================================================
@api.route('/users', methods=['GET'])
def users():
    resultSet = jsonify(UsersList["items"])
    return resultSet

@api.route("/users/<int:user_id>", methods=['GET']) 
def get_user(user_id=None):
    result = None

    result = get_item(user_id)

    return jsonify(result)

@api.route("/users/create", methods=['POST']) # CREATE
def create_user():
    result = None
    user = request.json

    # print(user)

    user["id"] = UsersList["nextIndex"]
    UsersList["items"].append(user)

    UsersList["nextIndex"] += 1

    # print(UsersList["items"])

    return jsonify(user)

@api.route("/users/<int:user_id>", methods=['PUT']) # UPDATE 
def update_user(user_id=None):
    result = None
    editedUser = request.json

    items_length = len(UsersList["items"])
    items_range = range(items_length)
    for index in items_range:
        if UsersList["items"][index]["id"] == user_id :
            UsersList["items"][index] = editedUser
            result = editedUser
            break

    return jsonify(result)

@api.route("/users/<int:user_id>", methods=['DELETE']) 
def delete_user(user_id=None):
    result = None

    user = get_item(user_id)
    result = user
    UsersList["items"].remove(user)

    return jsonify(result), 200

# =================================================================
# MAIN PROCESS
# =================================================================

@api.errorhandler(400)
@api.errorhandler(404)
def error_handler(error):
    # error.code: HTTPステータスコード
    # error.description: abortで設定したdict型
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code

app.register_blueprint(api)

# app.register_blueprint(
#     api, url_prefix="/route2")

# for rule in app.url_map.iter_rules():
#     print(rule)

# =================================================================
# URLs
# =================================================================

print("http://127.0.0.1:5000/")
print("http://127.0.0.1:5000/users")
# print("http://127.0.0.1:5000/users/1")
print("http://127.0.0.1:5000/api/users")
print("http://127.0.0.1:5000/api/users/1")


# =================================================================
# MAIN RUN
# =================================================================

if __name__ == "__main__":
    app.run()


# python3 server.py

# http://127.0.0.1:5000/
# http://127.0.0.1:5000/users
# http://127.0.0.1:5000/users/1
# http://127.0.0.1:5000/api/users
# http://127.0.0.1:5000/api/users/1
