import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import mail


#save picture 
def save_picture(form_picture): 
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) #the _ is used to get rid of the filename variable
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    #resizing the oicture before saving it
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
         sender='noreply@gmail.com', 
        recipients=[user.email])
    msg.body = f'''
To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
The link expires after 30 minutes.
If you did not make this request then simply ignore this email and no changes will be made.
''' 
    mail.send(msg)