from wtforms import Form, BooleanField, StringField,validators


#######FORMULARIO RENDERIZADO######
class RegistrationForm(Form):
    fullname = StringField('Fullname', [validators.DataRequired()])
    phone = StringField('Phone', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    
