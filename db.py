#db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
DB_HOST = os.environ.get('DB_HOST') or '34.125.244.185'
DB_PORT = os.environ.get('DB_PORT') or 3306

#setting up connection to Cloud SQL
def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    
    
    con = pymysql.connect(user=db_user, password=db_password, db=db_name, host=DB_HOST, port=DB_PORT,
                            cursorclass=pymysql.cursors.DictCursor
                             )
    print("hello")
    return con
   
    
    
    
#get_users function to retrieve all user info
def get_users():
    conn = open_connection()
    got_data = ''
    if conn != None:
        with conn.cursor() as cursor:
            result = cursor.execute('SELECT * FROM user_info;')
            user_data = cursor.fetchall()
            if result > 0:
                got_data = jsonify(user_data)
            else:
                got_data = 'No data in DB'
        conn.close()
    return got_data

#add_users function to add new users
def add_users(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("""INSERT INTO user_info 
        (username,em_name1,em_phone1,em_name2,em_phone2,notify_911,notify_nearby,help_nearby) 
        VALUES(%s, %s, %s, %s, %s, %r, %r, %r) 
        RETURNING username, em_name1, em_phone1, em_name2, em_phone2, notify_911, notify_nearby, help_nearby
        """ , (user["username"], user["em_name1"], user["em_phone1"],user["em_name2"],user["em_phone2"],user["notify_911"],user["notify_nearby"],user["help_nearby"]))
    return "DONE"
    conn.commit()
    conn.close()

#update_users function to update user_info table on Cloud SQL, when the user changes their settings or emergency contacts
def update_users(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("""UPDATE user_info SET em_name1=%s,em_phone1=%s,em_name2=%s,em_phone2=%s,notify_911=%r,notify_nearby=%r,help_nearby=%r 
        WHERE username = %s;
        """, (user["em_name1"], user["em_phone1"],user["em_name2"],user["em_phone2"],user["notify_911"],user["notify_nearby"],user["help_nearby"], user["username"]) )
        conn.commit()
    conn.close()


#get_user by username to get the user info by username
def get_user_by_username(username):
    conn = open_connection()
    with conn.cursor() as cursor:
    

        cursor.execute("""
            SELECT username,em_name1,em_phone1,em_name2,em_phone2,notify_911,notify_nearby,help_nearby 
            FROM user_info
            WHERE username = %s
        """, (username,))

        result = cursor.fetchone()

    # Create user object
    user = {
        'username': result[0],
        'em_name1': result[1],
        'em_phone1': result[2],
        'em_name2': result[3],
        'em_phone2': result[4],
        'notify_911': result[5],
        'notify_nearby': result[6],
        'help_nearby' : result[7]
    }

    conn.commit()
    conn.close()

    return user

#get_grid_dat functions to get chuncks of the grid data to find which grid the user is currently in 
def get_grid_data1():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id<31;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data

def get_grid_data2():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id>30 and rect_id<61;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data

def get_grid_data3():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id>60 and rect_id<91;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data

def get_grid_data4():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id>90 and rect_id<121;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data

def get_grid_data5():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id>120 and rect_id<151;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data

def get_grid_data6():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id>150 and rect_id<181;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data

def get_grid_data7():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id>180 and rect_id<211;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data

def get_grid_data8():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id>210 and rect_id<241;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data

def get_grid_data9():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM gridmap where rect_id>240;')
        grid_data = cursor.fetchall()
        if result > 0:
            got_data = jsonify(grid_data)
        else:
            got_data = 'No data in DB'
    conn.close()
    return got_data
