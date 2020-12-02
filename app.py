from flask import Flask,flash,render_template,request,redirect,url_for,jsonify
from flaskext.mysql import MySQL

from forms import  RegistrationForm

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'flaskcontact'

mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    form = RegistrationForm(request.form)
    ction = mysql.connect()
    cur = ction.cursor()
    cur.execute('SELECT * FROM CONTACT')
    data = cur.fetchall()
    #print (data)
    return render_template('index.html',form=form,contacts=data)

@app.route('/add_contact', methods=["POST"])
def add_contact():
    if request.method == "POST":
        fullname = request.form ['fullname']
        phone = request.form ['phone']
        email = request.form ['email']
        ction = mysql.connect()
        cur = ction.cursor()
        cur.execute('INSERT INTO contact (fullname,phone,email) VALUES(%s,%s,%s)',
        (fullname,phone,email))
        ction.commit()
        flash ('Contact Added successfully')
    return redirect(url_for('index'))

@app.route('/edit/<id>')
def get_contact(id):
    ction = mysql.connect()
    cur = ction.cursor()
    cur.execute('SELECT * FROM CONTACT WHERE id = %s',(id))
    data = cur.fetchall()
    #print (data[0])

    return render_template('edit_contact.html',contact=data[0])

@app.route('/update/<id>', methods=["POST"])
def update_contact(id):
    if request.method == "POST":
        fullname = request.form ['fullname']
        phone = request.form ['phone']
        email = request.form ['email']
        ction = mysql.connect()
        cur = ction.cursor()
        cur.execute ("UPDATE CONTACT  SET fullname=%s,email=%s, phone=%s  WHERE id=%s " ,(fullname,email,phone,id))
        ction.commit()
        flash ('Contact Updated successfully')
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    ction = mysql.connect()
    cur = ction.cursor()
    cur.execute('DELETE FROM CONTACT WHERE id = {0}'.format(id))
    ction.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))  

# Funciones en formato json para manejar desde Postman  

@app.route('/create_Contact', methods=['POST'])
def create_Contact():

    fullname = request.json['fullname']
    phone = request.json ['phone']
    email = request.json ['email']

    ction = mysql.connect()
    cur = ction.cursor()
    cur.execute('INSERT INTO contact (fullname,phone,email) VALUES(%s,%s,%s)',(fullname,phone,email))
    ction.commit()
    
    return jsonify({"menssage":"Contacto agregado satisfactoriamente"})

@app.route('/list_contact',methods=['GET'])
def get_list():
    ction = mysql.connect()
    cur = ction.cursor()
    cur.execute('SELECT * FROM CONTACT')
    data = cur.fetchall()
    
    return jsonify(contacts=data) 

@app.route('/contact/<id>',methods=['GET'])
def contact(id):   
    ction = mysql.connect()
    cur = ction.cursor()
    cur.execute('SELECT * FROM CONTACT WHERE id = %s',(id))
    data = cur.fetchall()
    
    return jsonify(contact=data[0]) 

@app.route('/update/<id>',methods=['PUT']) 
def update(id):
    
    fullname = request.json ['fullname']
    phone = request.json ['phone']
    email = request.json ['email']
    ction = mysql.connect()
    cur = ction.cursor()
    cur.execute ("UPDATE CONTACT  SET fullname=%s,email=%s, phone=%s  WHERE id=%s " ,(fullname,email,phone,id))
    ction.commit()
    return  jsonify({"menssage":"Contacto modificado satisfactoriamente"})

@app.route('/remove/<string:id>',methods=['DELETE'])
def remove(id):
    ction = mysql.connect()
    cur = ction.cursor()
    cur.execute('DELETE FROM CONTACT WHERE id = {0}'.format(id))
    ction.commit()
    
    return  jsonify({"menssage":"Contacto eliminado satisfactoriamente"})

if __name__ == "__main__":
   app.run(debug=True)
     