from setuptools import find_packages, setup


setup(
    name='my_pkg',
    version='1.0',
    packages=find_packages(include=['my_pkg', 'my_pkg.*']),
    install_requires=[
        'requests',
        'shapely',
    ],
)
