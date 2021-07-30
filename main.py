#main.py
from flask import Flask, jsonify, request
import db


app = Flask(__name__)

user_data=[ {
    'username': 'admin',
    'em_name1': 'name1',
    'em_phone1': '123',
    'em_name2': 'name2',
    'em_phone2': '456',
    'notify_911': True,
    'notify_nearby': True,
    'help_nearby' : True
}]

@app.route('/')
def home():
    return render_template("page.html", title="HOME PAGE")
    
    
#add_users
@app.route('/add_users', methods=['POST', 'GET'])
def add_users():
    user = request.get_json()
    message=db.add_users()
    return message
    #return request.is_json

#update_users
@app.route('/update_users', methods=['POST', 'GET'])
def update_users():
    user = request.get_json()
    db.update_users()

#get_user_by_username
@app.route('/get_user_by_username', methods=['GET','POST'])     
def get_user_by_username():
    
    username = request.args.get('username')
    
    user = db.get_user_by_username(username)

    return jsonify(user)

#get_users
@app.route('/get_users', methods=['GET','POST'])     
def get_users():
    users = db.get_users()
    return users

#getting grid data in individual parts
@app.route('/get_grid_data1', methods=['GET', 'POST'])     
def get_grid_data1():
    grids = db.get_grid_data1()
    return grids

@app.route('/get_grid_data2', methods=['GET', 'POST'])     
def get_grid_data2():
    grids = db.get_grid_data2()
    return grids

@app.route('/get_grid_data3', methods=['GET', 'POST'])     
def get_grid_data3():
    grids = db.get_grid_data3()
    return grids

@app.route('/get_grid_data4', methods=['GET', 'POST'])     
def get_grid_data4():
    grids = db.get_grid_data4()
    return grids

@app.route('/get_grid_data5', methods=['GET', 'POST'])     
def get_grid_data5():
    grids = db.get_grid_data5()
    return grids

@app.route('/get_grid_data6', methods=['GET', 'POST'])     
def get_grid_data6():
    grids = db.get_grid_data6()
    return grids

@app.route('/get_grid_data7', methods=['GET', 'POST'])     
def get_grid_data7():
    grids = db.get_grid_data7()
    return grids

@app.route('/get_grid_data8', methods=['GET', 'POST'])     
def get_grid_data8():
    grids = db.get_grid_data8()
    return grids

@app.route('/get_grid_data9', methods=['GET', 'POST'])     
def get_grid_data9():
    grids = db.get_grid_data9()
    return grids

#main
if __name__ == '__main__':
    app.run( port=3306, debug=True)
