# Generated by Django 2.1.3 on 2018-11-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_propertyimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('encryptedPassword', models.CharField(max_length=200)),
                ('salt', models.CharField(max_length=100)),
                ('UserAccountExpiryDate', models.DateField()),
                ('PasswordMustChanged', models.BooleanField()),
                ('PasswordReset', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PermissionType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('Read', 'Read'), ('Write', 'Write'), ('Delete', 'Delete'), ('Update', 'Update')], default='Read', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RoleCode',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.IntegerField()),
                ('sysFeature', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dateAssigned', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='propertycategory',
            name='PropertyCategory',
            field=models.CharField(choices=[('Single House', 'Single House'), ('Attached House', 'Attached House'), ('Town House', 'Town House'), ('Apartment', 'Apartment'), ('Store', 'Store'), ('Farm', 'Farm'), ('Factory', 'Factory'), ('Mall', 'Mall'), ('Building', 'Building'), ('Other', 'Other')], default='Single House', max_length=20),
        ),
        migrations.AlterField(
            model_name='propertyfacing',
            name='PropertyFacing',
            field=models.CharField(choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West'), ('Other', 'Other')], default='North', max_length=20),
        ),
        migrations.AlterField(
            model_name='propertyimages',
            name='propertyImageID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='propertysector',
            name='PropertySector',
            field=models.CharField(choices=[('Private', 'Private'), ('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Government', 'Government'), ('Rural', 'Rural'), ('Other', 'Other')], default='Private', max_length=20),
        ),
    ]
