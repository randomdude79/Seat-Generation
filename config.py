from flask import Flask, render_template, send_file
from serverless_wsgi import handle_request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_seats')
def generate_seats():
    user = input('What classroom are you?\n')
    if user == '1':
        os.system('python DeMaria.py')
        return send_file('seatsDM.md')
    elif user == '2':
        os.system('python MarquesLeach.py')
        return send_file('seatsML.md')
    else:
        return 'Not all teachers are supported yet.'

def handler(event, context):
    return handle_request(app, event, context)
