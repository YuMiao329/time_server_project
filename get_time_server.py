from flask import Flask, request
from datetime import datetime, date
import jsonify
import sys


# from client import out_data


def get_time():
    x = datetime.now()
    y = datetime.strftime(x, "%m-%d-%y %H:%M:%S")
    print(y)
    return y

def get_time_sec():
    x = datetime.strftime(datetime.now(),  "%H:%M:%S")
    hours = int(x.split(":")[0])
    mins = int(x.split(":")[1])
    secs = int(x.split(":")[2])
    print(hours, mins, secs)
    return hours, mins, secs

def get_date():
    x = datetime.now().date()
    y = datetime.strftime(x, "%m-%d-%y")
    print(y)
    return y


def get_age(out_data):
    time_string = out_data["date"].split("/")
    d1 = date(int(time_string[2]), int(time_string[0]), int(time_string[1]))
    d2 = datetime.now().date()
    return str(abs((d1 - d2).days / 365))


def data_Driver():
    data_value = data_input()
    data_character = get_age(data_value)


def data_input():
    data_value = int(input(("Enter data Value: ")))
    return data_value


def get_age(out_data):
    time_string = out_data.split("/")
    d1 = date(int(time_string[2]), int(time_string[0]), int(time_string[1]))
    print(d1)
    d2 = datetime.now().date()
    print(d2)
    return str(abs((d1 - d2).days / 365))


def interface():
    data_Driver()




if __name__ == '__main__':
    get_time()
    get_date()
    interface()
