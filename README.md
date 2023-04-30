# Predicting bike rental requests and creating a Flask web app


We got the dataset  of this project from [Kaggle](https://www.kaggle.com/competitions/bike-sharing-demand/data?select=sampleSubmission.csv) which was among Kaggle
competitions. In this competition, participants were asked to combine historical usage patterns with weather data in order to forecast bike rental demand in the Capital Bikeshare 
program in Washington, D.C.

The aim of this project is to provide a pipeline for predicting the bike rental request, and then create a Flask web API using the trained pipeline.

The repository contains a *BikeSharing.ipynb* notebook and a *deploy* folder. 

## run.py

The run.py script is the main script for your Flask web application, which serves as the entry point for the application. It contains the following components:

- Imports: The necessary libraries and modules are imported at the beginning of the script, including Flask, render_template, request, os, and pickle. 
It also imports the custom preprocessing module (preprocess.py).

- Initialization: The base path for the current file is determined using `os.path.dirname(os.path.abspath(__file__))`, and the path to the saved machine learning 
model (pipe.pkl) is constructed using `os.path.join(base_path, 'pipe.pkl')`. The Flask app is then instantiated with the name app.

- Route definition: The `@app.route('/', methods=['GET', 'POST'])` decorator defines the route for the home page of the application, which will handle both GET 
and POST requests.

- `home()` function: This function is the main handler for the home page route. It initializes the `y_predict` variable to a default value (e.g., -1). 
When a user submits the form (with a POST request), the function loads the saved pipeline using pickle, extracts the input values from the form, creates a DataFrame 
with the input values, and makes a prediction using the pipeline. The predicted value is assigned to the `y_predict` variable.

- Rendering the template: At the end of the `home()` function, the `render_template()` function is called to render the index.html template and display the result to
the user. The `y_predict` variable is passed to the template as the prediction parameter.

- Running the app: The `if __name__ == '__main__'`: block checks if the script is being run as the main module, and if so, it starts the Flask development server 
with the `app.run(debug=True)` command. The `debug=True` parameter enables the debug mode for easier development and troubleshooting.

In summary, the run.py script creates a Flask web application that loads a saved machine learning pipeline, takes user input through a form, preprocesses the input
data, makes a prediction using the pipeline, and displays the result to the user on the index.html page.

## index.html
This script is an HTML file containing the user interface of the web app. It consists of the following elements:

- A form with the POST method to submit the user's input data to the Flask API for processing.

- Input fields for the user to enter the required information for the prediction:

- 1. Date and time
- 2. Season
- 3. Holiday
- 4. Working day
- 5. Weather
- 6. emperature
- 7. Feel like (atemp)
- 8. Humidity
- 9. Windspeed

Each input field is accompanied by a label and a placeholder to guide the user.

- A submit button to trigger the form submission and send the input data to the Flask API for processing.

-A paragraph `(<p>)` element that displays the bike sharing prediction result received from the Flask API. The Flask API sends the predicted value to the
index.html script using the `{{prediction}}` placeholder, which is rendered by the Jinja2 template engine in Flask.

This index.html script, along with the run.py script, together create a web application for users to input data and receive bike sharing predictions 
using the machine learning pipeline.

## preprocess.py

The preprocessing script provided contains a set of custom transformers for preprocessing the input data before feeding it to the machine learning model. 
The script consists of four classes:

- `Preprocess`: This class inherits from BaseEstimator and TransformerMixin from sklearn. It serves as a base class for your custom transformers and implements the
fit and transform methods. The fit method is a placeholder that returns the object itself, while the transform method is an empty placeholder method that needs to be 
overridden by child classes.

- `ExtractData`: This class inherits from the Preprocess class and overrides the transform method. It extracts additional features from the datetime column of the 
input data, such as year, month, hour, and day of the week.

- `DataType`: This class also inherits from the Preprocess class and overrides the transform method. It converts the data type of the specified categorical columns to 
the category data type.

- `Encoding`: This class inherits from the Preprocess class, and it is responsible for one-hot encoding the categorical variables. It has a fit method that stores the
columns generated after one-hot encoding, ensuring that the same set of columns are created for any input data. The transform method performs the one-hot encoding
and adds any missing columns (with values set to 0) to match the stored columns.

- `Drop`: This class also inherits from the Preprocess class and overrides the transform method. It drops unnecessary columns from the input data, such as casual,
registered, atemp, datetime, and count. If some of these columns are not present in the input data, it will only drop the available ones (atemp and datetime).

These custom transformers can be used in a pipeline to preprocess the input data before passing it to the machine learning model for prediction.
