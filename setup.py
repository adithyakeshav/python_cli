from setuptools import setup
setup(
    name='PythonCli',
    version='1.0',
    packages=['get_serial_numbers'],
    entry_points={
        'console_scripts' : [
            'snum = get_serial_numbers.__main__:main'
        ]
    },
    python_requires = '>3.3'
)