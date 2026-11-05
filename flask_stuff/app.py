import os
from flask import Flask, request, render_template, jsonify
from datetime import datetime
import pymongo
from dotenv import load_dotenv
import certifi

load_dotenv()  # Load environment variables from .env file

MONGO_URL = os.getenv("MONGO_URL")
print("Mongo URL exists:", MONGO_URL is not None)
print("Mongo URL starts correctly:", MONGO_URL.startswith("mongodb") if MONGO_URL else False)
#client = pymongo.MongoClient(MONGO_URL)
client = pymongo.MongoClient(
    MONGO_URL,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)
db = client['test_database']  # Use your database name here
try:
    client.admin.command("ping")
    print("Connected successfully")

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

collection = db["test_collection"]
app = Flask(__name__)

@app.route('/')
def home():
    day_of_week = datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)
    #return 'Hi, Welcome to my Flask app!'

@app.route('/submit', methods=['POST'])
def submit():
    #name = request.form.get('username')
    return 'Form submitted successfully!'

@app.route('/record')
def record():
    form_data = dict(request.form)
    result = collection.insert_one(form_data)
    data = list(collection.find())
    for record in data:
        #record['_id'] = str(record['_id'])  # Convert ObjectId to string for JSON serialization
        del record['_id']  # Remove the '_id' field from the record
    return jsonify(data)
@app.route('/time')
def time():
    current_time = datetime.now().strftime('%H:%M:%S')
    return f'Current time: {current_time}'

@app.route('/api/<name>')
def name(name):
    return f'Hello {name}!'

@app.route('/add/<int:a>/<int:b>')
def add(a,b):

    answer = a+b
    result = {
        'ans': answer
    }

    return result

if __name__  == '__main__':
    app.run(debug=True)