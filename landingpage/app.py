from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html', user={'name':'', 'email':''})

@app.route('/contact/<string:code>', methods=['GET'])
def contactCode(code):
    if code == "1234":
        return render_template('contact.html', user={'name':'John Doe', 'email':'john@gmail.com'})
    else:
        return render_template('contact.html', user={'name':'', 'email':''})

if __name__ == '__main__':
    app.run(port=5000, debug=True)