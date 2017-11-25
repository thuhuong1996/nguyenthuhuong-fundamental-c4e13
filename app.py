from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
 return render_template('home.html')
    # return("hello world")
# @app.route('/hello_me/a')
# def hello_me():
#      return "hello huong hii"
#
# @app.route('/<name>')
# def hello(name):
#      return "hello" + name
#
# @app.route('/<lastname>/<firstname>')
# def hi(lastname, firstname):
#     return "Hello " + lastname + " " + firstname
#
# @app.route('/sum/<int:x>/<int:y>')
# def sum(x,y):
#     total = x+y
#     return str(total)
# @app.route

if __name__ == '__main__':
  app.run(debug=True)
