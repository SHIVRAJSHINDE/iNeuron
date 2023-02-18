
from flask import Flask,render_template,request
import pickle
app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        FS=int(request.form["FS"])
        FU = int(request.form["FU"])
        with open('my_model','rb') as f:
            model = pickle.load(f)
        result = model.predict([[FS,FU]])
        if result[0]=="YES":
            return render_template('home.html',data=["Sorry you may ve Diabitiese +VE","red"])
        else:
            return render_template('home.html',data=["You are not positive","green"])
    else:
        return render_template('home.html')
  


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/postdata',methods=['POST'])
def submit():
    if request.method == 'POST':
        FS=int(request.form["FS"])
        FU = int(request.form["FU"])
        with open('my_model','rb') as f:
            model = pickle.load(f)
        result = model.predict([[FS,FU]])
        if result[0]=="YES":
            return "Sorry you may ve Diabitiese +VE"
        else:
            return "you are not positive"
        return "Submitted Succesfully"
    else:
        return "Something Went Wrong"


if __name__ == "__main__":
    app.run(debug=True)
    