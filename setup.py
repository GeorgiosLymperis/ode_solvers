from setuptools import setup, find_packages

setup(
    name='ode_solvers',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
    ],
    author='Giorgos Lymberis',
    description='A collection of ODE solvers implemented in Python',
)