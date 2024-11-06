import sys 
sys.path.append("src")

from Model.calculadora_model import CalculadoraPensionalModel, calculate_expected_pension_savings
from Model.Exceptions import *

class CalculadoraPensionalController:
    def __init__(self):
        self.model = CalculadoraPensionalModel()

    # Crear nuevo usuario
    def create_user(self, nombre, edad, salario_actual, semanas_laboradas, ahorro_pensional, tasa_administracion, rentabilidad_promedio, genero):
        query = """
        INSERT INTO usuarios (nombre, edad, salario_actual, semanas_laboradas, ahorro_pensional, tasa_administracion, rentabilidad_promedio, genero)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (nombre, edad, salario_actual, semanas_laboradas, ahorro_pensional, tasa_administracion, rentabilidad_promedio, genero)
        
        # Utilizamos el método `calculate_expected_pension_savings` para realizar cálculos de pensión en el modelo.
        parameters = {
            "age": edad,
            "current_salary": salario_actual,
            "weeks_worked": semanas_laboradas,
            "current_pension_savings": ahorro_pensional,
            "management_rate": tasa_administracion,
            "average_return": rentabilidad_promedio,
            "gender": genero
        }
        try:
            expected_savings = calculate_expected_pension_saving(parameters)
            print("Ahorro pensional esperado:", expected_savings)  # O bien, guardar este valor en la base de datos
            self.model.cursor.execute(query, values)
            self.model.connection.commit()
        except Exception as e:
            raise DatabaseError("Error al calcular el ahorro pensional esperado o guardar el usuario") from e

    # Leer usuario
    def read_user(self, user_id):
        query = "SELECT * FROM usuarios WHERE id = %s"
        self.model.cursor.execute(query, (user_id,))
        return self.model.cursor.fetchone()

    # Actualizar usuario
    def update_user(self, user_id, **kwargs):
        fields = ", ".join([f"{key} = %s" for key in kwargs.keys()])
        values = list(kwargs.values()) + [user_id]
        query = f"UPDATE usuarios SET {fields} WHERE id = %s"
        self.model.cursor.execute(query, tuple(values))
        self.model.connection.commit()

    # Eliminar usuario
    def delete_user(self, user_id):
        query = "DELETE FROM usuarios WHERE id = %s"
        self.model.cursor.execute(query, (user_id,))
        self.model.connection.commit()

    def close_connection(self):
        self.model.close_connection()  # Cerrar la conexión a la base de datos
