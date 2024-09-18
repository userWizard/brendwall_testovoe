from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    id: int # noqa
    title: str
    price: int
    created_at: datetime
    updated_at: datetime
    description: str | None = None
