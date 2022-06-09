import json
import pandas as pd
import os
from gerar.dicionario import gerarDicionarioDoDataFrame
from score.calcular import calcularScoresDasSequencias

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/../output/pontos_de_corte.json') as file:
    pontosDeCorte = json.load(file)


sequenciasTransmembrana = pd.read_csv(
    dir_path+'/../output/proteinas_teste/fragmentos_transmembrana.csv')
sequenciasNaoTransmembrana = pd.read_csv(
    dir_path+'/../output/proteinas_teste/fragmentos_nao_transmembrana.csv', keep_default_na=False)


pontuacoesDeAminoAcidos = pd.read_csv(
    dir_path+'/../input/razoes_aminoacidos.csv')
pontuacoesDeAminoAcidosDuplas = pd.read_csv(
    dir_path+'/../input/razoes_duplas_aminoacidos.csv', keep_default_na=False)

pontuacoesDeAminoAcidosDicionario = gerarDicionarioDoDataFrame(
    pontuacoesDeAminoAcidos, 'AMINO_ACID', 'REASON')
pontuacoesDeAminoAcidosDuplasDicionario = gerarDicionarioDoDataFrame(
    pontuacoesDeAminoAcidosDuplas, 'AMINO_ACID_COUPLE', 'REASON')

scoresSequenciasTransmembrana = calcularScoresDasSequencias(
    sequenciasTransmembrana['SEQUENCIA_TRANSMEMBRANA'],
    pontuacoesDeAminoAcidosDicionario, pontuacoesDeAminoAcidosDuplasDicionario,
)
scoresSequenciasNaoTransmembrana = calcularScoresDasSequencias(
    sequenciasNaoTransmembrana['SEQUENCIA_NAO_TRANSMEMBRANA'],
    pontuacoesDeAminoAcidosDicionario, pontuacoesDeAminoAcidosDuplasDicionario,
)

acertosDeTransmembrana = 0
acertoNaRegiaoIntermediaria = 0
acertosDeNaoTransmembrana = 0

for scoreTransmembrana in scoresSequenciasTransmembrana:
    if scoreTransmembrana >= pontosDeCorte['regiaoTransmembrana']['pontoDeCorte']:
        acertosDeTransmembrana += 1
    elif scoreTransmembrana >= pontosDeCorte['regiaoNaoTransmembrana']['pontoDeCorte']:
        acertosDeTransmembrana += 1
        acertoNaRegiaoIntermediaria += 1

for scoreNaoTransmembrana in scoresSequenciasNaoTransmembrana:
    if scoreNaoTransmembrana < pontosDeCorte['regiaoNaoTransmembrana']['pontoDeCorte']:
        acertosDeNaoTransmembrana += 1

porcentagemAcertoTransmembrana = (
    acertosDeTransmembrana / len(scoresSequenciasTransmembrana)) * 100
porcentagemAcertoRegiaoIntermediaria = (
    acertoNaRegiaoIntermediaria / len(scoresSequenciasTransmembrana)) * 100
porcentagemAcertoNaoTransmembrana = (
    acertosDeNaoTransmembrana / len(scoresSequenciasNaoTransmembrana)) * 100

resumo = {
    'acertos_de_transmembrana': round(porcentagemAcertoTransmembrana, 2),
    'acertos_na_regiao_intermediaria': round(porcentagemAcertoRegiaoIntermediaria, 2),
    'acertos_de_nao_transmembrana': round(porcentagemAcertoNaoTransmembrana, 2)
}

with open(dir_path+'/../output/proteinas_teste/resumo_de_acertos.json', 'w') as f:
    json.dump(resumo, f)
