from setuptools import setup, find_packages

setup(
    name="hello",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        'console_scripts': [
            'hello=hello.hello:main',
        ],
    },
)
