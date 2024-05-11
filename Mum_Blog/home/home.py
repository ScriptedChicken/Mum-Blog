from flask import Blueprint, render_template
from flask import current_app as app

from Mum_Blog.api import get_posts, get_quotes

home_blueprint = Blueprint(
    "home_blueprint",
    __name__,
    static_folder='static',
    template_folder='templates',
)

@home_blueprint.route('/', methods=["GET"])
def home() -> str:
    posts = get_posts()
    quotes = get_quotes()
    return render_template(
        "index.jinja2",
        title="Latest Posts",
        subtitle="Hear what the people have to say",
        template="home-template",
        posts=posts,
        quotes=quotes
    )