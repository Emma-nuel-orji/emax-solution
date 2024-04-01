from flask import render_template, url_for, flash, redirect, Blueprint
from app.models import User, Product
from flask_login import current_user, login_required


admin = Blueprint('admin', __name__)


@admin.route('/admin', methods=['GET', 'POST'])
@login_required
def admin1():
    if current_user.email != 'orjiobiajulum@yahoo.com':
        flash("Sorry you have to be an admin to access this page", "info")
        return redirect(url_for('main.index'))
    product = Product.query.all()
    users = User.query.all()
    return render_template("admin.html", product=product, users=users)

    # users = User.query.all()
    # product = Product.query.all()
    # if current_user.email != 'emeraldinteriorservices@gmail.com':
    #     flash('Please you cant access to this page', 'danger')
    #     return redirect(url_for('main.index', users=users, product=product))
    # else:
    #     render_template('admin/home.html', users=users, product=product)
    # return render_template("admin/index.html", users=users, product=product,)


@admin.route('/users', methods=['GET', 'POST'])
# @login_required
def users():
    if current_user.email != 'emeraldinteriorservices@gmail.com':
        flash("Sorry you have to be an admin to access this page", "info")
        return redirect(url_for('main.index'))
    user = User.query.all()
    return render_template("admin/users.html", user=user)


