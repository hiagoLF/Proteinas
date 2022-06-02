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