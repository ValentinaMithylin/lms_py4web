from py4web import action

@action('home/dashboard')
def dashboard():
    return "You have been redirected to a new page!"