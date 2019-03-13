# -*- coding: iso-8859-15 -*-

from flask import Flask , request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index_ini.html')


@app.route('/home', methods=['GET'])
def inicio():
    return app.send_static_file('home_ini.html')


@app.route('/login', methods=['GET'])
def entrar():
    return app.send_static_file('login.html')


@app.route('/signup', methods=['GET'])
def registrarse():
    return app.send_static_file('signup_ini(1).html')


@app.route('/processLogin', methods=['GET', 'POST'])
def processLogin():
       missing = []
       fields = ['email', 'passwd', 'login_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None:
                  missing.append(field)
       if missing:
              return "Falta completar algunos campos"


       return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<title> Inicio - Me doy maña </title>' \
           '</head>' \
           '<body> <div id ="container">' \
		   '<a href="/"> Me doy maña </a> | <a href="home"> Inicio </a> | <a href="login"> Entrar </a> | <a href="signup"> Registrarse </a>' \
           '<h1>Data from Form: Login</h1>' \
	       '<form><label>email: ' + request.form['email'] + \
	       '</label><br><label>passwd: ' + request.form['passwd'] + \
           '</label></form></div></body>' \
           '</html>'


@app.route('/processSignup', methods=['GET', 'POST'])
def processSignup():
       missing = []
       fields = ['name', 'lastname', 'doc','email', 'phone', 'passwd', 'repeat_passwd', 'birth_date', 'signup_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None:
                     missing.append(field)
       if missing:
              return "Debe llenar todos los espacios"

       return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<title> Inicio - Me doy maña </title>' \
           '</head>' \
           '<body> <div id ="container">' \
		   '<a href="/"> Me doy maña </a> | <a href="home"> Inicio </a> | <a href="login"> Entrar </a> | <a href="signup"> Registrarse </a>' \
           '<h1>Data from Form: Sign Up</h1>' \
           '<form><label>name: ' + request.form['name'] + \
	       '</label><br><label>email: ' + request.form['email'] + \
	       '</label><br><label>passwd: ' + request.form['passwd'] + \
	       '</label><br><label>confirm: ' + request.form['confirm'] + \
           '</label></form></div></body>' \
           '</html>'


@app.route('/processHome', methods=['GET', 'POST'])
def processHome():
	missing = []
	fields = ['publicacion', 'last', 'post_submit']
	for field in fields:
		value = request.form.get(field, None)
		if value is None:
			missing.append(field)
	if missing:
		return "Hay campos vacios"

	return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<title> Inicio - Me doy maña </title>' \
           '</head>' \
           '<body> <div id="container">' \
		   '<a href="/"> Me doy maña </a> | <a href="home"> Inicio </a> | <a href="login"> Entrar </a> | <a href="signup"> Registrarse </a>' \
           '<h1>Hola, qué servicio requieres?</h1>' \
                	'<form action="processHome" method="post" name="home"> ' \
			'<label for="publicacion">Describe lo que necesitas</label><div class="inputs">' \
			'<input id="publicacion" maxlength="140" name="publicacion" size="128" type="text" value=""/>' \
			'<input id="last" type="hidden" name="last" value="' + request.form['last'] + '<br>'+ request.form['publicacion'] + '">' \
	                 '</div>' \
                    	'<div class="inputs">' \
                        '<input id="post_submit" name="post_submit" type="submit" value="Post!"/>' \
           		'<br><br>Previous Posts: <br>' + request.form['last'] + '<br>' +request.form['publicacion'] + \
                	'</form>' \
            		'</div></div>' \
           '</body>' \
           '</html>'


#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, port=80)