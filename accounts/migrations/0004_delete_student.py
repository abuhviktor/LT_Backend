# Generated by Django 3.2.12 on 2022-02-14 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_student_faculty'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
