from utils.busca import buscarConteudoFasta, buscarPedacosDaProteina
from utils.gerar import createProteinsDictionaryFromFasta
import pandas as pd
import os 

conteudoFasta = buscarConteudoFasta()
dicionarioDeProteinas = createProteinsDictionaryFromFasta(conteudoFasta)

dir_path = os.path.dirname(os.path.realpath(__file__))
dataFrameDeProteinas = pd.read_csv(dir_path+'/../input/proteinas.csv')

fragmentosTransmembrana = []
fragmentosNaoTransmembrana = []

for index, idProteina in enumerate(dataFrameDeProteinas['Protein_ID']):
    if idProteina not in dicionarioDeProteinas:
        continue

    [restoEsquerdo, 
    regiaoTransmembrana, 
    restoDireito] = buscarPedacosDaProteina(dicionarioDeProteinas[idProteina], dataFrameDeProteinas['TM_Segment_Helix'][index])

    if(len(restoEsquerdo) > 0):
        fragmentosNaoTransmembrana.append(restoEsquerdo)
    
    if(len(restoDireito) > 0):
        fragmentosNaoTransmembrana.append(restoDireito)

    if(len(regiaoTransmembrana) > 0):
        fragmentosTransmembrana.append(regiaoTransmembrana)

transmembranaDF = pd.DataFrame({'SEQUENCIA_TRANSMEMBRANA' : fragmentosTransmembrana})
naoTransmembranaDF = pd.DataFrame({'SEQUENCIA_NAO_TRANSMEMBRANA' : fragmentosNaoTransmembrana})

transmembranaDF.to_csv(dir_path+'/../output/fragmentos_transmembrana.csv', index=False)
naoTransmembranaDF.to_csv(dir_path+'/../output/fragmentos_nao_transmembrana.csv', index=False)