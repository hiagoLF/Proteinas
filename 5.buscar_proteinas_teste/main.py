import pandas as pd

from utils.buscar import requestProteinsFromUniprot, createProteinsDictionaryFromFasta, buscarPedacosDaProteina
from utils.guardar import guardarFastaEmArquivo
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

arquivo = pd.read_csv(dir_path+'/../input/proteinas_para_teste.csv')
idsProteinas = ' '.join(arquivo['Protein_ID'])
proteinasFasta = requestProteinsFromUniprot(idsProteinas)
guardarFastaEmArquivo(proteinasFasta)

dicionarioDeProteinas = createProteinsDictionaryFromFasta(proteinasFasta)

fragmentosTransmembrana = []
fragmentosNaoTransmembrana = []

for index, idProteina in enumerate(arquivo['Protein_ID']):
    if idProteina not in dicionarioDeProteinas:
        continue

    [restoEsquerdo, 
    regiaoTransmembrana, 
    restoDireito] = buscarPedacosDaProteina(dicionarioDeProteinas[idProteina], arquivo['TM_Segment_Helix'][index])

    if(len(restoEsquerdo) > 0):
        fragmentosNaoTransmembrana.append(restoEsquerdo)
    
    if(len(restoDireito) > 0):
        fragmentosNaoTransmembrana.append(restoDireito)

    if(len(regiaoTransmembrana) > 0):
        fragmentosTransmembrana.append(regiaoTransmembrana)

transmembranaDF = pd.DataFrame({'SEQUENCIA_TRANSMEMBRANA' : fragmentosTransmembrana})
naoTransmembranaDF = pd.DataFrame({'SEQUENCIA_NAO_TRANSMEMBRANA' : fragmentosNaoTransmembrana})

transmembranaDF.to_csv(dir_path+'/../output/proteinas_teste/fragmentos_transmembrana.csv', index=False)
naoTransmembranaDF.to_csv(dir_path+'/../output/proteinas_teste/fragmentos_nao_transmembrana.csv', index=False)

