from distutils.core import setup

setup(
    name='singlemodeladmin',
    packages=['singlemodeladmin'],
    version='0.8',
    description='ModelAdmin for models that are meant to have one record',
    author='Alexander Meng',
    author_email='alexbmeng@gmail.com',
    url='https://github.com/AMeng/django-single-model-admin',
    keywords=['django', 'model', 'admin'],
    install_requires=[
        'Django>=1.4'
    ],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ]
)
