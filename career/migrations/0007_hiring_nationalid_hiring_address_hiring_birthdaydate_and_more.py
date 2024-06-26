# Generated by Django 5.0.3 on 2024-03-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0006_remove_hiring_nationalid_remove_hiring_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiring',
            name='NationalId',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='National Id'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='birthdayDate',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birthday'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='fatherName',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Father Name'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='fileUpload',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hiring',
            name='marriageSituate',
            field=models.CharField(blank=True, choices=[('SN', 'Single'), ('MR', 'Married')], max_length=50, null=True, verbose_name='Married Situate'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Mobile Phone'),
        ),
        migrations.AlterField(
            model_name='hiring',
            name='firstName',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='hiring',
            name='lastName',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Last Name'),
        ),
    ]