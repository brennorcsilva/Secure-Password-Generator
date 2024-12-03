from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from password_generator import character_pool, generate_password

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-password', methods = ['POST'])
def generate_password_api():
    data = request.get_json()

    password_size = data.get('password_size', 0)
    include_uppercase = data.get('include_uppercase', False)
    include_numbers = data.get('include_numbers', False)
    include_special = data.get('include_special', False)

    if password_size <= 0:
        return jsonify({'error': 'Password size must be greater than 0!'}), 400
    
    chars = character_pool(include_uppercase, include_numbers, include_special)

    if not chars:
        return jsonify({'error': 'No characther types selected!'}), 400
    
    password = generate_password(password_size, chars)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)