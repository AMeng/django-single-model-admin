from distutils.core import setup

setup(
  name = 'django-single-model-admin',
  packages = ['django-single-model-admin'],
  version = '0.1',
  description = 'ModelAdmin for models that are meant to have one record',
  author = 'Alexander Meng',
  author_email = 'alexbmeng@gmail.com',
  url = 'https://github.com/AMeng/django-single-model-admin',
  download_url = 'https://github.com/AMeng/django-single-model-admin/tarball/0.1',
  keywords = ['django', 'model', 'admin'],
  install_requires=[
    'Django>=1.4'
  ]
)
