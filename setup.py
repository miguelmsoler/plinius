from setuptools import setup, find_packages

setup(
    name='plinius',
    version='0.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'plinius=plinius.main:main',
        ],
    },
    # TODO: Otras configuraciones como author, description, etc.
)
