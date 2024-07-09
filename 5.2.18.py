class AnyClass:

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __repr__(self):
        B = [f'{k}={v!r}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}({", ".join(B)})'


    def __str__(self):
        B = [f'{k}={v!r}' for k, v in self.__dict__.items()]
        return f'{self.__class__.__name__}: {", ".join(B)}'

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))