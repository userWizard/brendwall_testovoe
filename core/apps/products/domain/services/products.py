from abc import (
    ABC,
    abstractmethod,
)

class BaseProductService(ABC):
    
    def get_product_list(self):
        ...


class ORMProductService(BaseProductService):
    
    @abstractmethod
    def get_product_list(self):
        ...