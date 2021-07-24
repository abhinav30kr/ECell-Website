# Generated by Django 3.1.2 on 2021-07-23 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('roll_number', models.CharField(max_length=6)),
                ('phone', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ManagementTeamRecs',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recruitment.contactinfo')),
                ('answer1', models.TextField(max_length=3000)),
                ('answer2', models.TextField(max_length=3000)),
                ('answer3', models.TextField(max_length=3000)),
            ],
            bases=('recruitment.contactinfo',),
        ),
        migrations.CreateModel(
            name='MediaTeamRecs',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recruitment.contactinfo')),
                ('area_of_interest', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('answer1', models.TextField(max_length=3000)),
                ('answer2', models.TextField(max_length=3000)),
                ('answer3', models.TextField(max_length=3000)),
            ],
            bases=('recruitment.contactinfo',),
        ),
        migrations.CreateModel(
            name='WebTeamRecs',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recruitment.contactinfo')),
                ('area_of_interest', models.IntegerField(choices=[('Frontend', 1), ('Backend', 2), ('Both', 0)])),
                ('skills', models.CharField(max_length=200)),
                ('answer1', models.TextField(max_length=3000)),
                ('answer2', models.TextField(max_length=3000)),
                ('answer3', models.TextField(max_length=3000)),
            ],
            bases=('recruitment.contactinfo',),
        ),
    ]