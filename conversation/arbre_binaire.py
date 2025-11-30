class Etapes:
    def __init__(self, question=None, left=None, right=None, result=None):
        self.question = question  
        self.left = left
        self.right = right
        self.result = result

# Representation du noeud de l'arbre les .self précisent ce que chaque noeud peut contenir
# Genre ici la question à poser, les différents alternatives possibles (oui/on) + le resultat

def create_profiles():

    return {
        'A': Etapes(result="Profil A : Penseur Stable --> Tes choix sont logiques, prudent tu restes méthodique"),
        'B': Etapes(result="Profil B : Analyste Explorateur --> Curieux sur tout les aspects, aucun secret n'existe pour toi"),
        'C': Etapes(result="Profil C : Empathique Introspectif --> Sensibles et profonds tu restes très émotionnel sans le montrer"),
        'D': Etapes(result="Profil D : Sage Pragmatique --> Calme et observateur seuls les actions réfléchies et concrètes sont justifiés a tes yeux"),
        'E': Etapes(result="Profil E : Passionné Spontané --> instinctif, intense, expressif"),
        'F': Etapes(result="Profil F : Aventurier Calme --> spontané mais posé, adaptable"),
        'G': Etapes(result="Profil G : Diplomate Fuyant --> Tu recherches l'equilibre parfait pour éviter les tensions"),
        'H': Etapes(result="Profil H : Volontaire Direct --> La vérité est un principe, affirmé va droit au but")
    }


def build_branch_1(profiles):

    q4 = Etapes(
        question="Préfères-tu la stabilité plutôt que le changement ?",
        left=profiles['A'],
        right=profiles['B']
    )
    
    q5 = Etapes(
        question="Te sens-tu facilement envahi par tes émotions ?",
        left=profiles['C'],
        right=profiles['D']
    )
    
    q2 = Etapes(
        question="Tu bases-tu tes choix surtout sur la logique ?",
        left=q4,
        right=q5
    )
    
    return q2

def build_branch_2(profiles):

    q6 = Etapes(
        question="Les émotions fortes te motivent-elles ?",
        left=profiles['E'],
        right=profiles['F']
    )
    
    q7 = Etapes(
        question="As-tu tendance à éviter les conflits ou les décisions difficiles ?",
        left=profiles['G'],
        right=profiles['H']
    )
    
    q3 = Etapes(
        question="Tu suis plutôt ton instinct dans les situations nouvelles ?",
        left=q6,
        right=q7
    )
    
    return q3


def build_tree():

    profiles = create_profiles()
    branch_1 = build_branch_1(profiles)
    branch_2 = build_branch_2(profiles)
    
    racine = Etapes(
        question="Es-tu plutôt quelqu'un qui réfléchit avant d'agir ?",
        left=branch_1,
        right=branch_2
    )
    
    return racine


# mes 3 fonctions du dessus pour la strcture de mon arbre avec 2 chemins différents puis 4 autres chemins
# 2x4 donc 8 possiblités finales
