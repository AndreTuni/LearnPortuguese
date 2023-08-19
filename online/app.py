import csv
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Rest of your code

@app.route('/', methods=['GET', 'POST'])
def quiz_app():
    if request.method == 'POST':
        category = request.form.get('category')
        mode = request.form.get('mode')

        # Add your quiz logic here based on selected category and mode

        return render_template('quiz.html', result=result)  # Replace with your template and result data
    return render_template('index.html')  # Replace with your template

if __name__ == '__main__':
    app.run(debug=True)
