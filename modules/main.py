"""
Programa principal de linguagens formais e automatos
"""

from operations import *
from util import *
from af import Af
from afd import Afd
from afn import Afn

#Cria uma afn
MYAFN = Afn(None, None, None, None)
read_file('../tests/tests.afn')
