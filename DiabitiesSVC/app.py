
from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST','GET'])
def submit():
    if request.method =="POST":
   
        Clump = int(request.form["Clump"])
        UnifSize = int(request.form["UnifSize"])
        UnifShape = int(request.form["UnifShape"])
        MargAdh = int(request.form["MargAdh"])
        SingEpiSize = int(request.form["SingEpiSize"])
        BareNuc = int(request.form["BareNuc"])
        BlandChrom = int(request.form["BlandChrom"])
        NormNucl = int(request.form["NormNucl"])
        Mit = int(request.form["Mit"])
   
        with open('my_model','rb') as f:
            model = pickle.load(f)

        print("details are:  " )
        abc = model.predict([[Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc, BlandChrom, NormNucl, Mit]])
        abc = list(abc)
        
        if abc[0] == 2 :
            return render_template('home.html',data=["you are not +ve","red"]) # "result is " + str(abc[0])
        else:
            return render_template('home.html',data=["you are +ve","green"]) # "result is " + str(abc[0])
        #print(type(model.predict([[Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc, BlandChrom, NormNucl, Mit]])))
        #return "submitted succesfully"
    else:
        return "something went wrong"
#return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
    