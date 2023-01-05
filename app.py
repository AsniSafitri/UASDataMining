import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model_file = open('gnb_model2.pkl', 'rb')
model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('index.html', output='belum diprediksi')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Exited = int(request.form['Exited'])
        Gender = str(request.form['Gender'])
        Age = int(request.form['Age'])
        IsActiveMember = int(request.form['IsActiveMember'])
        EstimatedSalary = float(request.form['EstimatedSalary'])
        
        Gender_Male = request.form['Gender_Male'] 
        if(Gender_Male == 'Male'):
            Gender_Male = 1
        else:
            Gender_Female = 0
        prediction = model.predict([[Exited,Age,Gender,IsActiveMember,EstimatedSalary]])
        if prediction==1:
            return render_template('about.html',prediction_text="The Customer will leave the bank")
        else:
            return render_template('about.html',prediction_text="The Customer will not leave the bank")
                
if __name__=='__main__':
    app.run(debug=True)