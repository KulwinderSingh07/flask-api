from app import app
from model.user_model import user_model
from flask import request
obj=user_model()
@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone",methods=["POST"])
def user_addone_controller():
    # print(request.form)
    return obj.user_addone_model(request.form)

@app.route("/user/updateone",methods=["PUT"])
def user_update_controller():
    # print(request.form)
    return obj.user_updateone_model(request.form)
