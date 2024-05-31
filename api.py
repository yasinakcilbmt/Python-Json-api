from flask import Flask, jsonify
import requests

app = Flask(__name__)

url = 'https://jsonplaceholder.typicode.com/todos'

@app.route('/api/todos', methods=['GET'])
def get_todos():
    try:
        response = requests.get(url)
        response.raise_for_status()
        todos = response.json()
        
        print(todos)
        
        return jsonify(todos)
    except requests.exceptions.RequestException as e:
        error_message = str(e)
        
        print(f"Error: {error_message}")
        
        return jsonify(error=error_message), 500

if __name__ == '__main__':
    app.run(debug=True)
