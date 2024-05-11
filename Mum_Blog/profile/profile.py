from flask import Blueprint, render_template
from flask import current_app as app
from faker import Faker

fake = Faker()

profile_blueprint = Blueprint(
    "profile_blueprint",
    __name__,
    static_folder='static',
    template_folder='templates',
)

@profile_blueprint.route('/profile', methods=["GET"])
def profile() -> str:
    user = fake.simple_profile()
    job = fake.job()
    return render_template(
        "profile.jinja2",
        template="profile-template",
        user=user,
        job=job
    )