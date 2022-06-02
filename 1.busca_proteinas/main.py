import pandas as pd

from utils.buscar import requestProteinsFromUniprot
from utils.guardar import guardarFastaEmArquivo
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
arquivo = pd.read_csv(dir_path+'/../input/proteinas.csv')
idsProteinas = ' '.join(arquivo['Protein_ID'])
proteinasFasta = requestProteinsFromUniprot(idsProteinas)
guardarFastaEmArquivo(proteinasFasta)