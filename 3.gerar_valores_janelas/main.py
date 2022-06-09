import pandas as pd
import os
from numeros.precisao import diminuirPrecisaoDeNumeros
from gerar.dicionario import gerarDicionarioDoDataFrame
from score.calcularScoresDeSequencias import calcularScoresDasSequencias
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))

pontuacoesDeAminoAcidos = pd.read_csv(
    dir_path+'/../input/razoes_aminoacidos.csv')
pontuacoesDeAminoAcidosDuplas = pd.read_csv(
    dir_path+'/../input/razoes_duplas_aminoacidos.csv', keep_default_na=False)

pontuacoesDeAminoAcidosDicionario = gerarDicionarioDoDataFrame(
    pontuacoesDeAminoAcidos, 'AMINO_ACID', 'REASON')
pontuacoesDeAminoAcidosDuplasDicionario = gerarDicionarioDoDataFrame(
    pontuacoesDeAminoAcidosDuplas, 'AMINO_ACID_COUPLE', 'REASON')

sequenciasTransmembrana = pd.read_csv(
    dir_path+'/../output/fragmentos_transmembrana.csv')
sequenciasNaoTransmembrana = pd.read_csv(
    dir_path+'/../output/fragmentos_nao_transmembrana.csv', keep_default_na=False)

scoresSequenciasTransmembrana = calcularScoresDasSequencias(
    sequenciasTransmembrana['SEQUENCIA_TRANSMEMBRANA'],
    pontuacoesDeAminoAcidosDicionario, pontuacoesDeAminoAcidosDuplasDicionario,
)
scoresSequenciasNaoTransmembrana = calcularScoresDasSequencias(
    sequenciasNaoTransmembrana['SEQUENCIA_NAO_TRANSMEMBRANA'],
    pontuacoesDeAminoAcidosDicionario, pontuacoesDeAminoAcidosDuplasDicionario,
)

diminuirPrecisaoDeNumeros(scoresSequenciasTransmembrana)
diminuirPrecisaoDeNumeros(scoresSequenciasNaoTransmembrana)


resumoScoresTransMembrana = pd.DataFrame(scoresSequenciasTransmembrana)
resumoScoresTransMembrana.plot.kde()
plt.title('Distribuição dos scores em janelas transmembrana')
plt.xlabel("Score")
plt.ylabel("Densidade")
plt.savefig(dir_path+'/../output/valores_janelas/distr_transmembrana.png')


plt.clf()
resumoScoresNaoTransMembrana = pd.DataFrame(scoresSequenciasNaoTransmembrana)
resumoScoresNaoTransMembrana.plot.kde()
plt.title('Distribuição dos scores em janelas não transmembrana')
plt.xlabel("Score")
plt.ylabel("Densidade")
plt.savefig(dir_path+'/../output/valores_janelas/distr_nao_transmembrana.png')


dfScoresTransmembrana = pd.DataFrame(
    {'SCORE_TRANSMEMBRANA': scoresSequenciasTransmembrana})
dfScoresNaoTransmembrana = pd.DataFrame(
    {'SCORE_NAO_TRANSMEMBRANA': scoresSequenciasNaoTransmembrana})

dfScoresTransmembrana.to_csv(dir_path+'/../output/valores_janelas/scores_sec_transmembrana.csv', index=False)
dfScoresNaoTransmembrana.to_csv(dir_path+'/../output/valores_janelas/scores_sec_nao_transmembrana.csv', index=False)
