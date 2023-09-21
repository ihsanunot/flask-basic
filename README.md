Run :

```
flask --app main run (nama main sesuai file nya)
```

Install :
```
pip install python-dotenv
```

Contoh Routing:

```
@app.route('/profile/<username>')
def profile_name(username):
    return '<h1>Hello %s!</h1>' % username
```

yang <username> adalaha parameter yang di lempar ke fungsi def profile_name(username)

HTTP Request & Method

Testing Get:

```
request.args.get('nama') + request.args.get('alamat')
```

Hasil:
http://127.0.0.1:5000/cobarequest/?nama=ayana&alamat=bandung

tinggal rubah ayana dan bandung nya saja.

Untuk method post ada di cobapost.py tapi jangan lupa :
```
pip install requests
```

Pastikan buka 2 terminal untuk GET dan POST nya.

Jangan lupa untuk pakai method post dan juga
jangan lupa pakai key nya.

Contoh:
```
request.form[namakey]
```

testing run di cobapost.py