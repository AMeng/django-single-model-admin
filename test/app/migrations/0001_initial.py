from __future__ import unicode_literals
from django.db import models, migrations


class Migration(migrations.Migration):
    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('field', models.CharField(max_length=25))
            ],
            bases=(models.Model,)
        )
    ]
