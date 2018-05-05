# -*- coding:utf-8 -*-

from flask import render_template, redirect, url_for
from flask_login import login_required
from .forms import PostForm
from . import main
from ..models import Post, Category
from .. import db
from markdown import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.codehilite import CodeHiliteExtension


@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/category/coding')
def category_coding():
    category = Category.query.filter_by(name=u'Coding').first()
    if category:
        posts = category.posts
        return render_template('index.html', posts=posts)

    return render_template('default.html')

@main.route('/category/productivity')
def category_productivity():
    category = Category.query.filter_by(name=u'Productivity').first()
    if category:
        posts = category.posts
        return render_template('index.html', posts=posts)

    return render_template('default.html')

@main.route('/category/life')
def category_life():
    category = Category.query.filter_by(name=u'Life').first()
    if category:
        posts = category.posts
        return render_template('index.html', posts=posts)

    return render_template('default.html')

@main.route('/category/study')
def category_study():
    category = Category.query.filter_by(name=u'Study').first()
    if category:
        posts = category.posts
        return render_template('index.html', posts=posts)

    return render_template('default.html')

@main.route('/edit', methods=['Get', 'Post'])
@login_required
def edit_blog():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data, summary=form.summary.data)
        category = Category.query.filter_by(name=form.category.data).first()
        if not category:
            category = Category(name=form.category.data)
            db.session.add(category)
            db.session.commit()
        post.category = category
        db.session.add(post)
        db.session.commit()
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
        post.summary = form.summary.data
        category = Category.query.filter_by(name=form.category.data).first()
        if not category:
            category = Category(name=form.category.data)
            db.session.add(category)
            db.session.commit()
        post.category = category
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    form.body.data = post.body
    form.title.data = post.title
    form.category.data = post.category.name
    form.summary.data = post.summary.name
    return render_template('modify.html', form=form, id=id)


@main.route('/delete/<int:id>')
@login_required
def delete_blog(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('.index'))


@main.route('/archive/<int:id>')
def get_article(id):
    article = Post.query.get_or_404(id)
    article.body_html = markdown(article.body,
                                 extensions=[FencedCodeExtension(), TableExtension()],
                                 output_format='html')
    return render_template('post.html', article=article)
