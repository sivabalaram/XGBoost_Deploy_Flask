
from flask import Flask , render_template , request
import pickle
import numpy as np

model = pickle.load(open('health.pkl', 'rb'))



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
   
@app.route("/",methods=["POST"])
def predict():
    #HTML > PY
    #data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']

    arr = np.array([[ data2, data3, data4, data5, data6, data7, data8, data9, data10]])
    pred= model.predict(arr)
    
    #.PY > HTML
    return render_template('sub.html', data=pred)

    #.PY > HTML
    #return render_template("sub.html", n = name )
    # tumor is benign or malignant    

if __name__=="__main__":
    app.run(debug=True)    