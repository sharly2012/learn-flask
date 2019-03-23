from flask import Flask, request, make_response, redirect
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    # user_agent = request.headers.get("User-Agent")
    # return "<h1>Your browse is %s</h1>" % user_agent
    # response = make_response("<h1>This is a document carries a cookier !</h1>")
    # response.set_cookie("answer", "11")
    # return response
    return redirect("http://www.baidu.com")


# @app.route("/user/<name>")
# def user(name):
#     return "<h1>hello world, %s</h1>" % name


if __name__ == '__main__':
    manager.run()
