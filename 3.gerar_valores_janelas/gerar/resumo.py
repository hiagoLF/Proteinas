def resumirScores(scores: list):
    resumo = {}

    for score in scores:
        if str(round(score)) in resumo:
            resumo += 1
        else:
            resumo[round(score)] = 1
