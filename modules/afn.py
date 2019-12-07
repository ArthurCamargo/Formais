
"""
    File with the definition of an AFN.
"""
from af import Af

class Afn(Af):
    """ Um automato finito não determinístico. """
    def __init__(self, nome=None, alfabeto=None, estados=None, transicoes=None):
        Af.__init__(self, nome, alfabeto, estados)
        self.transicoes = transicoes
    def __str__(self):
        string = self.nome + '\n' + str(self.alfabeto) + "\n" + str(self.estados) + '\n'+ str(self.transicoes)
        return string
    def __doc__(self):
        return self.__class__.__doc__
