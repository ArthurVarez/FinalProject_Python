#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:56:41 2021

@author: Arthur
"""

from flask import Flask, render_template,request,redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField , FloatField , SelectField, SubmitField
from wtforms.validators import  DataRequired, InputRequired , NumberRange
from flask_wtf import Form
import joblib
import pandas as pd 
import sklearn


app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "key"

age_choices = [
    (-0.95197,"18-24"),(-0.07854,"25-34"),(0.49788,"35-44"),(1.09449,"45-54"),
    (1.82213,"55-64"),(2.59171,"65+")]
gender_choices = [(-0.48246,"Male"), (0.48246,"Female")]

education_choices = [(-2.43591,"Left school before 16 years"),(-1.73790,"Left school at 16 years"),
    (-1.43719 ,"Left school at 17 years"),(-1.22751,"Left school at 18 years")
    ,(-0.61113,"Some college or university"),(-0.05921,"Professional certificate/ diploma")
    ,(0.45468,"University degree"), (1.16365,"Masters degree"),(1.98437,"Doctorate degree")]

country_choices = [(-0.09765 ,"Australia"),(0.24923,"Canada"),(-0.46841,"New Zealand"),
    (-0.28519,"Other"),(0.21128,"Republic of Ireland"),(0.96082,"UK")
    ,(-0.57009,"USA")]
ethnicity_choices = [(-0.50212,"Asian"),(-1.10702,"Black"),(1.90725,"Mixed-Black/Asian"),
    (0.12600,"Mixed-White/Asian"),(-0.22166,"Mixed-White/Black"),(0.11440,"Other"),
    (-0.31685,"White")]

class Submit(FlaskForm):
    submit = SubmitField("Predict")

class MyForm(FlaskForm):
    name = StringField("Name : ", validators=[DataRequired()])
    age = SelectField("Age : ", choices=age_choices, coerce= float , validators=[InputRequired()])
    gender= SelectField("Gender : ", choices=gender_choices, coerce= float , validators=[InputRequired()])
    education= SelectField("Education : ", choices=education_choices, coerce= float , validators=[InputRequired()])
    country= SelectField("Country : ", choices=country_choices, coerce= float , validators=[InputRequired()])
    ethnicity= SelectField("Ethnicity : ", choices=ethnicity_choices, coerce= float , validators=[InputRequired()])
    Nscore = FloatField("Nscore(between -3.46436 and 3.27393)", validators=[DataRequired(),NumberRange(min=-3.46436, max=3.27393)])
    Escore = FloatField("Escore(between -3.27393 and 3.27393)", validators=[DataRequired(),NumberRange(min=-3.27393, max=3.27393)])
    Oscore = FloatField("0score(between -3.27393 and  2.90161)", validators=[DataRequired(),NumberRange(min=-3.27393, max= 2.90161)])
    Ascore = FloatField("Ascore(between -3.46436 and 3.46436)", validators=[DataRequired(),NumberRange(min=-3.46436, max=3.46436)])
    Cscore = FloatField("Cscore(between -3.46436 and 3.46436)", validators=[DataRequired(),NumberRange(min=-3.46436, max=3.46436)])
    Impulsive = FloatField("Impulsive(between -2.55524  and 2.90161)", validators=[DataRequired(),NumberRange(min=-2.55524, max=2.90161)])
    SS = FloatField("SS(between -2.07848 and 1.92173 )", validators=[DataRequired(),NumberRange(min=-2.07848, max=1.92173 )])
    Submit = SubmitField("Submit")


@app.route("/",methods=["GET","POST"])

def Hello():
    
    return render_template('welcome.html')



@app.route("/predict",methods=["GET","POST"])

def Informations_Form():
    myform = MyForm()
    if request.method=="POST" and myform.validate_on_submit:
        model = joblib.load('best_model.joblib')
        result = model.predict(pd.DataFrame([[myform.age,myform.gender,myform.education,myform.country
        ,myform.ethnicity,myform.Nscore,myform.Escore,myform.Oscore,myform.Ascore,myform.Cscore
        ,myform.Impulsive,myform.SS]],columns=  ['Age', 'Gender', 'Education', 'Country', 'Ethnicity', 'Nscore',
       'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS']))
        render_template('results.html',result = result,name=myform.name)
    return render_template('prediction.html',form=myform)
    
    


if __name__== "__main__":
    app.run(port=5050)