from django.db import models

# class Veterinarians(U):
#     city = models.
#     specialization = models.CharField(
#         max_length=85,
#         blank=True,
#         verbose_name='Специализация' 
#     )  
#     name = models.CharField(
#         max_length=250,
#         verbose_name='Имя'
#     )
#     last_name = models.CharField(
#         max_length=200,
#         verbose_name='Фамилия'
#     )
#     email = models.EmailField()
#     description = models.TextField(
#         blank=True,
#         verbose_name='Расскажите о себе'
#         help_text='Пару строчек о себе')
#     place_jobs = models.CharField(
#         max_length=250, 
#         verbose_name='Место работы'
#         help_text='Укажите место работы'
#         )
#     phone = models.Aggregate  
#     price = models.ForeignKey(prise)
#     free_help = models.ForeignKey()
#     rating = models.

#     def get_absolute_url(self):
#         """Method for a category that specifies a specific category"""
#         return reverse("category", kwargs={"category_id": self.pk})
    

#     def __str__(self):
#         return self.specialization

#     class Meta:
#         verbose_name ='Ветеринары'
#         verbose_name_plural ='Ветеринар'
#         ordering = ['-']

# class Price(models.Model):
#     title = models.CharField(
#         max_length=250
#     )
#     min_price = models.
#     max_price = models.
#     animals = models.ForeignKey('AnimalsCategory')
#     record = models.ForeignKey('Record'запись или выезд')

# class Record(models.Model):
#     title = models.CharField(
#         max_length=45,
#         verbose_name='Способ окозания услуги')

# class Animals(models.Model):
#     type = model.CharField(
#         max_length=50,
#         verbose_name='Тип животного'
#     )
#     type_of_assistance = models.ForeignKey(Helps_of_animals)
#     image = models.ImageField( 
#         upload_to ='photos/%Y/%m/%d/', 
#         null=True, 
#         blank=True, 
#         verbose_name='Фото'
#     )
    

