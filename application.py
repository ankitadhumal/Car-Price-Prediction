import pickle

import pandas as pd
import numpy as np
import pickle
from flask import Flask,render_template , request

#here we are creating an object of flask
app = Flask(__name__)

model=pickle.load(open(r"C:\Users\hp\Downloads\PROJECT2CAR-PRICE-PREDICTION\LinearRegressionModel.pkl","rb"))
cars = pd.read_csv(r"C:\Users\hp\Downloads\Cleaned_Cars.csv")

#if anyone hits the route "/" then the index will be called
#index will called only when someone hits our URL
@app.route("/")
def index():
    company = sorted(cars["company"].unique())
    car_model = sorted(cars["name"].unique())
    year = sorted(cars["year"].unique(),reverse=True)
    fuel_type = sorted(cars["fuel_type"].unique())
    company.insert(0,"select company")
    return render_template("index.html",company=company,car_model=car_model,years=year,fuel_types=fuel_type)

@app.route("/predict",methods=["POST"])
def predict():
    company=request.form.get("company")
    car_model=request.form.get("car_model")
    year = int(request.form.get("year"))
    fuel_type = request.form.get("fuel_type")
    kms_driven = int(request.form.get("kilo_driven"))
    print(company,car_model,year,fuel_type,kms_driven)

    prediction=model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],columns=["name","company","year","kms_driven","fuel_type"]))

    return str(np.round(prediction[0],2))


if __name__=="__main__":
    app.run(debug=True)