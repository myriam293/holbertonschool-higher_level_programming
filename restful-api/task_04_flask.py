
#!/usr/bin/python3
"""Module for creating a simple Flask RESTful API"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Root endpoint returning a welcome message"""
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    """Endpoint to return a list of all usernames"""
    return jsonify(list(users))


@app.route('/add_user', methods=['POST'])
def add_user():
    """POST endpoint to add a new user to the in-memory store"""
    data = request.json
    if not data or 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400

    user = {
        'username': data.get('username'),
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    users[user['username']] = user
    return jsonify({'message': 'User added', 'user': user}), 201


@app.route('/status')
def status():
    """Simple health check endpoint"""
    return 'OK'


@app.route('/users/<username>')
def get_user(username):
    """Returns user info for a given username, or error if not found"""
    if username not in users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users[username])


if __name__ == "__main__":
    """Run the Flask development server"""
    app.run()
