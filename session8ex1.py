from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def a():
 return render_template('poet.html')


if __name__ == '__main__':
  app.run(debug=True)
