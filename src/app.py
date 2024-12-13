from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
  {
    "label": "My first task",
    "done": False
  }
]


@app.route('/todos', methods=['GET'])
def get_All_todo():
  return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)

    if 0 <= position < len(todos):
       todos.pop(position)
       return jsonify(todos)
    else:
       return jsonify({}, 400)

# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)