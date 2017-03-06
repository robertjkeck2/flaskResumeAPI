from models import app
import views


@app.route('/')
def index():
    return "Welcome to the Resume API.\n\nPlease use API requests to access data."

