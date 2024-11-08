import sys
sys.path.append("src")
from flask import Flask, request    
from flask import render_template
from Controller.calculadora_controller import create_user, UsuarioCreadoError, update_user, UsuarioActualizadoError, delete_user, UsuarioBorradoError, brows_user, UsuarioBuscadoError
from Model.Parameters import ParametrosPension

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
@app.route('/')      
def hello():
    return render_template("index.html")

@app.route('/insertar')
def insertar():
    return render_template("insertar.html")

@app.route('/insertado')
def insertado():
    Parametros = ParametrosPension()
    Parametros.name = request.args["name"] 
    Parametros.age = int(request.args["age"])  
    Parametros.gender = request.args["gender"]  
    Parametros.current_salary = float(request.args["current_salary"])  
    Parametros.weeks_worked = int(request.args["weeks_worked"]) 
    Parametros.current_pension_savings = float(request.args["current_pension_savings"])
    Parametros.average_return = float(request.args["average_return"])  
    Parametros.management_rate = float(request.args["management_rate"])
    try:
        create_user(Parametros)
        return f"El usuario {Parametros.name} ha sido creado exitosamente "
    except:
        raise UsuarioCreadoError(f"El usuario {Parametros.name} no se ha creado")
    


@app.route('/actualizar')
def actualizar():
    return render_template("actualizar.html")

@app.route('/actualizado')
def actualizado():
    id = request.args["ID"]
    Parametros = ParametrosPension()
    Parametros.name = request.args["name"] 
    Parametros.age = request.args["age"] 
    Parametros.gender = request.args["gender"].upper() 
    Parametros.current_salary = request.args["current_salary"] 
    Parametros.weeks_worked = request.args["weeks_worked"] 
    Parametros.current_pension_savings = request.args["current_pension_savings"]
    Parametros.average_return = request.args["average_return"]
    Parametros.management_rate = request.args["management_rate"]
    try:
        update_user(Parametros, id)
        return f"El usuario {Parametros.name} ha sido actualizado exitosamente "
    except:
        raise UsuarioActualizadoError(f"El usuario con el id: {id} no se ha actualizado")

@app.route('/borrar')
def borrar():
    return render_template("borrar.html")

@app.route('/borrado')
def borrado():
    id = request.args["ID"]
    try:
        delete_user(id)
        return f"El usuario con el id {id}, se ha borrado exitosamente"
    except:
        raise UsuarioBorradoError(f"El usuario con el id: {id}, no se ha borrado o no existe")

@app.route('/buscar')
def buscar():
    return render_template("buscar.html")

@app.route('/buscado')
def buscado():
    id = request.args["ID"]
    try:
        Usuario = brows_user(id)
        return f"El nombre del usuario es: {Usuario.name} la edad es: {Usuario.age} genero: {Usuario.gender} el salario es: {Usuario.current_salary}, semanas trabajadas: {Usuario.weeks_worked}, pension actual: {Usuario.current_pension_savings}, Tasa de administracion: {Usuario.average_return}, rentabilidad promedio {Usuario.average_return} "
    except:
        raise UsuarioBuscadoError(f"Error el usuario con el id {id} no fue encontrados")
        
# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run(debug= True)