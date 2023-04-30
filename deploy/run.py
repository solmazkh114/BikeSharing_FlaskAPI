from flask import Flask, render_template, request
from preprocess import *
import pickle
import os

base_path = os.path.dirname(os.path.abspath(__file__))
pipe_path = os.path.join(base_path, 'pipe.pkl')
#print(pipe_path)

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
#@app.route('/index')
def home():
    y_predict = -1
    if request.method == "POST":
        pipe = pickle.load(open(pipe_path, 'rb'))
        
        # retrieve input field values using request.form.get()
        datetime = request.form.get('datetime')
        season = request.form.get('season')
        holiday = request.form.get('holiday')
        workingday = request.form.get('workingday')
        weather = request.form.get('weather')
        temp = float(request.form.get('temp'))
        atemp = float(request.form.get('atemp'))
        humidity = float(request.form.get('humidity'))
        windspeed = float(request.form.get('windspeed'))


        # create a list of the input field values
        input_list = [datetime, season, holiday, workingday, weather, temp, atemp, humidity, windspeed]
        # define the column names in the same order as the input_list
        column_names = ['datetime', 'season', 'holiday', 'workingday', 'weather', 'temp', 'atemp', 'humidity', 'windspeed']

        # create a DataFrame using the input_list and column names
        input_df = pd.DataFrame([input_list], columns=column_names)

        # make the prediction using the pipeline
        y_predict = pipe.predict(input_df)


    return render_template("index.html", prediction = int(y_predict))

if __name__== '__main__':
    app.run(debug =True)
    