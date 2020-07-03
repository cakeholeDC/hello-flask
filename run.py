from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # return '<h1>Hello Flask</h1>'
    return render_template('home.html')

@app.route('/users/')
def users():
    users = ["cakehole", "sally", "jim"]
    return render_template("users.html", users=users)

@app.route('/users/<username>')
def user(username):
    letters = list(username)
    dict = {
        "name":username,
    }

    user_logged_in = True
    return render_template('profile.html', 
                user_logged_in=user_logged_in,
                username=username, 
                time=datetime.utcnow(),
                letters=letters, 
                dict=dict, 
                )

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thank_you.html', first=first, last=last)

@app.route('/login')
def login():
    valid_users = ["cakehole", "sally", 'jim']
    username = request.args.get('username')
    if username in valid_users:
        return render_template('profile.html', username=username, time=datetime.utcnow())
    else:
        return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
