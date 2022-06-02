import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def buscarConteudoFasta():
    file = open(dir_path+'/../../output/proteinas.fasta', 'r')
    content = file.read()
    file.close()
    return content

def buscarPedacosDaProteina(sequenciaProteina: str, transmembrana: str):
    textoIntervalo = ((transmembrana.split('(')[1])[:-1]).split('-')
    intervalo = [int(textoIntervalo[0]), int(textoIntervalo[1])]

    restoEsquerdo = sequenciaProteina[0:intervalo[0]-1]
    regiaoTransmembrana = sequenciaProteina[intervalo[0]-1:intervalo[1]-1]
    restoDireito = sequenciaProteina[intervalo[1]-1:-1]
    return [restoEsquerdo, regiaoTransmembrana, restoDireito]
