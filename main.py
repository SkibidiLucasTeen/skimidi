from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome to Flask!</h1>
        <form action="/greet" method="POST">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Greet Me</button>
        </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Guest')
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
