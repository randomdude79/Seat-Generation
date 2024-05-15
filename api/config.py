import os
from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_seats_dm', methods=['POST'])
def generate_seats_dm():
    os.system('python api/DeMaria.py')
    return send_file('templates/seatsDM.md')

if __name__ == '__main__':
    app.run(debug=True)
