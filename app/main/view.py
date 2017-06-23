# -*- coding:utf-8 -*-

from flask import render_template, redirect, url_for
from flask_login import login_required
from .forms import PostForm
from . import main
from ..models import Post
from .. import db


@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts)


@main.route('/edit', methods=['Get', 'Post'])
@login_required
def edit_blog():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data)
        db.session.add(post)
        return redirect(url_for('.index'))
    return render_template('edit.html', form=form)


@main.route('/edit/<int:id>', methods=['Get', 'Post'])
@login_required
def modify_blog(id):
    form = PostForm()
    post = Post.query.get_or_404(id)
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.add(post)
        return redirect(url_for('.index'))
    form.body.data = post.body
    form.title.data = post.title
    return render_template('modify.html', form=form, id=id)


@main.route('/delete/<int:id>')
@login_required
def delete_blog(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    return redirect(url_for('.index'))


@main.route('/archive/<int:id>')
def get_article(id):
    article = Post.query.get_or_404(id)
    return render_template('post.html', article=article)
