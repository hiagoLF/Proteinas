# Carregar valores dos scores não transmembrana
# Carregar valores dos scores transmembrana
# Calcular médias
# Calcular desvios padrões
# Calcular pontos de corte

import os
from statistics import mean, pstdev
import pandas as pd
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

scoresNaoTransmembrana = pd.read_csv(
    dir_path+'/../output/valores_janelas/scores_sec_nao_transmembrana.csv', keep_default_na=False)
scoresTransmembrana = pd.read_csv(
    dir_path+'/../output/valores_janelas/scores_sec_transmembrana.csv', keep_default_na=False)


mediaScoreNaoTransmembrana = mean(
    scoresNaoTransmembrana['SCORE_NAO_TRANSMEMBRANA'])
mediaScoreTransmembrana = mean(scoresTransmembrana['SCORE_TRANSMEMBRANA'])

desvioPadraoScoreNaoTransmembrana = pstdev(
    scoresNaoTransmembrana['SCORE_NAO_TRANSMEMBRANA'])
desvioPadraoScoreTransmembrana = pstdev(
    scoresTransmembrana['SCORE_TRANSMEMBRANA'])

pontoDeCorteRelaxado = mediaScoreNaoTransmembrana + \
    (2 * desvioPadraoScoreNaoTransmembrana)
pontoDeCorteRigoroso = mediaScoreTransmembrana + \
    (-2 * desvioPadraoScoreTransmembrana)

pontosDeCorte = {
    'regiaoTransmembrana': {
        'pontoDeCorte': pontoDeCorteRigoroso,
        'media': mediaScoreTransmembrana,
        'desvioPadrao': desvioPadraoScoreTransmembrana
    },
    'regiaoNaoTransmembrana': {
        'pontoDeCorte': pontoDeCorteRelaxado,
        'media': mediaScoreNaoTransmembrana,
        'desvioPadrao': desvioPadraoScoreNaoTransmembrana
    },
}

with open(dir_path+'/../output/pontos_de_corte.json', 'w') as f:
    json.dump(pontosDeCorte, f)
