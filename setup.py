from setuptools import setup, find_packages

setup(
    name="nombre_del_paquete",  # Cambia el nombre según lo necesites
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
