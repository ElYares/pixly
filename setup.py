from setuptools import setup, find_packages

setup(
    name='pixly',
    version='0.1.0',
    description='Paquete para lectura y procesamiento de imágenes biomédicas con operaciones morfológicas y segmentación',
    author='Arturo Yared Elizondo Reigno',
    author_email='yared.elizondo.ingsoft@gmail.com',
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    python_requires='>=3.8',
)
