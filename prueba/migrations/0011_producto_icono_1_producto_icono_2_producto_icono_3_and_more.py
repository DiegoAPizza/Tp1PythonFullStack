# Generated by Django 4.2.7 on 2023-12-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0010_categoria_clase_css'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='icono_1',
            field=models.CharField(default='fa-solid fa-star', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='icono_2',
            field=models.CharField(default='fa-solid fa-heart', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='icono_3',
            field=models.CharField(default='fa-solid fa-star', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='icono_4',
            field=models.CharField(default='fa-solid fa-heart', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='icono_5',
            field=models.CharField(default='fa-solid fa-circle', max_length=50),
        ),
    ]
