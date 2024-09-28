from py4web import action

from ..models.connect_db import db

@action('home/dashboard')
@action.uses('dashboard.html')
def dashboard():
    user_name = ''
    get_user_name_sql = f"SELECT name FROM users WHERE user_id = '007' LIMIT 0, 1;"
    get_user_name = db.executesql(get_user_name_sql, as_dict = True)

    if get_user_name:
        user_name = str(get_user_name[0]['name']).split(' ')[0]

    return locals()