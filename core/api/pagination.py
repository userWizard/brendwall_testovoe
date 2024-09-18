from ninja import Schema

class PaginationOut(Schema):
    offset: int
    limit: int


class PaginationIn(Schema):
    offset: int = 0
    limit: int = 20
