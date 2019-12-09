"""
Programa principal de linguagens formais e automatos
"""

#from operations import afn_afd_convert
from util import read_file
from af import Af

#Cria uma afn
MYAFN = read_file('../tests/test3.afn')
MYAFN.minimize()
#MYAFN.print_grammar()
#print(MYAFD)
#print(MYAFN.transform_afd())
#MYAFN.transform_afd()
