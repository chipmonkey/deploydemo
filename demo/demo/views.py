from demo import app


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/user/<userid>')
def user_userid(userid):
    return "Get User {userid} from db"
