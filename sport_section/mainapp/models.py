from django.db import models


class SectionView(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Sportsman(models.Model):
    section = models.ForeignKey(SectionView,
                                on_delete=models.CASCADE)
    surname = models.TextField(max_length=128)
    name = models.TextField(max_length=128)
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'
