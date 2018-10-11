from flask import Flask
from flask_restful import Api
from .resources import Todo, TodoList

# initialize api
app = Flask(__name__)
api = Api(app)

# add api resources
api.add_resource(TodoList, "/todos")
api.add_resource(Todo, "/todos/<int:todo_id>")

if __name__ == "__main__":
    app.run(debug=True)
