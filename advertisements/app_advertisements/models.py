from django.db import models

class Advertisement(models.Model):
    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"



    title = models.CharField("Заголовок", max_length=128)
    deskription = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text = "Уместен торг или нет")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
