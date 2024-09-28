from py4web import action

from ..models.connect_db import db

@action('home/dashboard')
@action.uses('dashboard.html')
def dashboard():
    return locals()