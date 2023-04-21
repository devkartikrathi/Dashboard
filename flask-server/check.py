from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
import jwt
import datetime
from functools import wraps
from database import *


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjgyMDU4NDAxfQ.V6YQlftOt8S20Sivc4wLRpcT3voTw5I2CnbvlE55xXw"
data = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
print(data)