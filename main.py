from flask import Flask
from flask import escape
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    contohList = ['apple','mangga','jeruk']
    contohDic = {
        'nama':'Neno Balqis',
        'usia' : '27',
        'alamat' : 'Bogor'
    }
    return render_template('index.html', nama = 'Mona', umur = '28', list=contohList, dict=contohDic)

@app.route('/about/')
def about():
    return '<h1>About Me</h1>'

@app.route('/contact/')
def contact():
    return '<h1>Contact Me</h1>'

@app.route('/profile/')
def profile():
    return '<h1>Profile</h1>'

# @app.route('/profile/<username>')
# def profile_name(username):
#     return '<h1>Hello %s!</h1>' % username

@app.route('/profile/<int:nilai>/')
def profile_name(nilai):
    nilai = nilai + 20
    return '<h1>Contoh Angka Routing %s!</h1>' % nilai

@app.route('/htmlescape/<code>/')
def htmlescape(code):
    return escape(code)
    # return '<h3>Contoih HTML Escape %s' % code

@app.route('/cobarequest/', methods=['GET','POST'])
def cobaRequest():
    if request.method=='GET':
        return request.args.get('nama') + request.args.get('alamat')
    elif request.method=='POST':
        return request.form['nama']

app.run(debug=True)