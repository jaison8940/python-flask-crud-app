from db import db
from models import users
import json
import dbcreate

def get(id=None):
    try:       
        if id:
            user_results= users.query.filter_by(id = id)
        else:
            user_results = users.query.all()
        res = {}
        for user in user_results:
            temp = {}
            temp['name'],temp['email'],temp['contactno'] = user.name,user.email,user.contactno
            res[user.id] = temp
            
        return res
    except Exception as error:
        return str(error)
        

def post(data):
    try:
        data = json.loads(data)
        if isinstance(data,dict):
            data = [data]
        for user in data:
            db.session.add(users(name=user['name'],email=user['email'],contactno=user['contactno']))
        db.session.commit()
        return "Inserted Successfully"
    except Exception as error:
        return str(error)

def put(data):
    try:
        data = json.loads(data)
        if isinstance(data,dict):
            data = [data]
        for user in data:
            updateUser = users.query.get(user['id'])
            print(updateUser.name)
            updateUser.name = user['name']
            updateUser.email = user['email']
            updateUser.contactno = user['contactno']
            print(updateUser.name)
        db.session.commit()
        return "Updated Successfully"
    except Exception as error:
        return str(error)
        
def delete(id):
    try:
        db.session.delete(users.query.get(id))
        db.session.commit()
        return "Deleted Successfully"
    except Exception as error:
        return str(error)
    


    