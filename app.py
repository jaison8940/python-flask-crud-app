from flaskapp import app,request
from service import get,post,put,delete

@app.route('/user',methods=['GET'])
@app.route('/user/<id>',methods=['GET'])
def read_users(id=None):
    return get(id)

@app.route('/user',methods=['POST'])
def insert_users():
    return post(request.data)

@app.route('/user',methods=['PUT'])
def update_users():
    return put(request.data)

@app.route('/user/<id>',methods=['DELETE'])
def delete_users(id):
    return delete(id)
    
if __name__ == '__main__':
    app.run(debug = True)