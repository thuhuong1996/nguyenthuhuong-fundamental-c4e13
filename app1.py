from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('home.html')
@app.route('/bmi/<int:weight>/<int:height>')
def eval(weight,height):
    bmi_result = weight/(height*height)
    if bmi_result < 16:
        return ("Severely underweight")
    elif 16 <= bmi_result < 18.5:
        return("underweight")
    elif 18.5 <= bmi_result < 25:
        return("normal")
    elif 25 <= bmi_result < 30:
        return("overweight")
    else:
        return("obese")



if __name__ == '__main__':
  app.run(debug=True)
