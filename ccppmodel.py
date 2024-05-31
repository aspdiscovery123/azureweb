

import joblib
from flask import Flask,request,render_template

model=joblib.load(r'ccpp_model (2).pkl')

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

def application():
    if request.method =='GET':
        return  render_template('index.html',prediction=None)
    else:
        temp=request.form.get('temperature',type=float)
        humi=request.form.get('humidity',type=float)
        vacc=request.form.get('vacuum',type=float)
        pre=request.form.get('pressure',type=float)
        data=[temp,humi,pre,vacc]
        out=model.predict([data])
        print(out)
        return render_template('index.html',prediction=out) 

app.run(port=5004)