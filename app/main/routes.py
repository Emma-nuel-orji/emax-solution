import secrets
from app.models import Product, Payment, News, Agent, Project, Properties
from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, session
from app import db, mail
from app.forms import ContactForm, PaymentForm, SearchPropForm, SearchAgentForm, SearchProjForm
from app.models import User
from flask_login import current_user, login_required
from flask_mail import Message
from app.users.utils import save_picture

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    product = Product.query.all()
    form = SearchPropForm()
    return render_template("index.html", product=product, form=form)


@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")


@main.route('/projects', methods=['GET', 'POST'])
def projects():
    project = Project.query.all()
    return render_template("projects.html", project=project)


@main.route('/properties', methods=['GET', 'POST'])
def properties():
    property = Properties.query.all()
    return render_template("properties.html", property=property)


@main.route('/agents', methods=['GET', 'POST'])
def agents():
    agent = Agent.query.all()
    form = SearchAgentForm()
    return render_template("agents.html", agent=agent, form=form)



@main.route('/news', methods=['GET', 'POST'])
def news():
    news = News.query.all()
    return render_template("news.html", news=news)



@main.route('/gallery', methods=['GET', 'POST'])
# @login_required
def gallery():
    return render_template("gallery.html")


@main.route('/returnpolicy', methods=['GET', 'POST'])
def returnpolicy():
    return render_template("return.html")


@main.route('/terms', methods=['GET', 'POST'])
def terms():
    return render_template("terms.html")


@main.route('/privacy', methods=['GET', 'POST'])
def privacy():
    return render_template("privacy.html")



@main.route('/contact', methods=['GET', 'POST'])
def contact():
    user = User
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {form.name.data}', sender=f'{user.email}',
                      recipients=['support@emax-solution.com'])
        msg.body = f"""
           Name :  {form.name.data}

           Email :  {form.contact_email.data}

           Phone Number :  {form.number.data}

           Message :  {form.message.data}
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.index'))
    return render_template('contact.html', title='contact Form', form=form)


@main.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():
    global image_file
    if 'shoppingcart' not in session or len(session['shoppingcart']) <= 0:
        return redirect(url_for('product.product'))
    form = PaymentForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = picture_file
        description = form.description.data
        author = current_user
        product = Payment(image=image, description=description, author=author)
        db.session.add(product)
        db.session.commit()
        flash(
            'Your Payment proof has been uploaded successfully, Admin will get back to you whenever your payment is approved!',
            'success')
        return redirect(url_for('main.thanks'))
    elif request.method == 'GET':
        image_file = url_for('static', filename='img/' + current_user.image_file)

    subtotal = 0
    grandtotal = 0
    for key, product in session['shoppingcart'].items():
        discount = 0
        discount = (discount / 100) * float(product['price'].replace(',', ''))

        subtotal += float(product['price'].replace(',', ''))
        subtotal -= discount

        grandtotal = "{:,.2f}".format(subtotal)

    return render_template('payments.html', grandtotal=grandtotal, product=product, form=form, image_file=image_file)


@main.route('/proof')
@login_required
def proof():
    payment = Payment.query.all()
    return render_template('admin/proof.html', payment=payment)


# @main.route("/delete_proof/<int:payment_id>/delete", methods=['GET', 'POST'])
# def delete_proof(payment_id):
#     product = Payment.query.get_or_404(payment_id)
#     if current_user.email != 'orjiobiajulum@yahoo.com':
#         abort(403)
#     db.session.delete(product)
#     db.session.commit()
#     flash("the product has been deleted successfully", 'success')
#     return redirect(url_for('admin.admin1'))
#     return render_template("admin/proof.html", product=product)


@main.route("/delete_new/<int:new_id>/delete", methods=['GET', 'POST'])
def delete_new(new_id):
    new = News.query.get_or_404(new_id)
    if current_user.email != 'orjiobiajulum@yahoo.com':
        abort(403)
    db.session.delete(new)
    db.session.commit()
    flash("the product has been deleted successfully", 'success')
    return redirect(url_for('admin.admin1'))
    return render_template("admin.html", new=new)


@main.route("/delete_post/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    post = Agent.query.get_or_404(post_id)
    if current_user.email != 'orjiobiajulum@yahoo.com':
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("the product has been deleted successfully", 'success')
    return redirect(url_for('admin.admin1'))
    return render_template("admin.html", post=post)

@main.route("/delete_prop/<int:prop_id>/delete", methods=['GET', 'POST'])
def delete_prop(prop_id):
    prop = Properties.query.get_or_404(prop_id)
    if current_user.email != 'orjiobiajulum@yahoo.com':
        abort(403)
    db.session.delete(prop)
    db.session.commit()
    flash("the product has been deleted successfully", 'success')
    return redirect(url_for('admin.admin1'))
    return render_template("admin.html", prop=prop)


@main.route("/delete_proj/<int:proj_id>/delete", methods=['GET', 'POST'])
def delete_proj(proj_id):
    proj = Project.query.get_or_404(proj_id)
    if current_user.email != 'orjiobiajulum@yahoo.com':
        abort(403)
    db.session.delete(proj)
    db.session.commit()
    flash("the product has been deleted successfully", 'success')
    return redirect(url_for('admin.admin1'))
    return render_template("admin.html", proj=proj)


@main.route('/thanks')
@login_required
def thanks():
    return render_template('thank.html')




# search button goes here

@main.context_processor
def layout():
	form = SearchPropForm()
	return dict(form=form)

 
@main.route('/searchprop', methods=["POST"])
def searchprop():
	form = SearchPropForm()
	prop = Properties.query

	if form.validate_on_submit():
		# Get data from submitted form
		post.searched = form.searched.data
		# Query the Database
		prop = prop.filter(Properties.name.like('%' + post.searched + '%'))
		prop = prop.order_by(Properties.location).all()

		return render_template("searchprop.html",
		 form=form,
		 searched = post.searched,
		 prop = prop)



@main.route('/posts/<int:id>')
def post(id):
	prop = Properties.query.get_or_404(id)
	return render_template('users.html', prop=prop)


@main.route('/searchproj', methods=["POST"])
def searchproj():
	form = SearchProjForm()
	proj = Project.query

	if form.validate_on_submit():
		# Get data from submitted form
		posts.searched = form.searched.data
		# Query the Database
		proj = proj.filter(Project.name.like('%' + posts.searched + '%'))
		proj = proj.order_by(Project.location).all()

		return render_template("searchproj.html",
		 form=form,
		 searched = posts.searched,
		 proj = proj)



@main.route('/posts/<int:id>')
def posts(id):
	proj = Project.query.get_or_404(id)
	return render_template('users.html', proj=proj)
