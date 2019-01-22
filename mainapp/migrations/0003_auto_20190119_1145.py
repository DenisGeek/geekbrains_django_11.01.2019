# Generated by Django 2.1 on 2019-01-19 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190119_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, verbose_name='Product name')),
                ('image', models.ImageField(blank=True, upload_to='product.images')),
                ('descriptionShort', models.CharField(blank=True, max_length=60, verbose_name='Product short description')),
                ('description', models.TextField(blank=True, verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Product price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Product available in store')),
            ],
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='categoryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory'),
        ),
    ]
