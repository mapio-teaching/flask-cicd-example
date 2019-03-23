import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='flask-cicd-example',
    version='1.0.0',
    url='https://github.com/mapio-teaching/flask-cicd-example',
    license='BSD',
    maintainer='Massimo Santini',
    maintainer_email='santini@di.unimi.it',
    description='An example of CI/CD based on the flaskr app.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'gunicorn'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
