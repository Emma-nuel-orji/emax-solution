from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from app import db
from app.posts.forms import ProductForm
from app.models import Product
from flask_login import current_user, login_required
from app.posts.utils import save_picture

posts = Blueprint('posts', __name__)


@posts.route('/agentpost', methods=['GET', 'POST'])
@login_required
def agentpost():
    global image_file
    form = ProductForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        category = form.category.data
        desc = form.desc.data
        author = current_user
        product = Product(name=name, price=price, discount=discount, category=category, desc=desc, author=author, image=image)
        db.session.add(product)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('admin.home'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('agentpost.html', form=form, image_file=image_file)


@posts.route('/newspost', methods=['GET', 'POST'])
@login_required
def newspost():
    global image_file
    form = ProductForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        category = form.category.data
        desc = form.desc.data
        author = current_user
        product = Product(name=name, price=price, discount=discount, category=category, desc=desc, author=author, image=image)
        db.session.add(product)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('admin.home'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('newspost.html', form=form, image_file=image_file)


@posts.route('/propertiespost', methods=['GET', 'POST'])
@login_required
def propertiespost():
    global image_file
    form = ProductForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        category = form.category.data
        desc = form.desc.data
        author = current_user
        product = Product(name=name, price=price, discount=discount, category=category, desc=desc, author=author, image=image)
        db.session.add(product)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('admin.home'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('propertiespost.html', form=form, image_file=image_file)



@posts.route('/projectspost', methods=['GET', 'POST'])
@login_required
def projectpost():
    global image_file
    form = ProductForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        category = form.category.data
        desc = form.desc.data
        author = current_user
        product = Product(name=name, price=price, discount=discount, category=category, desc=desc, author=author, image=image)
        db.session.add(product)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('admin.home'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('projectpost.html', form=form, image_file=image_file)



@posts.route('/adminagent', methods=['GET', 'POST'])
# @login_required
def adminagent():
    product = Product.query.all()
    return render_template("adminagent.html", product=product)


@posts.route('/adminnews', methods=['GET', 'POST'])
# @login_required
def adminnews():
    product = Product.query.all()
    return render_template("adminnews.html", product=product)



@posts.route('/adminproperties', methods=['GET', 'POST'])
# @login_required
def adminproperties():
    product = Product.query.all()
    return render_template("adminproperties.html", product=product)


@posts.route('/adminproject', methods=['GET', 'POST'])
# @login_required
def adminproject():
    product = Product.query.all()
    return render_template("adminproject.html", product=product)


# @posts.route('/product', methods=['GET', 'POST'])
# def product():
#     page = request.args.get('page', 1, type=int)
#     product = Product.query.paginate(page=page, per_page=20)
#     return render_template("product.html", product=product)



@posts.route('/single_product', methods=['GET', 'POST'])
def single_product():
    product = Product.query.all()
    return render_template('single_product.html', product=product)


# @posts.route("/productpost/<int:product_id>", methods=['GET', 'POST'])
# def products(product_id):
#     prod = Product.query.get_or_404(product_id)
#     return render_template("single_product.html", prod=prod)


@posts.route('/single_project', methods=['GET', 'POST'])
def single_project():
    return render_template("single_project.html")


@posts.route('/single_properties', methods=['GET', 'POST'])
def single_properties():
    return render_template("single_properties.html")


@posts.route('/single_agent', methods=['GET', 'POST'])
def single_agent():
    return render_template("single_agent.html")

@posts.route('/single_news', methods=['GET', 'POST'])
def single_news():
    return render_template("single_news.html")

