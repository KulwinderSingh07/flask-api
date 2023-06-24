import mysql.connector
import json
class user_model():
    def __init__(self):
        try:
            #connection stablishment code
            self.con=mysql.connector.connect(host="localhost",user="Kulwinder",password="Laddi@2002",database="flask-api")
            self.con.autocommit=True
            self.curr=self.con.cursor(dictionary=True)
            print("Connection Succesfull")
        except:
            print("Some error occures to connect to mysql")
    def user_getall_model(self):
        self.curr.execute("select * from User")
        result=self.curr.fetchall()
        print(result)
        if len(result)>0:
            return json.dumps(result)
        else:
            return "Data not found"
        
    def user_addone_model(self,data):
        # print(data["email"])
        # self.curr.execute("select * from User")
        self.curr.execute(f"insert into User(name,email,phone,password) values('{data['name']}','{data['email']}','{data['phone']}','{data['password']}')")
        return "user created succesfully"

    def user_updateone_model(self,data):
        self.curr.execute(f"update User set name='{data['name']}', email='{data['email']}', phone='{data['phone']}', password='{data['password']}', role='{data['role']}' where id={data['id']}")
        print(self.curr.rowcount)
        if self.curr.rowcount>0:
            return "user updated succesfully"
        else:
            return "User not updated"