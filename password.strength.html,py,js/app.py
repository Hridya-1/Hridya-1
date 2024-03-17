from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['GET'])
def generate_password():
    password = request.args.get('password')

    nonAlphaChars = []
    numericChars = []
    chars = []

    for char in password:
        if not char.isalnum():
            nonAlphaChars.append(char)
        if char.isnumeric():
            numericChars.append(char)
        if char.isalnum() and not char.isnumeric():
            chars.append(char)

    if len(nonAlphaChars) > 0 and len(numericChars) > 0 and len(chars) > 0:
        strength = 'Strong password'
    elif len(nonAlphaChars) == 0 and len(numericChars) > 0 and len(chars) > 0:
        strength = 'Good password'
    elif len(nonAlphaChars) == 0 and len(numericChars) == 0 and len(chars) > 0:
        strength = 'Weak password'
    elif len(nonAlphaChars) == 0 and len(numericChars) == 0 and len(chars) == 0:
        strength = 'Error!!! Enter the password'

    return jsonify({'strength': strength})

if __name__ == '__main__':
    app.run(debug=True)
