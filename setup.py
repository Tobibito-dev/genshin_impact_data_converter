from setuptools import setup, find_packages

setup(
    name='gidm',
    version='3.2.0',
    license='MIT',
    author='Tobibito-dev',
    author_email='tobibito.dev@gmail.com',
    packages=find_packages('src'),
    package_dir={'', 'src'},
    url='https://github.com/Tobibito-dev/genshin_impact_data_manager',
    keywords='gidm',
    install_requires=['setuptools']
)
