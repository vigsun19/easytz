from setuptools import setup, find_packages

setup(
    name='easytz',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytz',
    ],
    description='A simple and efficient library for seamless time zone conversions — with built-in batch processing for handling multiple datetime objects effortlessly.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Vignesh Sundaram',
    author_email='vigneshanm@gmail.com',
    url='https://github.com/vigsun19/easytz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)