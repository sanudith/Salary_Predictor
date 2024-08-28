from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
#Load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')
def home():
    result = ""
    return render_template('index.html')

#functions for predict the values by the model
@app.route('/predict', methods = ['POST','GET'])
def predict():
    yearsCount = float(request.form['YearsExperience'])
    #yearsCount = float(request.form['YearsExperience'])
    result = model.predict([[yearsCount]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug = True)


