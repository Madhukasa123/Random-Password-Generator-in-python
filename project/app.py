import random
import string
from flask import Flask, render_template

app = Flask(__name__)

# Password generation function
def generate_password(length=12):
    special_characters = '!@#$%^&*()_+[]{}|;:,.<>?'
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits

    password = ''.join([
        random.choice(special_characters),
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(numbers),
    ])

    remaining_length = length - 4
    all_characters = special_characters + lowercase_letters + uppercase_letters + numbers
    for _ in range(remaining_length):
        password += random.choice(all_characters)

    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password')
def generate_and_return_password():
    password = generate_password()
    return password

if __name__ == '__main__':
    app.run(debug=True)
