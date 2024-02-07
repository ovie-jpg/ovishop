# Generated by Django 5.0.1 on 2024-01-23 16:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_amount', models.IntegerField()),
                ('transfer_note', models.TextField(blank=True, null=True)),
                ('transfer_reference', models.CharField(blank=True, max_length=25, null=True)),
                ('recipient_code', models.CharField(blank=True, max_length=25, null=True)),
                ('bank_slug', models.CharField(blank=True, max_length=25, null=True)),
                ('bank_code', models.CharField(blank=True, max_length=25, null=True)),
                ('account_name', models.CharField(blank=True, max_length=25, null=True)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=25)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.TextField()),
                ('commission', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=25)),
                ('amount', models.IntegerField()),
                ('ref', models.CharField(max_length=7)),
                ('transaction', models.CharField(default='unconfirmed', max_length=25)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percentage', models.IntegerField()),
                ('valid_till', models.DateField()),
                ('product', models.ManyToManyField(blank=True, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='static\x07ssets\\images\\image_downloader_1698902956158.png', upload_to='media')),
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.IntegerField()),
                ('earnings', models.IntegerField(default=0)),
                ('rec_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rec_by', to=settings.AUTH_USER_MODEL)),
                ('recommendations', models.ManyToManyField(blank=True, related_name='recs', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
