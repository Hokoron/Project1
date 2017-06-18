from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from model.dbClass import dbClass
import pygal
import os

app = Flask(__name__)
weelradius = '0'
password = ''
username = ''

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/registreren')
def regestreren():
    if not session.get('registratie'):
        return render_template('registratie.html')
    else:
        session['registratie'] = False
        return home()

@app.route('/login', methods=['POST'])
def do_admin_login():
    data = dbClass()
    try:
        datafinal = data.getinfo(request.form['username'])[0]
    except:
        datafinal = (None,)
    if(request.form['password'] ==datafinal[0]):
        session['logged_in'] = True
    else:
        print('wrong password!')
        session['logged_in'] = False
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/registratie', methods=['POST'])
def do_admin_registratie():
    data = dbClass()
    data2 = dbClass()
    try:
        datafinal = data.getuser(request.form['username'])[0]
    except:
        datafinal = ('',)
    if request.form['password'] == '' or request.form['username'] == ''or request.form['weelradius'] == '':
        session['registratie'] = False
    elif(request.form['username'] == datafinal[0]):
        print("username taken")
        session['registratie'] = False
    else:
        data2.saveinfo(request.form['username'],request.form['password'],str(request.form['weelradius']))
        session['registratie'] = True
    return regestreren()

@app.route('/distance')
def distance():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        data = dbClass()
        lijst = data.getafstand()
        newlijst = []
        for item in lijst:
            newlijst.append(item[0])
        data2 = dbClass()
        lijst2 = data2.getdate()
        newlijst2 = []
        for item in lijst2:
            newlijst2.append(item[0])
        graph = pygal.Line()
        graph.title = 'afstand afgeleged '
        graph.x_labels = newlijst2
        graph.add('afstand', newlijst)
        graph_data = graph.render_data_uri()
        return render_template("distence.html", graph_data=graph_data)

@app.route('/time')
def time():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        data = dbClass()
        lijst = data.getgeredetijd()
        newlijst = []
        for item in lijst:
            newlijst.append(item[0])
        data2 = dbClass()
        lijst2 = data2.getdate()
        newlijst2 = []
        for item in lijst2:
            newlijst2.append(item[0])
        data3 = dbClass()
        lijst3 = data3.getdodetijd()
        newlijst3 = []
        for item in lijst3:
            newlijst3.append(item[0])

        graph = pygal.Line()
        graph.title = 'tijd afgelegd en stilgestaan '
        graph.x_labels = newlijst2
        graph.add('geredentijd', newlijst)
        graph.add('gepauzeerdetijd', newlijst3)
        graph_data = graph.render_data_uri()
        return render_template("time.html", graph_data=graph_data)

@app.route('/acount')
def acount():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
            return render_template('acount.html')

@app.route('/changepassword', methods=['POST'])
def changepassword():
    data = dbClass()
    data2 = dbClass()
    try:
        datafinal = data.getinfo(request.form['username'])[0]
    except:
        datafinal = (None,)
    if (request.form['password'] == datafinal[0]):
        data2.changepass(request.form['username'],request.form['re_password'])
    return acount()

@app.route('/changeusername', methods=['POST'])
def changeusername():
    data = dbClass()
    data2 = dbClass()
    try:
        datafinal = data.getinfo(request.form['username'])[0]
    except:
        datafinal = (None,)
    if (request.form['password'] == datafinal[0]):
        data2.changename(request.form['username'], request.form['new_username'])
    return acount()

@app.route('/changeweelsize', methods=['POST'])
def changeweelsize():
    data = dbClass()
    data2 = dbClass()
    try:
        datafinal = data.getinfo(request.form['username'])[0]
    except:
        datafinal = (None,)
    if (request.form['password'] == datafinal[0]):
        data2.changeweel(request.form['username'], request.form['new_weel'])
    return acount()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host="169.254.10.11")

#https://stocksnap.io/photo/HV3XMBMNL1