def calcularScoresDasSequencias(sequencias: list, pontuacoesAminoacidos: dict, pontuacoesAminoacidosDuplas: dict):    
    def extrairPontuacaoDeJanelaDeslizante(janela: str):
        tamanhoJanela = len(janela)
        pontuacao = 0
        for indicieAtual, aminoacidoAtual in enumerate(janela):
            pontuacaoAminoacido = pontuacoesAminoacidos[aminoacidoAtual]
            pontuacao += pontuacaoAminoacido
            if(indicieAtual < tamanhoJanela-1):
                pontuacaoDuplaAminoacido = pontuacoesAminoacidosDuplas[aminoacidoAtual+janela[indicieAtual + 1]]
                pontuacao += pontuacaoDuplaAminoacido
        return pontuacao


    pontuacoes = []
    for indicie, sequencia in enumerate(sequencias):
        tamanhoSequencia = len(sequencia)
        if(tamanhoSequencia <= 25):
            pontuacao = extrairPontuacaoDeJanelaDeslizante(sequencia)
            pontuacoes.append(pontuacao)
        else:
            for vez in range(0, tamanhoSequencia - 26):
                pontuacao = extrairPontuacaoDeJanelaDeslizante(sequencia[vez:vez+26])
                pontuacoes.append(pontuacao)
    
    return pontuacoes
