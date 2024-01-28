from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FloatField, SubmitField, FieldList, HiddenField, FormField, MultipleFileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class StepForm(Form):
    order = HiddenField(default=1)
    description = TextAreaField(validators=[DataRequired()])
    #submit = SubmitField('Add Step')

class IngredientForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    quantity = FloatField('Quantity', validators=[DataRequired()])
    unit = StringField('Unit', validators=[DataRequired()])
    #submit = SubmitField('Add Ingredient')

class DrinkForm(Form):
    name = StringField('Name',  validators=[DataRequired()])


class RecipeForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    cooking_time = IntegerField('Cooking Time', validators=[DataRequired()])
    steps = FieldList(FormField(StepForm), min_entries=1)
    ingredients = FieldList(FormField(IngredientForm), min_entries=1)
    drinks = FieldList(FormField(DrinkForm))
    photos = MultipleFileField('Image', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
        ])
    

