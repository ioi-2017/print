from setuptools import find_packages, setup

setup(
    name='ioiprint',
    version='0.9.0',
    description='A printing tool for IOI contest.',
    packages=find_packages(),
    install_requires=['Jinja2>=2.9.6'],
    python_requires='>=3.5',
    package_data={
        'ioiprint': ['template/*', 'static/*']
    },
    entry_points={
        'console_scripts': [
            'ioiprint = ioiprint.main:main'
        ]
    }
)
