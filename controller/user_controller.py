from app import app
from model.user_model import user_model
from flask import request,send_file
from model.auth_model import auth_model
from datetime import datetime
obj=user_model()
auth=auth_model()
@app.route("/user/getall")
@auth.token_auth("/user/getall")  #jwt decorator
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

@app.route("/user/delete/<id>", methods=["DELETE"])
def delete_user(id):
    return obj.delete_user_model(id)

@app.route("/user/patch/<id>", methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form,id)

@app.route("/user/getall/limit/<limit>/page/<page>" ,methods=["GET"])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit,page)

@app.route("/user/<uid>/upload/avatar",methods=["PUT"])
def user_uploadAvtar_controller(uid):
    file=request.files['avatar']
    uniqueFilename=str(datetime.now().timestamp()).replace(".","")
    print(file)
    print(uid)
    splitFilename=file.filename.split(".")
    ext=splitFilename[len(splitFilename)-1]
    final_file_path=f"uploads/{uniqueFilename}.{ext}"
    file.save(final_file_path)
    return obj.user_upload_avatar_model(uid,final_file_path)

@app.route("/upload/<filename>")
def user_getavatar_controller(filename):
    return send_file(f"uploads/{filename}")

@app.route("/user/login",methods=["POST"])
def user_login_controller():
    return obj.user_login_model(request.form)

