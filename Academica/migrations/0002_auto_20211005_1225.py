# Generated by Django 3.2.7 on 2021-10-05 12:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='cogido',
            new_name='codigo',
        ),
        migrations.AddField(
            model_name='matriculas',
            name='curso',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='Academica.cursos'),
            preserve_default=False,
        ),
    ]
