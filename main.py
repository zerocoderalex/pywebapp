
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


app = Flask(__name__)
app.secret_key = 'your_secret_key'
user = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'password': 'password123'
}


class ProfileForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6, max=35)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Сохранить изменения')

@app.route('/')
@app.route('/edit_profile')
def edit_profile():
    form = ProfileForm()
    if form.validate_on_submit():
        # Обновляем данные пользователя
        user['name'] = form.name.data
        user['email'] = form.email.data
        user['password'] = form.password.data
        flash('Профиль успешно обновлен!', 'success')
        return redirect(url_for('edit_profile'))

    # Заполнение формы данными пользователя
    form.name.data = user['name']
    form.email.data = user['email']

    return render_template('edit_profile.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)