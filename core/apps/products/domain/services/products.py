from abc import (
    ABC,
    abstractmethod,
)

from typing import Iterable

from core.apps.products.domain.entities.products import Product
from core.apps.products.models.products import ProductModel
from core.api.pagination import PaginationIn

class BaseProductService(ABC):
    
    def get_product_list(
        self,
        pagination: PaginationIn
    ) -> Iterable[Product]:
        ...

    def create_product(
        self,
        title: str,
        description: str,
        price: int
    ) -> Iterable[Product]:
        ...

class ORMProductService(BaseProductService):
    
    @abstractmethod
    def get_product_list(
        self,
        pagination: PaginationIn
    ) -> Iterable[Product]:
        query = ProductModel.objects.all()[
            pagination.offset:pagination.offset + pagination.limit
        ]
        return [product.to_entity() for product in query]
    
    @abstractmethod
    def create_product(
        self,
        title: str,
        description: str,
        price: int
    ) -> Iterable[Product]:
        return ProductModel.objects.create(title, description, price)