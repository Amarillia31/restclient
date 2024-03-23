from setuptools import setup
REQIRES = [
    'allure-pytest',
    'curlify',
    'requests',
    'structlog'
]

setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/Amarillia31/restclient.git',
    license='MIT',
    author='elena',
    author_email='-',
    install_requires=REQIRES,
    description='rest client with allure and logger'
)
