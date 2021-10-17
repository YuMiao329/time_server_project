from flask import Flask, request
from datetime import datetime, date
import jsonify
import json
#from get_time_server import get_time, get_date, get_age
import get_time_server


app = Flask(__name__)



@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def server_status():
    return "Server is on"


@app.route("/time", methods=["GET"])
def current_time():
    print("Current time is: {}".format(get_time_server.get_time()))
    answer = get_time_server.get_time()
    return answer


@app.route("/date", methods=["GET"])
def current_date():
    print("Current date is: {}".format(get_time_server.get_time()))
    answer = get_time_server.get_date()
    return answer


@app.route("/age", methods=["POST"])
def find_age():
    in_data = request.get_json()
    data_value = in_data["date"]
    answer = (get_time_server.get_age(data_value))
    return (answer)


@app.route("/until_next_meal/<meal>", methods=["GET"])
def find_meal(meal):

    hours, mins, secs = get_time_server.get_time_sec()
    if format(meal) == "dinner":
        if hours >= 18:
            answer = 24 - hours + 18
        else:
            answer = 18 - hours

    if format(meal) == "breakfast":
        if hours >= 8:
            answer = 24 - hours + 8
        else:
            answer = 8 - hours

    if format(meal) == "lunch":
        if hours >= 12:
            answer = 24 - hours + 12
        else:
            answer = 12 - hours

    return str(answer)

if __name__ == '__main__':
    app.run()
