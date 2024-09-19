from django.http import HttpRequest
from ninja import (
    Query,
    Router,
)

from core.api.schemas import ApiResponse, ListPaginatedResponse
from core.api.v1.products.schemas import ProductSchema
from core.api.pagination import PaginationIn, PaginationOut
from core.apps.products.domain.services.products import BaseProductService, ORMProductService

router = Router(tags=['Products'])

router.get('product_list/', response=ListPaginatedResponse[ProductSchema])
def get_products_list_handler(
    request: HttpRequest,
    pagination_in: Query[PaginationIn]
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    service: BaseProductService = ORMProductService()
    
    products_list = service.get_product_list(pagination_in=pagination_in)
    
    items = [ProductSchema.from_entity(obj) for obj in products_list]
    
    pagination_out = PaginationOut(
        items=items,
        limit=pagination_in.limit 
    )
    
    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out)
    )


router.post('products_create/', response=ListPaginatedResponse[ProductSchema])
def create_products_handler(
    request: HttpRequest,
    title: str,
    description: str,
    price: int
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    service : BaseProductService = ORMProductService()
    
    create_products = service.create_product(
        title=title, description=description, price=price
    )
    return create_products