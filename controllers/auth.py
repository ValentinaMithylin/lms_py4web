import json
from py4web import action, request, redirect, URL

from ..models.connect_db import db
# from ..controllers import home


@action('auth/login')
@action.uses('login.html')
def login():
    email = request.POST.get('user_email')
    password = request.POST.get('user_pass')

    check_user_sql = f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}' LIMIT 0, 1;"
    check_user = db.executesql(check_user_sql, as_dict = True)

    if len(check_user):
        redirect(URL('home','dashboard'))
    
    else:
        print("No user found")

    return dict()



@action('auth/register')
@action.uses('register.html')
def register():
    # email = request.POST.get('user_email')
    # password = request.POST.get('user_pass')

    # if str(email) != '' and str(password) != '': 
    #     check_user_sql = f"SELECT * FROM users WHERE email = '{email}' LIMIT 0, 1;"
    #     check_user = db.executesql(check_user_sql, as_dict = True)
    #     # return json.dumps(check_user)

    #     user_id = "007"
    #     name = "Valentina Mithylin"

    #     if not check_user:
    #         new_user_sql = f"INSERT INTO users (user_id, name, email, password) VALUES ('{user_id}','{name}','{email}','{password}');"
    #         db.executesql(new_user_sql, as_dict = True)
    # return 'registering'
    return dict()