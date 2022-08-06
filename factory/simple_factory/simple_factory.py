"""
PADRÃO DE PROJETO 'SIMPLE FACTORY'
    NÃO É CONSIDERADO UM PADRÃO DE PROJETO PARA ALGUMAS BIBLIOGRAFIAS
    
    Na POO o termo 'FACTORY' (fábrica) é uma classe ou método responsável por criar objetos.
    
    VANTAGENS:
        - Permite criar um sistema com baixo acoplamento entre classes porque
        oculta as classes que criam os objetos do código do cliente.

        - Facilita a adição de novas classes ao código, porque o cliente não
        conhece e nem utiliza a implementação da classe (utiliza a factory).
        
        - Pode facilitar o processo de criação de 'cache' ou 'singletons', porque
        a fábrica pode retornar um objeto já criado para o cliente, ao invés de 
        criar novos objetos sempre que o cliente precisar.
        
    DESVANTAGES:
        - Pode introduzir muitas classes no código.
    
VIDEO UML DA SEÇÃO.

NESTE EXEMPLO USAREMOS UM SISTEMA SIMPLISTA DE COMO FUNCIONARIA UM 'UBER'.
"""
from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    """Class Abstrata que cria objetos do tipo Veículo"""
    @abstractmethod
    def get_carro(self):
        """Método abstrado que cria um 'contrato' com o desenvolvedor,
        garantindo que as classes que herdam de 'Veículo' tenham este método."""
        pass
    

class CarroPopular(Veiculo):
    def __init__(self):
        self.get_carro()
    
    def get_carro(self) -> None:
        print('Cliente está usando Carro Popular')


class CarroLuxo(Veiculo):
    def __init__(self):
        self.get_carro()
    
    def get_carro(self) -> None:
        print('Cliente está usando Carro Luxo')
        
        
class VeiculoFactory:
    def __init__(self, tipo: str):
        self.buscar_cliente(tipo)
    
    def get_carro(self, tipo: str) -> None | CarroPopular | CarroLuxo:
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'luxo':
            return CarroLuxo()
        return None
        
    def buscar_cliente(self,tipo: str) -> None:
        self.get_carro(tipo)


if __name__ == '__main__':
    lista_carros = ['popular', 'luxo']
    
    for choices in range(10):
        cliente = VeiculoFactory(choice(lista_carros))
