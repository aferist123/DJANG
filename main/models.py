from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст новини")
    author = models.CharField(max_length=100, verbose_name="Автор")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def __str__(self):
        return self.title