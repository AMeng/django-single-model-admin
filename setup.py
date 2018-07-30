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
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django :: 1.4",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ]
)
