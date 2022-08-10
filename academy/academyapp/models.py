from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CategoryLevelOne(models.Model):
    category_name = models.CharField('Kategori (1)', max_length=40)
    order_number = models.IntegerField('Sıra Numarası', unique=True)
    slug = models.SlugField('Url', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Kategori (1)'
        verbose_name_plural = 'Kategoriler (1)'

    def __str__(self):
        return self.category_name


class CategoryLevelTwo(models.Model):
    category_name = models.CharField('Kategori (2)', max_length=40)
    order_number = models.IntegerField('Sıra Numarası', unique=True)
    slug = models.SlugField('Url', unique=True, db_index=True)
    sub_category = models.ForeignKey(CategoryLevelOne, models.SET_NULL,
                                     null=True, related_name='sub_categories', verbose_name='Alt Kategori')

    class Meta:
        verbose_name = 'Kategori (2)'
        verbose_name_plural = 'Kategoriler (2)'

    def __str__(self):
        return self.category_name


class Course(models.Model):
    name = models.CharField('Kurs Adı', max_length=50)
    description = models.TextField('Kurs Açıklaması')
    is_active = models.BooleanField('Aktif', default=False)
    unit_price = models.DecimalField('Fiyat', max_digits=5, decimal_places=2)
    slug = models.SlugField('Url', unique=True, db_index=True)
    instructor = models.ForeignKey(
        User, models.SET_NULL, null=True, related_name='courses', verbose_name='Eğitmen')
    image = models.FileField(upload_to='images', verbose_name='Resim')
    category_level_two = models.ForeignKey(
        CategoryLevelTwo, models.SET_NULL, null=True, verbose_name='Kategori')

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'

    def __str__(self):
        return f'{self.name} {self.instructor}'


class WhichCourseAndStudent(models.Model):
    student = models.ForeignKey(User, models.CASCADE, verbose_name='Öğrenci')
    course = models.ForeignKey(Course, models.CASCADE, verbose_name='Kurs')
    order_number = models.IntegerField('Sıra Numarası')

    class Meta:
        verbose_name = 'Kurs ve Öğrenci'
        verbose_name_plural = 'Kurslar ve Öğrenciler'

    def __str__(self):
        return f'{self.student} {self.course}'
