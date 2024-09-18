from django.db import models
from django.core.validators import MinValueValidator

from core.apps.products.utils.temps import MIN_VALUE
from core.apps.common.models import TimedBaseModel
from core.apps.products.domain.entities.products import Product as ProductEntity



class ProductModel(TimedBaseModel):
    """Product model"""
    title = models.CharField(
        verbose_name='Название',
        max_length=50,
        blank=False,
    )
    price = models.IntegerField(
        verbose_name='Цена',
        validators=(MinValueValidator(MIN_VALUE),),
        error_messages={
            "errors":
            f"Минимальное время готовки {MIN_VALUE} минута."
        },
        default=MIN_VALUE,
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=200,
        blank=True
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    
    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.pk,
            title=self.title,
            price=self.price,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    def __str__(self):
        return self.title