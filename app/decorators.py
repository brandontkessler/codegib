from functools import wraps
from flask import flash, redirect, url_for, abort
from flask_login import current_user


def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.confirmed is False:
            flash('Please confirm your account!', 'warning')
            return redirect(url_for('auth.unconfirmed'))
        return func(*args, **kwargs)

    return decorated_function


def check_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.admin_priv is False:
            abort(403, 'You cannot access this page.')
        return func(*args, **kwargs)

    return decorated_function


def check_blogger(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.blog_priv is False:
            abort(403, 'You cannot access this page.')
        return func(*args, **kwargs)
    return decorated_function
