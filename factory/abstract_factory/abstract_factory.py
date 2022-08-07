"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou depedentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herença, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def get_veiculo(self): pass
            

class VeiculoPopular(Veiculo, ABC):
    @abstractmethod
    def get_veiculo(self) -> None: pass


class VeiculoLuxo(Veiculo, ABC):
    @abstractmethod
    def get_veiculo(self) -> None: pass


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> None | VeiculoPopular: pass
    
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> None | VeiculoLuxo: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> None | VeiculoPopular: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> None | VeiculoLuxo: pass
    

class CarroPopularZN(VeiculoPopular):    
    def get_veiculo(self) -> None:
        print('Cliente ZN está usando Carro Popular')


class CarroLuxoZN(VeiculoLuxo):    
    def get_veiculo(self) -> None:
        print('Cliente ZN está usando Carro Luxo')
        

class MotoPopularZN(VeiculoPopular):        
    def get_veiculo(self) -> None:
        print('Cliente ZN está usando Moto Popular')        


class MotoLuxoZN(VeiculoLuxo):        
    def get_veiculo(self) -> None:
        print('Cliente ZN está usando Moto de Luxo')
       
        
class CarroPopularZS(VeiculoPopular):    
    def get_veiculo(self) -> None:
        print('Cliente ZS está usando Carro Popular')


class CarroLuxoZS(VeiculoLuxo):    
    def get_veiculo(self) -> None:
        print('Cliente ZS está usando Carro Luxo')
        

class MotoPopularZS(VeiculoPopular):        
    def get_veiculo(self) -> None:
        print('Cliente ZS está usando Moto Popular')        


class MotoLuxoZS(VeiculoLuxo):        
    def get_veiculo(self) -> None:
        print('Cliente ZS está usando Moto de Luxo')
        

class ZonaSulVeiculos(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()
    
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

class ZonaNorteVeiculos(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()
    
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()
    
    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()
    

class Cliente:
    def buscar_clientes_ZS(self):
        for factory in [ZonaSulVeiculos()]:
            cp = factory.get_carro_popular()
            cp.get_veiculo()
            
            cl = factory.get_carro_luxo()
            cl.get_veiculo()
                        
            mp = factory.get_moto_popular()
            mp.get_veiculo()  
                                  
            ml = factory.get_moto_luxo()
            ml.get_veiculo()    
            
    def buscar_clientes_ZN(self):
        for factory in [ZonaNorteVeiculos()]:
            cp = factory.get_carro_popular()
            cp.get_veiculo()
            
            cl = factory.get_carro_luxo()
            cl.get_veiculo()
                        
            mp = factory.get_moto_popular()
            mp.get_veiculo()  
                                  
            ml = factory.get_moto_luxo()
            ml.get_veiculo()
        

if __name__ == '__main__':
    cliente = Cliente()
    cliente.buscar_clientes_ZS()
    print('')
    cliente.buscar_clientes_ZN()
