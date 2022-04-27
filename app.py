from flask import Flask,redirect,url_for,render_template,request,session,flash
from flaskext.mysql import MySQL
from datetime import datetime
import  bcrypt
import  os
from flask import send_from_directory


app=Flask(__name__)
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='us-cdbr-east-05.cleardb.net'
app.config['MYSQL_DATABASE_USER']='bbb5aefdfc0734'
app.config['MYSQL_DATABASE_PASSWORD']='12784f39'
app.config['MYSQL_DATABASE_DB']='heroku_4e34d5e7db07c50'
mysql.init_app(app)

#conexion a las carpetas

carpeta=os.path.join('fotos')
app.config['carpeta']=carpeta
carpeta1=os.path.join('archivos')
app.config['carpeta1']=carpeta1
@app.route('/fotos/<foto>')
def fotos(foto):
    return send_from_directory(app.config['carpeta'],foto)
@app.route('/archivos/<archivo>')
def archivos(archivo):
    return send_from_directory(app.config['carpeta1'],archivo)

def consulta(sql,datos):
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    
#navegacion
@app.route("/")
def index(): 
    return render_template("paginas/index.html")

#login

@app.route("/registro")
def registro():
    return render_template("paginas/registro.html")
@app.route('/store',methods=['GET','POST'])
def storage():
    if request.method=='GET':
        return render_template("paginas/registro.html")
    else:
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        correo=request.form['correo']
        foto=request.files['foto']
        now=datetime.now()
        tiempo=now.strftime("%Y%H%M%S")
        if foto.filename!='':
            newnamefoto=tiempo+foto.filename
            foto.save('fotos/'+newnamefoto)
        pas=request.form['password'].encode('utf-8')
        pas_encry=bcrypt.hashpw(pas,bcrypt.gensalt())
        datos=(nombre,apellido,correo,newnamefoto,1,pas_encry,)
     
        sql="INSERT INTO viewers (id, nombre, apellido, correo, foto, tipo,contraseña) VALUES (NULL, %s, %s, %s, %s, %s,%s)"
        consulta(sql,datos)
        return render_template('paginas/index.html')
@app.route('/login')
def login():
    return render_template("paginas/login.html")
@app.route('/singin',methods=["GET","POST"])
def sing_in():
    if request.method=='POST':
        correo=request.form['correo']
        pas=request.form['contraseña'].encode('utf-8')
     
        sql="SELECT*FROM viewers WHERE correo=%s"
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute(sql,(correo,))
        user=cursor.fetchone()
        
        conn.close()
        if (user!=None):
            if bcrypt.hashpw(pas,user[6].encode('utf-8'))==user[6].encode('utf-8'):
                session['correo']=correo
                session['nombre']=user[1]
                session['foto']=user[4]
                if user[5]==2:
                    return redirect(url_for('codigos_admin'))
                elif user[5]==1:
                    return redirect(url_for('codigos'))
            else:
                flash("Error, contraseña o correo incorrecto",'alert-marning')
                return render_template("paginas/login.html")
        else:
            flash("El correo no existe,Registrate",'alert-warning')
            return render_template("paginas/login.html")
    else:
        return render_template("paginas/login.html")     
@app.route('/salir')
def salir():
    session.clear()
    return redirect(url_for('login'))
@app.route('/codigos')
def codigos():
    sql="SELECT*FROM codigos"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    codigos=cursor.fetchall()
    conn.commit()
    return render_template("paginas/codigos_usuario.html",codigos=codigos)
@app.route('/codigos_admin')
def codigos_admin():
    sql="SELECT*FROM codigos"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    codigos=cursor.fetchall()
    conn.commit()
    return render_template("paginas/codigos_admin.html",codigos=codigos)
@app.route('/add',methods=['POST'])
def add():
  
    nombre=request.form['nombre']
    archivo=request.files['archivo']
    now=datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    if archivo.filename!='':
        newnamearchivo=tiempo+archivo.filename
        archivo.save('archivos/'+newnamearchivo)
    datos=(nombre,newnamearchivo)
    sql="INSERT INTO codigos (id, nombre, archivo) VALUES (NULL, %s, %s)"
    consulta(sql,datos)
    return redirect(url_for('codigos_admin'))
@app.route('/agregar')
def agregar():
    return render_template("paginas/registra_archivos.html")

if __name__ == '__main__':
    app.secret_key="^A%DJAJU^JJ123"
    app.run(port=5000,debug=True)