"""
O Pattern Singleton garante que um determinada classe seja instanciada uma única vez.
Caso tenhamos mais de uma instância para a mesma classe, o objeto retornado será sempre o mesmo.
Isso pode ser iteressante, por exemplo, em casos de configuração de design de interface gráfica, em que a classe que controla as características da GUI (como tema, cor, fonte etc) será instanciada uma única vez.
Muitos desenvolvedoresnão adotam mais este padrão de desenvolvimento, e de fato,
não é muito utilizado nos dias atuais.
Um dos 4 GoF defende a exclusão do Singleton da relação dos Design Patterns.

Aqui veremos três maneiras de implementar um Sigleton:

-> com a própria classe;
-> com decorador personalizado;
-> com metaclassess.

"""

# 01 -> IMPLEMENTANDO O PADRÃO SINGLETON COM A PRÓPRIA CLASSE.
from tokenize import Single
from typing import Dict


class AppSettings:
    
    # atributo de classe que recebe um dict vazio como valor.
    # assim que a classe AppSetings for intanciada pela primeira vez
    # esse atributo de classe irá receber, dentro outros dados, o 
    # nome da instanciada que o está chamando e o local que ele
    # ocupa na memória, deixando de estar vazio.
    _instance = None
    
    # o dunder __new__ verifica se o atributo de classe _instance
    # está vazio. Se ele estiver vazio então o __new__ cria um novo
    # objeto e guarda dentro de _instance os dados referente a este
    # objeto.
    # Se AppSetings já foi instanciada, então o new retorna o mesmo
    # objeto já criado anteriormente, impedindo que a classe 
    # AppSetings gere mais de uma instância.
    def __new__(cls, *args, **kwargs):
        # primeiro verifica se _instance está vazio;
        # se estiver, _instance recebe os dados referente ao objeto criado;
        # se não estiver vazio, __new__ retorna o mesmo objeto.
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self): pass
        

if __name__ == '__main__':
    # estamos criando duas instâncias da mesma classe.
    # ao verficar se teste == teste_2 perceberemos
    # que ambas as instâncias estão retornando o mesmo objeto.
    # Tudo o que for alterado afetará todas as instâncias e vice-versa.
    teste = AppSettings()
    teste_2 = AppSettings()
    print(teste == teste_2)



# 02 -> IMPLEMENTANDO O PADRÃO SINGLETON COM DECORADOR PERSONALIZADO.

# decorador personalizado
# a função recebe uma classe
def singleton(classe):
    
    # o atributo instance começa como um dict vazio
    instance = {}
    
    # a função get_class verifica se instance está vazio.
    # se estiver vazio, instance receberá os dados provenientes
    # da CLASSE que o está usando como decorador.
    # se já tiver algum dado então a função retornará os dados
    # já presentes em intance.
    def get_class(*args, **kwargs):
        if classe not in instance:
            instance[classe] = classe(*args, **kwargs)
        return instance[classe]
    
    # perceba que a funçao singleton() retorna o próprio método get_class()
    # sem executá-lo
    return get_class

# classe OutroAppSettings decorada com nosso decorador personalizado.
@singleton
class OutroAppSettings:
    def __init__(self):
        self.tema = 'escuro'
        self.fonte = '18px'
        

if __name__ == '__main__':
    t1 = OutroAppSettings()
    t1.tema = 'Claro'
    t2 = OutroAppSettings()
    t3 = OutroAppSettings()
    # perceba que mesmo tendo três instâncias de OutroAppSettings, 
    # ao modificar o valor do atributo 'tema' apenas na instância 't1'
    # todas as outras instâncias, 't2 e t3', sofrerão as mesmas alterações.
    print(t1.tema, t2.tema, t3.tema)



# 03 -> IMPLEMENTANDO O PADRÃO SINGLETON COM METACLASSE.


# classe que será implementada como metaclass
# Deve herdar de type.
class Singleton(type):
    
    # atributo de classe que guardará as iformaçõe da variável
    # que está instanciando a classe MaisUmSettings()
    _instance: dict = {}
    
    # o método mágico __call__ permite que uma classe seja instanciada
    # como uma função.
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]
    

# a classe deve receber a Singleton criada como metaclass
class MaisUmSettigns(metaclass=Singleton):
    def __init__(self):
        self.tema = 'escuro'
        self.fonte = '18px'
        
        
if __name__ == '__main__':
    m1 = MaisUmSettigns()
    print(m1.fonte)
    m1.fonte = 'zero'
    m2 = MaisUmSettigns()
    print(m2.fonte)
