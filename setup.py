from setuptools import setup

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='src',
    version="0.0.1",
    author='Priyank',
    description='A simple demonstration',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    url='https://github.com/priyanksms/DVCPrac',
    packages=['src'],
    python_requires='>=3.7',
    install_requires=[
        'dvc',
        'numpy',
        'pandas',
        'scikit-learn'
    ]
)

