from monostate_1 import MonoStateMixin


class MonoState(MonoStateMixin):
    
    _state = {}
    
    # a diferente nesse método de criar um Monostate é que o método mágico
    # __new__ fica encarregado de criar o objeto, e não o __init__.
    def __new__(cls, *args, **kwargs):
        objeto = super().__new__(cls, *args, **kwargs)
        objeto.__dict__ = cls._state
        return objeto

    def __init__(self, nome=None, sobrenome=None):
        if nome is not None:
            self.nome: str = nome
            
        if sobrenome is not None:
            self.sobrenome: str = sobrenome
        

if __name__ == '__main__':
    t1 = MonoState()
    t1.nome = 'Adão'
    t1.sobrenome = 'Silva'
    t2 = MonoState()
    print(t1)
    print(t2)