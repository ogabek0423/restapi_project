from rest_framework.pagination import LimitOffsetPagination


class PageNumberPagination(LimitOffsetPagination):
    def __init__(self, x, y):
        if x is None:
            default_limit = 5
        else:
            default_limit = x

        self.x = x
        self.y = y

    if x is None:
        default_limit = 10

    max_limit = 100
