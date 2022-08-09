# Generated by Django 4.0.1 on 2022-08-06 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academyapp', '0003_alter_categorylevelthree_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorylevelone',
            options={'verbose_name': 'Kategori (1)', 'verbose_name_plural': 'Kategoriler (1)'},
        ),
        migrations.AlterModelOptions(
            name='categorylevelthree',
            options={'verbose_name': 'Kategori (3)', 'verbose_name_plural': 'Kategoriler (3)'},
        ),
        migrations.AlterModelOptions(
            name='categoryleveltwo',
            options={'verbose_name': 'Kategori (2)', 'verbose_name_plural': 'Kategoriler (2)'},
        ),
        migrations.AlterField(
            model_name='categorylevelone',
            name='category_name',
            field=models.CharField(max_length=40, verbose_name='Kategori (1)'),
        ),
        migrations.AlterField(
            model_name='categorylevelone',
            name='order_number',
            field=models.IntegerField(unique=True, verbose_name='Sıra Numarası'),
        ),
        migrations.AlterField(
            model_name='categorylevelone',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='categorylevelthree',
            name='category_name',
            field=models.CharField(max_length=40, verbose_name='Kategori (3)'),
        ),
        migrations.AlterField(
            model_name='categorylevelthree',
            name='order_number',
            field=models.IntegerField(unique=True, verbose_name='Sıra Numarası'),
        ),
        migrations.AlterField(
            model_name='categorylevelthree',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='categorylevelthree',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='academyapp.categoryleveltwo', verbose_name='Alt Kategori'),
        ),
        migrations.AlterField(
            model_name='categoryleveltwo',
            name='category_name',
            field=models.CharField(max_length=40, verbose_name='Kategori (2)'),
        ),
        migrations.AlterField(
            model_name='categoryleveltwo',
            name='order_number',
            field=models.IntegerField(unique=True, verbose_name='Sıra Numarası'),
        ),
        migrations.AlterField(
            model_name='categoryleveltwo',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='categoryleveltwo',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='academyapp.categorylevelone', verbose_name='Alt Kategori'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kurs Adı')),
                ('description', models.TextField(verbose_name='Kurs Açıklaması')),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktif')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Fiyat')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ('image', models.FileField(upload_to='images', verbose_name='Resim')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to=settings.AUTH_USER_MODEL, verbose_name='Eğitmen')),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurslar',
            },
        ),
    ]