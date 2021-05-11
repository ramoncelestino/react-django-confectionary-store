# Generated by Django 3.2.2 on 2021-05-11 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('complement', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveredAt', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('totalPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('valuePaid', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.city')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.neighborhood'),
        ),
    ]
