from functools import wraps
from flask import session, redirect, url_for, flash

def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('You need to log in as admin to access this page.', 'danger')
            return redirect(url_for('routes.adminlogin'))
        return f(*args, **kwargs)
    return decorated_function
def faculty_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('faculty_logged_in'):
            flash('You need to log in as faculty to access this page.', 'danger')
            return redirect(url_for('routes.facultylogin'))
        return f(*args, **kwargs)
    return decorated_function
