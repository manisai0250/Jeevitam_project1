from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField
from wtforms.validators import InputRequired, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure random key

# Define a simple form using Flask-WTF
class RegistrationForm(FlaskForm):
    yourname = StringField('Your Name', validators=[InputRequired()])
    emailaddress = StringField('Email Address', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    phone = StringField('Phone', validators=[InputRequired()])
    longitude = StringField('Longitude', validators=[InputRequired()])
    latitude = StringField('Latitude', validators=[InputRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], validators=[InputRequired()])
    city = StringField('City', validators=[InputRequired()])
    postal_code = StringField('Postal Code', validators=[InputRequired()])

# Dummy database connection
# Replace this with your MySQL database connection
# Note: Using SQLAlchemy for a real-world application is recommended
# Also, remember to secure your database connection
def save_to_database(data):
    # Your database logic here
    print("Data saved to the database:", data)

# Route to handle registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate_on_submit():
        data = {
            'yourname': form.yourname.data,
            'emailaddress': form.emailaddress.data,
            'password': form.password.data,
            'phone': form.phone.data,
            'longitude': form.longitude.data,
            'latitude': form.latitude.data,
            'gender': form.gender.data,
            'city': form.city.data,
            'postal_code': form.postal_code.data,
        }

        save_to_database(data)
        flash('Registration successful!', 'success')
        return redirect(url_for('register'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
