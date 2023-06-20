from flask import Flask, render_template, request
from solution import Solution

app = Flask(__name__)

# define route for home page
@app.route('/')
def index():
    return render_template('index.html')

# define route for parsing the form data and displaying the result
@app.route('/evaluate', methods=['POST'])
def evaluate():
    # get the input from the form
    raw_tokens = request.form['tokens']
    tokens = [t.strip() for t in raw_tokens.split(',') if t.strip()]

    # validate the input
    valid_operators = ['+', '-', '*', '/']
    errors = []
    for t in tokens:
        if t in valid_operators:
            continue
        try:
            int(t)
        except ValueError:
            errors.append(f'Invalid token: {t}')
    
    # evaluate the expression or show error message
    if errors:
        return render_template('result.html', error='<br>'.join(errors))
    else:
        solution = Solution()
        result = solution.evalRPN(tokens)
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
