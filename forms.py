from wtforms import Form, BooleanField, StringField,validators



class RegistrationForm(Form):
    fullname = StringField('Fullname', [validators.DataRequired()])
    phone = StringField('Phone', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])