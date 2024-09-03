from Test import Test_Error 
from src.Logic import Parameters


def verificarEdad(edad):
    if edad < 18 or edad > 115:
        raise Test_Error.EdadError(f"Su edad la cual es: {edad} debe ser mayor a 18 y menor a 115")


def verificarSalarioActual(salario_actual):
    if salario_actual < 0:
        raise Test_Error.SalarioActualNegativoError(f"Su salario el c ual es: {salario_actual} debe ser mayor a 0")
    

def verificarSemanasLaboradas(semanas_laboradas):
    if semanas_laboradas < 0:
        raise Test_Error.SemanasLaboradasNegativasError(f"Las semanas laboradas las cuales son: {semanas_laboradas} deben ser mayores a 0")


def verificarTasaAdministracion(tasa_administracion):
    if tasa_administracion < 0 or tasa_administracion > 3:
        raise Test_Error.TasaAdministracionError(f"La tasa de administración la cual es: {tasa_administracion} debe ser mayor a 0 y menor a 3")


def verificarAhorroPensional(ahorro_pensional_a_hoy):
    if ahorro_pensional_a_hoy < 0:
        raise Test_Error.AhorroPensionalNegativoError(f"El ahorro pensional a hoy el cual es: {ahorro_pensional_a_hoy} debe ser mayor a 0")


def verificarRentabilidadPromedio(rentabilidad_promedio):
    if rentabilidad_promedio < 0:  # revisar este caso
        raise Test_Error.RentabilidadPromedioNegativaError(f"La rentabilidad promedio las cuales son: {rentabilidad_promedio} debe ser mayor que 0")


def calcularAhorroPensionalEsperado(parametros):
    verificarEdad(parametros.edad)
    verificarSalarioActual(parametros.salario_actual)
    verificarSemanasLaboradas(parametros.semanas_laboradas)
    verificarAhorroPensional(parametros.ahorro_pencional_a_hoy)
    verificarRentabilidadPromedio(parametros.rentabilidad_promedio)
    verificarTasaAdministracion(parametros.tasa_administracion)

def calcularPensionEsperada():
    pass


