
"""
    File with the definition of an AFN.
"""
from af import Af
from af import State

class Afn(Af):
    """ Um automato finito não determinístico. """
    def __init__(self, nome=None, alfabeto=None, estados=None, current=None):
        Af.__init__(self, nome, alfabeto, estados)

        for estado in self.estados:
            if estado.nome == current:
                self.current = estado

    def __str__(self):
        n_l = "\n"
        string = self.nome + n_l + str(self.alfabeto) + n_l + str(self.estados)
        return string

    def __repr__(self):
        return str(self)

    def __doc__(self):
        return self.__class__.__doc__

    def peak(self, letter):
        """
        Anda com o estado atual para o proximo estado dado uma letra
        se houver mais de 1 estado para qual ele vai retorna um novo estado
        com a juncao dos estados, se nao houver como andar retorn None
        """
        #Terminar de fazer
        aux = []
        new = self.current.peak(letter)
        for estado in self.estados:
            if estado.nome == new[0]:
                aux.append(estado)
        return aux

    def transform_afd(self):
        """
        Algoritmo que transforma a afn em uma afd
        """
        tmp = {self.current.nome}
        visited = set()

        while len(tmp) != 0:
            cur = tmp.pop()
            if cur not in visited:
                visited.add(cur)
                print(cur)
                for letter in self.alfabeto:
                    tmp.update(self.peak(letter))
                    print(tmp)
