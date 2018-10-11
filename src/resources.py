from flask_restful import Resource, abort, reqparse

SAMPLE_TODOS = {
    0: {"task": "build an API"},
    1: {"task": "?????"},
    2: {"task": "profit!"},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in SAMPLE_TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


todo_parser = reqparse.RequestParser()
todo_parser.add_argument("task", required=True)


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return SAMPLE_TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del SAMPLE_TODOS[todo_id]
        return "", 204

    def put(self, todo_id):
        args = todo_parser.parse_args()
        task = {"task": args["task"]}
        SAMPLE_TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):

    last_id = 2

    def get(self):
        return SAMPLE_TODOS

    def post(self):
        args = todo_parser.parse_args()
        TodoList.last_id += 1
        todo_id = TodoList.last_id
        SAMPLE_TODOS[todo_id] = {"task": args["task"]}
        return SAMPLE_TODOS[todo_id], 201
