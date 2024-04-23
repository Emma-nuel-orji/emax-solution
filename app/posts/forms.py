from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField ,TextAreaField
from wtforms.validators import DataRequired, Length, Email


class NewsForm(FlaskForm):
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Post News')

class AgentForm(FlaskForm):
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    name = StringField('Agent Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Post Agent')
    
    
class ProjectForm(FlaskForm):
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    name = StringField('Project Name', validators=[DataRequired()])
    
    status = SelectField('Property Status', validators=[DataRequired()], choices=[("--Select One--"), ("Selling"),("Renting")])
    type = SelectField('Category', validators=[DataRequired()], choices=[("--Select One--"), ("House"),("Land"),("Commercial property")])
    
    blocks = StringField('Number Of Blocks', validators=[DataRequired()])
    flats = StringField('Number Of Flats', validators=[DataRequired()])
    floors = StringField('Number Of Floors', validators=[DataRequired()])
    
    description = StringField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Post Project')

    
class PropertiesForm(FlaskForm):
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    
    name = StringField('Property Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    status = SelectField('Property Status', validators=[DataRequired()], choices=[("--Select One--"), ("Selling"),("Renting")])
    type = SelectField('Property type', validators=[DataRequired()], choices=[("--Select One--"), ("House"),("Land"),("Commercial property")])
    
    square = StringField('Square', validators=[DataRequired()])
    bedroom = StringField('Number Of Bedrooms', validators=[DataRequired()])
    bathroom = StringField('Number Of Bathroom', validators=[DataRequired()])
    floors = StringField('Number Of Floors', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    
    pic = FileField('Upload Your Profile', validators=[FileAllowed(['jpg', 'png'])])
    fullname = StringField('Fullname', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    
    submit = SubmitField('Post Property')    