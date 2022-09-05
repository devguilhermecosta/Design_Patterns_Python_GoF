"""
O Pattern Monostate (ou Borg) tem o mesmo objetivo do Singleton.
É uma variação do Sigleton.
A diferença é que o Singleton sempre retorna a mesma instância da classe,
e no Monostate diferentes instâncias podem retornar a classe, porém, o
Monostate garante que todas as instâncias retornem sempre o mesmo estado
da classe.

O Pattern Monostate não faz parte do GoF. Ele foi proposto por Alex Martelli.
"""

# classe que retorna uma representação para __str__ e __repr__ para qualquer
# classe que herdar de MonoStateMixin
class MonoStateMixin:
    def __str__(self):
        parametros = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
            )
        return f'{self.__class__.__name__}({parametros})'
        
    def __repr__(self):
        return self.__str__()
    

# primeira maneira de usar o Monostate
# herda de MonoStateMixin para usar __str__ e __repr__
class MonoState(MonoStateMixin):
    
    # dicionário vazio
    _state: dict = {}
    
    def __init__(self, nome=None, sobrenome=None):
        # __dict__ armazena todos os atributos de classe
        # aqui estamos fazendo um ADD no __dict__ usando o atributo de classe
        # _state. Tudo o que estiver em _state será adicionado em __dict__.
        self.__dict__: dict = self._state
        
        # aqui estamos dizendo que, caso o valor de nome não seja None um
        # atributo self.nome será criado com o valor de nome.
        # esse atributo por sua vez será adicionad em __dict__
        if nome is not None:
            self.nome: str = nome
        
        # aqui estamos dizendo que, caso o valor de sobrenome não seja None um
        # atributo self.sobrenome será criado com o valor de sobrenome.
        # esse atributo por sua vez será adicionad em __dict__
        if sobrenome is not None:
            self.sobrenome: str = sobrenome
        
        # o grande ponto do MONOSTATE está no __dict__.
        # Existe somente um __dict__ por classe, então independente de quantas
        # instancias existirem para a classe MonoState() todas elas sempre
        # estarão acessando e modificando o mesmo __dict__
        
if __name__ == '__main__':
    t1 = MonoState(nome='Guilherme')
    t2 = MonoState(sobrenome='Costa')
    print(t1)
    print(t2)
