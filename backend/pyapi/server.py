import json
from flask import Flask

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
        ,"editedIndex": -1
        ,"editedItem": {"id": None,  "name": None, "email":None, "status":{"value":'valid', "text":'有効'}}
        ,"defaultItem": {"id": None,  "name": None, "email":None, "status":{"value":'valid', "text":'有効'}}
}

app = Flask(__name__) 

@app.route("/") 
def home():
    return "Python API!"


@app.route("/users") 
def users():
    resultSet = json.dumps(UsersList["items"])
    # resultSet = jsonify(UsersList["items"])
    return resultSet

# https://qiita.com/tchnkmr/items/26d271886b46c4e52dc1
@app.route("/users/<int:user_id>", methods=['GET']) 
def get_user(user_id=None):
    result = None
    # DBからフィルタリングして取得
    # user = User.query.filter_by(id=user_id).first()
    for user in UsersList["items"]:
        if user["id"] == user_id :
            result = user
            break

    return json.dumps(result), 418

if __name__ == "__main__":
    app.run()

# python3 server.py

# http://127.0.0.1:5000/
# http://127.0.0.1:5000/users
