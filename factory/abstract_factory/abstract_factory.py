"""
Factory Method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar.
O Factory Method permite adiar a instanciação para as subclasses, garantindo
o baixo acoplamento entre classes.  
"""
from abc import ABC, abstractmethod
from random import choice


#CLASSE ABSTRATA
class Veiculo(ABC):
    """Class Abstrata que cria objetos do tipo Veículo"""
    @abstractmethod
    def get_veiculo(self):
        """Método abstrado que cria um 'contrato' com o desenvolvedor,
        garantindo que as classes que herdam de 'Veículo' tenham este método."""
        pass
    
   
#CLASSE ABSTRATA    
class VeiculoFactory(ABC):
    def __init__(self, tipo: str):
        self.__buscar_cliente(tipo)
    
    @abstractmethod
    def get_veiculo(self, tipo: str) -> None:
        pass
        
    def __buscar_cliente(self,tipo: str) -> None:
        self.get_veiculo(tipo)
    

class CarroPopular(Veiculo):
    def __init__(self):
        self.get_veiculo()
    
    def get_veiculo(self) -> None:
        print('Cliente está usando Carro Popular')


class CarroLuxo(Veiculo):
    def __init__(self):
        self.get_veiculo()
    
    def get_veiculo(self) -> None:
        print('Cliente está usando Carro Luxo')
        

class MotoPopular(Veiculo):
    def __init__(self):
        self.get_veiculo()
        
    def get_veiculo(self) -> None:
        print('Cliente está usando Moto Popular')        


class MotoLuxo(Veiculo):
    def __init__(self):
        self.get_veiculo()
        
    def get_veiculo(self) -> None:
        print('Cliente está usando Moto de Luxo')
        

class ZonaSulVeiculos(VeiculoFactory):
    def get_veiculo(self, tipo: str) -> None | CarroPopular | CarroLuxo | MotoPopular | MotoLuxo:
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'carro_luxo':
            return CarroLuxo()
        if tipo == 'moto_popular':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        return None
    

class ZonaNorteVeiculos(VeiculoFactory):
    def get_veiculo(self, tipo: str) -> None | CarroPopular | CarroLuxo | MotoPopular | MotoLuxo:
        if tipo == 'carro_popular':
            return CarroPopular()
        if tipo == 'carro_luxo':
            return CarroLuxo()
        return None


if __name__ == '__main__':
    lista_carros = ['carro_popular', 
                    'carro_luxo',
                    'moto_popular',
                    'moto_luxo',]
    
    print('Carros da Zona Sul')
    for choices in range(10):
        cliente = ZonaSulVeiculos(choice(lista_carros))

    print('')
    
    lista_carros1 = ['carro_popular', 
                    'carro_luxo',
                    ]
    print('Carros da Zona Norte')
    for choices in range(10):
        cliente1 = ZonaNorteVeiculos(choice(lista_carros1))