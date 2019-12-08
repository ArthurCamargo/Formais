"""
Programa principal de linguagens formais e automatos
"""

#from operations import afn_afd_convert
from util import read_file
from af import Af
from afd import Afd
from afn import Afn

#Cria uma afn
MYAFN = read_file('../tests/test1.afn')
#MYAFD = MYAFN.transform_afd()
#print(MYAFD)
#print(MYAFN.transform_afd())
#MYAFN.peak('a')
#MYAFN.transform_afd()
