import sys 
sys.path.append("src")

from Model.calculadora_model import CalculadoraPensionalModel
from Model.Parameters import ParametrosPension
from Model.Exceptions import *
import SecretConfig
import psycopg2

class UsuarioBuscadoError(Exception):
    pass

class UsuarioActualizadoError(Exception):
    pass

class UsuarioCreadoError(Exception):
    pass

class UsuarioBorradoError(Exception):
    pass


def ObtenerCursor():
    """
    Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones
    """
    DATABASE = SecretConfig.PGDATABASE
    USER = SecretConfig.PGUSER
    PASSWORD = SecretConfig.PGPASSWORD
    HOST = SecretConfig.PGHOST
    PORT = SecretConfig.PGPORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()

def CrearTabla():
    """
    Crea la tabla de usuarios, en caso de que no exista
    """    
    sql = ""
    with open("sql/crear-usuarios.sql","r") as f:
        sql = f.read()

    cursor = ObtenerCursor()
    try:
        cursor.execute( sql )
        cursor.connection.commit()
    except:
        # SI LLEGA AQUI, ES PORQUE LA TABLA YA EXISTE
        cursor.connection.rollback()

def BorrarFilas():
    """
    Borra todas las filas de la tabla (DELETE)
    ATENCION: EXTREMADAMENTE PELIGROSO.

    Si lo llama en produccion, pierde el empleo
    """
    sql = "Delete from usuarios;"
    cursor = ObtenerCursor()
    cursor.execute( sql )

    # Crear nuevo usuario
def create_user(Usuario: ParametrosPension):
    try:
        query = """
        INSERT INTO usuarios (nombre, edad, salario_actual, semanas_laboradas, ahorro_pensional, tasa_administracion, rentabilidad_promedio, genero)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (Usuario.name, Usuario.age, Usuario.current_salary, Usuario.weeks_worked, Usuario.current_pension_savings, Usuario.management_rate, Usuario.average_return, Usuario.gender.upper())
        cursor = ObtenerCursor()
        
        calculadora = CalculadoraPensionalModel(Usuario)    
        calculadora.calculate_expected_pension_savings()
        cursor.execute(query, values)
        cursor.connection.commit()
    except:
        raise UsuarioCreadoError(f"El usuario con el nombre: {Usuario.name}, no se pudo crear")
    # Leer usuario
def brows_user(user_id):
    try:
        query = f"SELECT nombre, edad, salario_actual, semanas_laboradas, ahorro_pensional, tasa_administracion, rentabilidad_promedio, genero FROM usuarios WHERE id = '{user_id}'"
        cursor = ObtenerCursor()
        cursor.execute(query)
        lista = cursor.fetchone()
        usuario_buscado = ParametrosPension()
        usuario_buscado.name = lista[0]
        usuario_buscado.age = lista[1]
        usuario_buscado.current_salary = lista[2]
        usuario_buscado.weeks_worked = lista[3]
        usuario_buscado.current_pension_savings = lista[4]
        usuario_buscado.management_rate = lista[5]
        usuario_buscado.average_return = lista[6]
        usuario_buscado.gender = lista[7]
        return usuario_buscado
    except:
        raise UsuarioBuscadoError(f"El usuario buscado no se ha encontrado")
        

    # Actualizar usuario
def update_user(Usuario: ParametrosPension, user_id:str):
    try:
        cursor = ObtenerCursor()
        query = f"UPDATE usuarios SET nombre = '{Usuario.name}', edad = '{Usuario.age}', salario_actual = '{Usuario.current_salary}', semanas_laboradas = '{Usuario.weeks_worked}', ahorro_pensional = '{Usuario.current_pension_savings}', tasa_administracion = '{Usuario.management_rate}', rentabilidad_promedio = '{Usuario.average_return}', genero = '{Usuario.gender}'  WHERE id = '{user_id}';"
        cursor.execute(query)
        cursor.connection.commit()
        return f"El usuario con el id: {user_id} se ha actualizado correctamente"
    except:
        raise UsuarioActualizadoError(f"El usuario con el id: {user_id}, no se encontro")

    # Eliminar usuario
def delete_user(user_id):
    cursor = ObtenerCursor()
    query = f"DELETE FROM usuarios WHERE id = {user_id}"
    cursor.execute(query)
    cursor.connection.commit()
