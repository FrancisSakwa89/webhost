from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required, DataRequired, Email


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about youself.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title = StringField('Link title',validators=[DataRequired()])
    post = TextAreaField('Paste your link',validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Add comment',validators=[DataRequired()])
    submit = SubmitField('Submit')


class SubscribeForm(FlaskForm):
    username = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    submit = SubmitField('Subscribe')
