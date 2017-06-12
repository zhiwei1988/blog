from datetime import datetime
from . import db
from markdown import markdown
import bleach


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, index=True, primary_key=True)
    title = db.Column(db.String, index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
         allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                         'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                         'h1', 'h2', 'h3', 'p']
         target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'),
                                                        tags=allowed_tags, strip=True))


db.event.listen(Post.body, 'set', Post.on_changed_body)
