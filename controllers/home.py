from py4web import action

@action('home/dashboard')
@action.uses('dashboard.html')
def dashboard():
    # return "You have been redirected to a new page!"
    return locals()