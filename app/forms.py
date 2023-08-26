from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL



class UrlForm(FlaskForm):
    original_url = StringField(
        'Вставте ссылку',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов'),
                    URL(message='Введите ссылку начинающуюся с https://')]
    )
    submit = SubmitField('Получить короткую ссылку')