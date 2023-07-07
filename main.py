from flask import Flask, jsonify, make_response
import json
from faker import Faker
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_ai():
 return '<h1>Hello This is an AI class</h2>'

employees = []
for i in range(0,20):
  fake = Faker()
  employee = {}
  employee['first_name'] = fake.first_name()
  employee['last_name'] = fake.last_name()
  employee['job'] = fake.job()
  employees.append(employee)

@app.route('/user')
def gen_user():
 return make_response(jsonify(employees), 200)
if __name__ == "__main__":
 app.run(host = '0.0.0.0')
