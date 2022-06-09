import urllib.parse
import urllib.request

def requestProteinsFromUniprot(proteinsIds: str):
  params = {
    "format": "fasta",
    "columns": 'id,entry_name,reviewed',
    "from": "ID",
    "to": "ACC",
    "query": proteinsIds,
  }

  data = urllib.parse.urlencode(params)
  data = data.encode('utf-8')
  req = urllib.request.Request('https://www.uniprot.org/uploadlists/', data)
  with urllib.request.urlopen(req) as f:
    response = f.read()
  fastaProteins = response.decode('utf-8')
  return fastaProteins


def createProteinsDictionaryFromFasta(fastaProteins):
  proteinsList = fastaProteins.split('>')

  proteinSequencesDictionary = {}

  for protein in proteinsList:
    splitedFasta = protein.split('\n') 
    if(len(splitedFasta) > 1):
        proteinId = splitedFasta[0].split('|')[2].split(' ')[0].strip()
        splitedFasta.pop(0)
        proteinSequence = ''.join(splitedFasta)
        proteinSequencesDictionary[proteinId] = proteinSequence
  
  return proteinSequencesDictionary


def buscarPedacosDaProteina(sequenciaProteina: str, transmembrana: str):
    textoIntervalo = ((transmembrana.split('(')[1])[:-1]).split('-')
    intervalo = [int(textoIntervalo[0]), int(textoIntervalo[1])]

    restoEsquerdo = sequenciaProteina[0:intervalo[0]-1]
    regiaoTransmembrana = sequenciaProteina[intervalo[0]-1:intervalo[1]-1]
    restoDireito = sequenciaProteina[intervalo[1]-1:-1]
    return [restoEsquerdo, regiaoTransmembrana, restoDireito]
