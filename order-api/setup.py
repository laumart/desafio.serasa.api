from setuptools import find_packages, setup

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='order_api',
    version='1.0',
    author='Laudinei Martins',
    license='MIT',
    description='Order-API',
    long_description='Micro-Service for Orders using Fastapi',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)