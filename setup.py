from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='exotic_fruits',
    version=version,
    description='appp for managing exotic customization',
    author='Systematrix',
    author_email='kolate.sambhaji@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
