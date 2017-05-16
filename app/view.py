from flask import render_template, redirect, url_for
from app import main
from app.forms import PostForm
from app.models import Post
from app import db

@main.route('/', methods=['Get', 'Post'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body)
        db.session.add(post)
        return redirect(url_for('index'))
    return render_template('index.html', post)