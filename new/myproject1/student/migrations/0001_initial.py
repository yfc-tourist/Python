# Generated by Django 2.2.1 on 2019-05-14 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('createCounttime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studentinfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=3)),
                ('gendle', models.BooleanField()),
                ('classes', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('result', models.FloatField()),
                ('stuid', models.ForeignKey(on_delete='CASCADE', to='student.Userinfo')),
            ],
        ),
    ]