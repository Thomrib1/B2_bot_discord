import random

def calculate_qi():

    return random.randint(70, 160)

def get_qi_message(qi_score):

    if qi_score < 85:
        return f"Ton QI est de **{qi_score}** là c'est chaud "
    elif qi_score < 100:
        return f"Ton QI est de **{qi_score}** t'es pas dingue "
    elif qi_score < 115:
        return f"Ton QI est de **{qi_score}** - tout juste "
    elif qi_score < 130:
        return f"Ton QI est de **{qi_score}** Nice "
    else:
        return f"Ton QI est de **{qi_score}** le goatttttt"