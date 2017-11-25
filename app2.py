from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('home.html')
@app.route('/aboutme')
def hi ():
    return ("my name is Huong. I am studying at NEU. I like watching movies and hanging out with friends. I have a cat, she is called Miu")
@app.route('/school')
def hello_hi():
    return ("http://techkids.vn/")
if __name__ == '__main__':
  app.run(debug=True)
