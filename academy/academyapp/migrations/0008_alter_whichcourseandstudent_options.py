# Generated by Django 4.0.1 on 2022-08-10 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academyapp', '0007_whichcourseandstudent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='whichcourseandstudent',
            options={'verbose_name': 'Kurs ve Öğrenci', 'verbose_name_plural': 'Kurslar ve Öğrenciler'},
        ),
    ]