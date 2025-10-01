"""
This script imports the necessary libraries for building
a Flask web application with form handling using Flask-WTF.

- pandas (pd): For data manipulation and analysis (if needed in the app).
- FlaskForm: Base class for creating forms in Flask using Flask-WTF.
- wtforms fields: Provides different types of form input fields
  (SelectField, DateField, TimeField, IntegerField, SubmitField).
- wtforms.validators: Provides validation rules (e.g., DataRequired ensures
  that the field must not be left empty).
"""

# Import pandas for data handling
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired


# getting the data
train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")

class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=X_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )
    date_of_journey = DateField(
        label="Date of Journey",
        validators=[DataRequired()]
    )
    source = SelectField(
        label="Source",
        choices=X_data.source.unique().tolist(),
        validators=[DataRequired()]
    )
    destination = SelectField(
        label="Destination",
        choices=X_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )
    dep_time = TimeField(
        label="Departure Time",
        validators=[DataRequired()]
    )
    arrival_time = TimeField(
        label="Arrival Time",
        validators=[DataRequired()]
    )
    duration = IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices=X_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
