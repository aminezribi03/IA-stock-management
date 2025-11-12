def score_tendance(nb_mentions):
    if nb_mentions > 100:
        return 5
    elif nb_mentions > 50:
        return 3
    elif nb_mentions > 10:
        return 1
    else:
        return 0
