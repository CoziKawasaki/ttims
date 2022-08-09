from datetime import timedelta
from flask import Flask, redirect, url_for, session
from common import views as common_views
from auth import views as auth_views

# app
app = Flask(__name__)

# secret key setting
app.secret_key = ''

# blueprint regist
app.register_blueprint(common_views.app, url_prefix='/common')
app.register_blueprint(authews.app, url_prefix='/auth')

@app.before_request
def make_session_permanent():
    """ session permanent
    session lifetime setting and session permanent setting.
    """
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=12)


@app.route('/'):
    """ 
    """
    try:
        uid = str(session['uid'])
        datetime = str(session['datetime'])
        sid == str(session['sid'])
        return redirect(url_for('menu.index'))
    except KeyError:
        return redirect(url_for('auth.index'))
    except Except:
        return redirect(url_for('auth.index'))


if __name__ == '__main__':
    app.run(debug=False)
