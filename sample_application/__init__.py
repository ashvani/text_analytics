import dateutil.parser

from flask import Flask, render_template
from flask_adminlte import AdminLTE


class User(object):
    """
    Example User object.  Based loosely off of Flask-Login's User model.
    """
    full_name = "Ashvani Dubey"
    avatar = "/static/img/ashvani.jpg"
    created_at = dateutil.parser.parse("December 27, 2017")


def create_app(configfile=None):
    app = Flask(__name__)
    AdminLTE(app)

    # This is a placeholder user object.  In the real-world, this would
    # probably get populated via ... something.
    current_user = User()

    @app.route('/')
    def index():
        return render_template('index.html', current_user=current_user)

    @app.route('/login')
    def login():
        return render_template('login.html', current_user=current_user)

    @app.route('/lockscreen')
    def lockscreen():
        return render_template('lockscreen.html', current_user=current_user)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
