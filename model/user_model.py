import mysql.connector
class user_model():
    def __init__(self):
        try:
            #connection stablishment code
            con=mysql.connector.connect(host="localhost",user="Kulwinder",password="Laddi@2002",database="flask-api")
            print("Connection Succesfull")
        except:
            print("Some error occures to connect to mysql")
    def user_getall_model(self):
        # connection establishment code
        # quey execution code
        return "this is user signup model"