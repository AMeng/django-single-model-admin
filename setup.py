from distutils.core import setup

setup(
    name='singlemodeladmin',
    packages=['singlemodeladmin'],
    version='0.3',
    description='ModelAdmin for models that are meant to have one record',
    author='Alexander Meng',
    author_email='alexbmeng@gmail.com',
    url='https://github.com/AMeng/django-single-model-admin',
    keywords=['django', 'model', 'admin'],
    install_requires=[
        'Django>=1.4'
    ]
)
