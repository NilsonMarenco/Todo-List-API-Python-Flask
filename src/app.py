from flask import Flask
from flask import Flask, jsonify
from flask import request




app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)

    # y luego puedes devolverlo al front-end en el cuerpo de la respuesta de la siguiente manera
    return json_text



todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
   
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop((position-1))
    response_body = todos
    return jsonify(response_body), 200


# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)