from flask import Flask, request, session, redirect, url_for, render_template
from flask_mail import Mail, Message
from helpers import *
import message_strings
from tinydb import TinyDB, where
from validate_email import validate_email
import base64

from settings import *

app = Flask(__name__)
users = TinyDB('db/users.json')
app.config.from_object(__name__)
mail = Mail(app)

app.secret_key = 'Q\xfd\n-r\x13V#_\x84\xbc>\x90ck\xb3\x83\xcaw\x81 \xaby7'

api_key = "u_wot_m8"

@app.route("/", methods=['GET'])
def home():
	# action="email-sent"
	action = request.args.get('action', '')
	error = request.args.get('error', '')
	action_text = ""
	error_text = ""
	if action:
		if action == 'email-sent':
			action_text = message_strings.signup_email_sent
	if 'username' in session:
		# logged in!
		return render_template('home.html', session=session, error_text=error, action_text=action, emails=get_email_lists())
	else:
		return render_template('home.html', error_text=error_text, action_text=action_text)

@app.route("/confirm/", methods=['GET'])
def confirm():
	code = request.args.get('code', '')
	username = request.args.get('username', '')
	print("Code: " + code)
	print("username: " + username)
	if code:
		c = get_confirm_by_username(username)
		if c:
			if c == code:
				print("confirming")
				confirm_user(username)
				print("redirecting...")
				return redirect(url_for('login', action="confirmed"))
	else:
		return redirect(url_for('home'))

@app.route("/login/", methods=['GET', 'POST'])
def login():
	# action="confirmed"
	# error="username"
	# error="email"
	print("reached login with method " + request.method)
	action = request.args.get('action', '')
	error = request.args.get('error', '')
	action_text = ""
	error_text = ""

	if 'username' in session:
		return redirect(url_for('home'))
	if action:
		if action == 'confirmed':
			action_text = message_strings.signup_account_confirmed
	if error:
		if error == 'username':
			error_text = message_strings.signup_username_taken
		if error == 'email':
			error_text = message_strings.signup_email_taken

	if request.method == 'GET':
		return render_template('login.html', action_text=action_text, error_text=error_text)

	if request.method == 'POST':
		if (not 'username_or_email' in request.form) or (not 'password' in request.form):
			# login failed - incomplete form
			return render_template('login.html', error_text=message_strings.login_incomplete_form)
		usr = get_user_by_username(request.form['username_or_email'])
		if not usr:
			if validate_email(request.form['username_or_email']):
				usr = get_user_by_email(request.form['username_or_email'])
		if usr:
			if usr['password'] == base64.b64encode(request.form['password']):
				session['username'] = usr['username']
				return redirect(url_for('home'))

		return render_template('login.html', error_text=message_strings.login_failed)
	else:
		abort(405)

	return redirect(url_for('home'))

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
	err = request.args.get('error')
	if 'username' in session:
		return redirect(url_for('home'))
	if request.method == 'GET':
		return render_template('signup.html', error=0)

	if request.method == 'POST':
		print("posting new user...")
		print(request.form)
		if (not request.form['username']) or \
		   (not request.form['password']) or \
		   (not request.form['passwordconfirm']) or \
		   (not request.form['email']):
			print("0")
			# login failed - incomplete form
			return render_template('signup.html', error_text=message_strings.signup_incomplete_form)
		if (valid_email(request.form['email']) == -1):
			# not an email
			return render_template('signup.html', error_text=message_strings.signup_invalid_email)
		if (valid_email(request.form['email']) == 0):
			# not a college email
			return render_template('signup.html', error_text=message_strings.signup_invalid_email)
		if request.form['password'] != request.form['passwordconfirm']:
			print("1")
			# login failed - passwords do not match
			return render_template('signup.html', error_text=message_strings.signup_mismatched_passwords)
		confirm = generate_random_string()
		worked = save_new_user(request.form['username'], base64.b64encode(request.form['password']), \
							request.form['email'], confirm , 0)
		if worked == -2:
			print("username already in use!")
			return redirect(url_for('login', error="username"))
		if worked == -1:
			print("email already in use!")
			return redirect(url_for('login', error="email"))
		if worked > 0:
			print("saved successfully")
			session['user'] = {
				"username": request.form['username'],
		   		"email": request.form['email']
		  	}
		  	send_confirm_email(confirm, mail, request.form['username'], request.form['email'])
			return redirect(url_for('home', action="email-sent"))
		else:
			# login failed - that username is already taken
			return render_template('signup.html', error_text=message_strings.signup_username_taken)
	else:
		abort(405)
	return redirect(url_for('home'))

@app.route("/logout/", methods=['POST'])
def logout():
	if request.method == 'POST':
		if 'username' in session:
			session.pop('username', None)
	return redirect(url_for('home'))

@app.route("/api/", methods=['GET'])
def api():
	key = request.args.get('api_key', '')
	if key == api_key:
		pass


if __name__ == "__main__":
    app.run(debug = True)


