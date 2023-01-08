from setuptools import setup, find_packages

setup(
    name='sandbox',
    version='0.0.4',
    description='Commonly base codes.',
    url='https://github.com/MoonsRainbow/commonly_base.git',
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