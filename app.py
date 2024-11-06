import sys
sys.path.append("src")
from Model.calculadora_model import CalculadoraPensionalModel
from Model.Parameters import ParametrosPension
from flask import Flask    
from flask import render_template, request
import math

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
@app.route('/')      
def hello():
    return render_template("Formulario.html")

@app.route('/calcular_pension')
def calcular_pension():
    parameters = ParametrosPension()
    parameters.age = int(request.args["age"]) 
    parameters.gender = request.args["gender"] 
    parameters.current_salary = int(request.args["current_salary"]) 
    parameters.weeks_worked = int(request.args["weeks_worked"]) 
    parameters.current_pension_savings = int(request.args["current_pension_savings"]) 
    parameters.average_return = int(request.args["average_return"]) 
    parameters.management_rate = int(request.args["management_rate"])
    calcular = CalculadoraPensionalModel(parameters)
    calcular.calculate_expected_pension_savings()
    total = calcular.expected_pension_savings
    return f"El valor de la pension es de: {math.ceil(total)} COP"


# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run()