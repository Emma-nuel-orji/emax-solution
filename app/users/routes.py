from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, session
from app import db, bcrypt
from app.models import User, Userreg, Agent
from flask_login import login_user, current_user, logout_user, login_required
from app.users.utils import save_picture, send_password_reset_email
from app.users.forms import LoginForm, RegistrationForm, UpdateAccountForm, ResetPasswordForm, RequestResetForm, UserForm, SearchAgentForm

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, phone=form.phone.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data} Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template("register.html", title='Register', form=form)


@users.route('/register_option', methods=['GET', 'POST'])
def register_option():
    return render_template("register_option.html")


@users.route('/register_user', methods=['GET', 'POST'])
def register_user():
  
    form = UserForm()
    if form.validate_on_submit():
        
        username = form.username.data
        email = form.email.data
        password = form.password.data
       
        
        use = Userreg(email=email, password=password, username=username)
        db.session.add(use)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template("register_user.html", form=form)



# search Agents button goes here 

@users.context_processor
def layout():
	form = SearchAgentForm()
	return dict(form=form)


 
@users.route('/searchagent', methods=["POST"])
def searchagent():
	form = SearchAgentForm()

	agent = Agent.query

	if form.validate_on_submit():
		# Get data from submitted form
		post.searched = form.searched.data
		# Query the Database
		agent = agent.filter(Agent.name.like('%' + post.searched + '%'))
		agent = agent.order_by(Agent.email).all()

		return render_template("searchagent.html",
		 form=form,
		 searched = post.searched,
		 agent = agent)



@users.route('/posts/<int:id>')
def post(id):
	user = Agent.query.get_or_404(id)
	return render_template('users.html', user=user)



@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Welcome to emax-solution.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('registartion unsuccessful.please check your Email and password', 'danger')
    return render_template('login.html', form=form)


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template("account.html", image_file=image_file, form=form)


@users.route("/delete_user/<int:user_id>/delete", methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if current_user.id != 2:
        abort(403)
    db.session.delete(user)
    db.session.commit()
    flash("the user has been deleted successfully", 'success')
    return redirect(url_for('admin.home'))
    return render_template("users.html", user=user)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@users.route('/reset_password', methods=['POST', 'GET'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route('/reset_password-<token>', methods=['POST', 'GET'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if not user:
        flash('Invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('your password has been updated!.', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
