"""
File with the definition of an AFD.
"""
from af import Af

class Afd(Af):
    """ Um automato finito determinístico. """
    def __init__(self, nome=None, alfabeto=None, estados=None, transicoes=None):
        Af.__init__(self, None, None, None)
        self.transicoes = transicoes
    def __str__(self):
        return self.__class__.__name__
    def __doc__(self):
        return self.__class__.__doc__
