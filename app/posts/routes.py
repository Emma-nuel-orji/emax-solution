from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from app import db
from app.posts.forms import NewsForm, AgentForm, ProjectForm, PropertiesForm
from app.models import Product, Properties, Project, News, Agent
from flask_login import current_user, login_required
from app.posts.utils import save_picture

posts = Blueprint('posts', __name__)


@posts.route('/agentpost', methods=['GET', 'POST'])
@login_required
def agentpost():
    global image_file
    form = AgentForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
        name = form.name.data
        email = form.email.data
        phone = form.phone.data

        author = current_user
        agen = Agent(name=name, email=email, phone=phone, author=author, image=image)
        db.session.add(agen)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts.adminagent'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('agentpost.html', form=form, image_file=image_file)


@posts.route('/newspost', methods=['GET', 'POST'])
@login_required
def newspost():
    global image_file
    form = NewsForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
        title = form.title.data
        description = form.description.data
        
        author = current_user
        new = News(title=title, description=description, author=author, image=image)
        db.session.add(new)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts.adminnews'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('newspost.html', form=form, image_file=image_file)


@posts.route('/projectpost', methods=['GET', 'POST'])
@login_required
def projectpost():
    global image_file
    form = ProjectForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
        name = form.name.data
        status = form.status.data
        type = form.type.data
        
        blocks = form.blocks.data
        floors = form.floors.data
        flats = form.flats.data
        
        description = form.description.data
        location = form.location.data
        
        author = current_user
        proj = Project(name=name, status=status, author=author, description=description, location=location, image=image, blocks=blocks, floors=floors, flats=flats, type=type)
        db.session.add(proj)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts.adminproject'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('projectpost.html', form=form, image_file=image_file)



@posts.route('/propertiespost', methods=['GET', 'POST'])
@login_required
def propertiespost():
    global image_file
    form = PropertiesForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
            
        if form.pic.data:
            picture_file = save_picture(form.pic.data)
            pic = picture_file
        name = form.name.data
        
        location = form.location.data
        status = form.status.data
        square = form.square.data
        bedroom = form.bedroom.data
        bathroom = form.bathroom.data
        floors = form.floors.data
        price = form.price.data
        description = form.description.data
        type = form.type.data
        
        fullname = form.fullname.data
        phone = form.phone.data
        email = form.email.data
        
        author = current_user
        prop = Properties(name=name, type=type, price=price, author=author, location=location, status=status, square=square, bedroom=bedroom, bathroom=bathroom, floors=floors, description=description, image=image, fullname=fullname, phone=phone, email=email, pic=pic)
        db.session.add(prop)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts.adminproperties'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('propertiespost.html', form=form, image_file=image_file)



@posts.route('/adminagent', methods=['GET', 'POST'])
# @login_required
def adminagent():
    agent = Agent.query.all()
    return render_template("adminagent.html", agent=agent)


@posts.route('/adminnews', methods=['GET', 'POST'])
# @login_required
def adminnews():
    news = News.query.all()
    return render_template("adminnews.html", news=news)



@posts.route('/adminproperties', methods=['GET', 'POST'])
# @login_required
def adminproperties():
    property = Properties.query.all()
    return render_template("adminproperties.html", property=property)


@posts.route('/adminproject', methods=['GET', 'POST'])
# @login_required
def adminproject():
    project = Project.query.all()
    return render_template("adminproject.html", project=project)


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


@posts.route('/single_project/<int:proj_id>', methods=['GET', 'POST'])
def single_project(proj_id):
    proj = Project.query.get_or_404(proj_id)
    return render_template("single_project.html", proj=proj)


@posts.route('/single_properties/<int:prop_id>', methods=['GET', 'POST'])
def single_properties(prop_id):
    prop = Properties.query.get_or_404(prop_id)
    return render_template("single_properties.html", prop=prop)


@posts.route('/single_agent/<int:post_id>', methods=['GET', 'POST'])
def single_agent(post_id):
    post = Agent.query.get_or_404(post_id)
    return render_template("single_agent.html", post=post)

@posts.route('/single_news/<int:new_id>', methods=['GET', 'POST'])
def single_news(new_id):
    new = News.query.get_or_404(new_id)
    news = News.query.all()
    return render_template("single_news.html", new=new, news=news)

