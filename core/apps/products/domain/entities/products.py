from dataclasses import dataclasses

@dataclasses
class Product:
    id: int # noqa
    title: str | None = None
    description: str | None = None
    price: int