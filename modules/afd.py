"""
File with the definition of an AFD.
"""
from af import Af

class Afd(Af):
    """ Um automato finito determinístico. """
    def __init__(self, nome=None, alfabeto=None, estados=None):
        Af.__init__(self, nome, alfabeto, estados)

    def __str__(self):
        return Af.__str__

    def __doc__(self):
        return self.__class__.__doc__
