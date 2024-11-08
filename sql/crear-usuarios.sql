CREATE TABLE usuarios (
    id Serial PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT CHECK (edad >= 18 AND edad <= 115),
    salario_actual DECIMAL(10, 2) CHECK (salario_actual >= 0),
    semanas_laboradas INT CHECK (semanas_laboradas >= 0),
    ahorro_pensional DECIMAL(10, 2) CHECK (ahorro_pensional >= 0),
    tasa_administracion DECIMAL(4, 2) CHECK (tasa_administracion >= 0 AND tasa_administracion <= 3),
    rentabilidad_promedio DECIMAL(4, 2) CHECK (rentabilidad_promedio >= 0 AND rentabilidad_promedio <= 3),
    genero CHAR(1) CHECK (genero IN ('M', 'F'))
);