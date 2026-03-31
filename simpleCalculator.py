from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Simple Calculator</h2>
    <form action="/calculate">
        <input name="a" placeholder="Enter first number">
        <input name="b" placeholder="Enter second number">
        <select name="op">
            <option value="add">+</option>
            <option value="sub">-</option>
            <option value="mul">*</option>
            <option value="div">/</option>
        </select>
        <button type="submit">Calculate</button>
    </form>
    '''

@app.route('/calculate')
def calculate():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    op = request.args.get('op')

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    else:
        result = a / b

    return f"<h3>Result: {result}</h3><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run()
