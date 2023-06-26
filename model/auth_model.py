import mysql.connector
import json
from flask import make_response,request
from datetime import datetime,timedelta
from functools import wraps
from config.db_config import dbconfig
import os
import jwt
import re
class auth_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host=dbconfig["host"],user=dbconfig["user"],password=dbconfig["password"],database=dbconfig["database"])
            self.con.autocommit=True
            self.curr=self.con.cursor(dictionary=True)
            print("Connection Succesfull")
        except:
            print("Some error occures to connect to mysql")
    
    def token_auth(self,endpoint=""):
        def inner1(func):
            @wraps(func)
            def inner2(*args):
                endpoint=request.url_rule
                print(endpoint)
                authorization=request.headers.get("Authorization")
                if re.match("Bearer *([^ ]+) *$", authorization,flags=0):
                    token=authorization.split(" ")[1]
                    try:
                        jwtdecoded=jwt.decode(token,"kulwinder",algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR":"Token expired"},401)
                    role_id=jwtdecoded['payload'][0]['role_id']
                    self.curr.execute(f"select roles from accessibility_view where endpoint='{endpoint}'")
                    result=self.curr.fetchall()
                    if len(result)>0:
                        allowed_roles=json.loads(result[0]['roles'])
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                            return make_response({"ERROR":"INVALID_ROLE"},404)
                    else:
                        return make_response({"Error":"Uknown endpoint"},404)
                else:
                    return make_response({"ERROR":"INVALID_TOKEN"},401)
            return inner2
        return inner1