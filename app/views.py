import string
from datetime import datetime
import random

from flask import Flask, render_template, redirect, url_for
from . import forms, models

from . import db, app


@app.route('/', methods=['GET','POST'])
def index():
    form = forms.UrlForm()
    if form.validate_on_submit():
        URL = models.URLmodel()
        URL.original_url = form.original_url.data
        URL.short = get_short()
        db.session.add(URL)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template('index.html',
                           form=form)

@app.route('/urls', methods=['GET'])
def urls():
    url = models.URLmodel.query.all()
    return render_template('urls.html',
                           urls = url)

@app.route('/<short>', methods=['GET'])
def url_redirect(short):
    url = models.URLmodel.query.filter(models.URLmodel.short == short).first()
    url.visits += 1
    db.session.commit()

    return redirect(url.original_url)

def get_short():
    url_list = []
    url = models.URLmodel.query.all()
    for  i in url:
        url_list.append(i.short)
    new_url = url_generator()
    while new_url in url_list:
        new_url = url_generator()
    return new_url

def url_generator():
    link = ''
    dig = string.digits
    letters = string.ascii_letters

    for r in range(6):
        link += random.choice(dig+letters)
    return link