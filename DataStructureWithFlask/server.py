from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from DataStructureWithFlask.linkedlist import LinkedList
from DataStructureWithFlask.hash_table import HashTable

# app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


@event.listens_for(Engine, "connect")
# configure sqlite3 to enforce foreign key constraints
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datetime.now()


class User(db.Model):
    # models: creating DDL for User table
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")


class BlogPost(db.Model):
    # models: creating DDL for BlogPost table
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# creating routes
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data['email'],
        address=data["address"],
        phone=data["phone"]
    )

    # inserting new user in the db
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "user Created"}), 200


@app.route('/user/descending_id', methods=['GET'])
def get_user_descending():
    users = User.query.all()
    user_ll = LinkedList()
    print(users)
    for user in users:
        user_ll.insert_beginning(
            {
                "id": user.id,
                "name" : user.name,
                "email" : user.email,
                "address" : user.address,
                "phone" : user.phone
        })

    return jsonify(user_ll.to_list()), 200


@app.route('/user/ascending_id', methods=['GET'])
def get_user_ascending():
    users = User.query.all()
    user_ll = LinkedList()

    for user in users:
        user_ll.insert_at_end(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone
            })

    return jsonify(user_ll.to_list()), 200


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user_id = int(user_id)
    users = User.query.all()

    user_ll = LinkedList()

    for user in users:
        user_ll.insert_beginning({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone
        })

    required_user = user_ll.get_user_by_id(user_id)
    return jsonify(required_user), 200


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({}), 200


@app.route('/blog_post/<user_id>', methods=['POST'])
def create_blog_post(user_id):
    data = request.get_json()

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": "User does not exist"}), 400

    ht = HashTable(10)
    ht.add_key_value("title", data["title"])
    ht.add_key_value("body", data["body"])
    ht.add_key_value("date", now)
    ht.add_key_value("user_id", user_id)

    new_blog_post = BlogPost(
        title=ht.get_value("title"),
        body=ht.get_value("body"),
        date=ht.get_value("date"),
        user_id=ht.get_value("user_id"),
    )
    db.session.add(new_blog_post)
    db.session.commit()
    return jsonify({"message": "new blog post created"}), 200


@app.route('/user/<user_id>', methods=['GET'])
def get_all_blog_post(user_id):
    pass


@app.route('/blog_post/<blog_post_id>', methods=['GET'])
def get_one_blog_post(blog_post_id):
    pass


@app.route('/blog_post/<blog_post_id>', methods=['DELETE'])
def delete_blog_post(blog_post_id):
    pass


if __name__ == "__main__":
    app.run(debug=True)
