from setuptools import setup, find_packages

setup(
    name='sandbox',
    version='0.0.5.1',
    description='A collection of commonly used basic codes.',
    url='https://github.com/MoonsRainbow/sandbox.git',
    author='MoonsRainbow',
    author_email='Moons_Rainbow@kakao.com',
    license='MoonsRainbow',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pymysql == 1.0.2'
    ]
)