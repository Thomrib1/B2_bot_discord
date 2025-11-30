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
