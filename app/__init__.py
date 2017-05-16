from flask import Flask, render_template, redirect, url_for, flash
from flask import Blueprint
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import PostForm
# from models import Post

# main = Blueprint('main', __name__)
#
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     Bootstrap(app)
#
#     app.register_blueprint(main)
#
#     return app


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

db = SQLAlchemy(app)

@app.route('/', methods=['Get'])
def index():
    # form = PostForm()
    # if form.validate_on_submit():
    #     post = Post(body=form.body)
    #     db.session.add(post)
    #     return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/edit', methods=['Get', 'Post'])
def edit_blog():
    form = PostForm()
    if form.is_submitted():
        flash(form.body.data)
    #     post = Post(body=form.body)
    #     db.session.add(post)
        return redirect(url_for('index'))
    return render_template('edit.html', form=form)

if __name__ == '__main__':
    app.run()