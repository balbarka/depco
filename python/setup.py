# Databricks notebook source
from setuptools import setup, find_packages
  

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='depco',
      version='0.11',
      description='Depco Package Description',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 3.7.6',
        'Spark Distribution :: Databricks :: 7.3 LTS ML'
      ],
      keywords='CICD Pipeline Pytest',
      url='https://github.com/balbarka/depco',
      author='Brad Barker',
      author_email='brad.barker@databricks.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
          'pandas'],
      extras_require = {
          'databricks_provided':  ['pyspark',]},
      include_package_data=True,
      zip_safe=True)
