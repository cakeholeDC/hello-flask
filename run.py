from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask</h1>'

@app.route('/cakehole')
def cakehole():
    return '<h1>CAKEHOLE</h1>'

@app.route('/cakehole/<username>')
def user(username):
    return "<h1>Hello, {}</h1>".format(username.upper())
    # return "<h1>Hello, {}</h1>".format(username[99])

@app.route('/lorem/<name>')
def lorem(name):
    n = name
    if n[-1] == "y":
        output = n[0:-1] + "iful"
    else:
        output = n + "y"
    
    return '<h1>Hi, {}!</h1>'.format(output)




if __name__ == '__main__':
    app.run(debug=True)