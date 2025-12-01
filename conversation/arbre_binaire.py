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
        'A': Etapes(result="Penseur Stable --> Tes choix sont logiques, prudent tu restes méthodique"),
        'B': Etapes(result="Analyste Explorateur --> Curieux sur tout les aspects, aucun secret n'existe pour toi"),
        'C': Etapes(result="Empathique Introspectif --> Sensibles et profonds tu restes très émotionnel sans le montrer"),
        'D': Etapes(result="Sage Pragmatique --> Calme et observateur seuls les actions réfléchies et concrètes sont justifiés a tes yeux"),
        'E': Etapes(result="Passionné Spontané --> instinctif, intense, expressif"),
        'F': Etapes(result="Aventurier Calme --> spontané mais posé, adaptable"),
        'G': Etapes(result="Diplomate Fuyant --> Tu recherches l'equilibre parfait pour éviter les tensions"),
        'H': Etapes(result="Volontaire Direct --> La vérité est un principe, affirmé va droit au but")
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

class ConversationManager:
    def __init__(self):
        self.tree = build_tree()
        self.user_conversations = {}
    
    def start_conversation(self, user_id):
        self.user_conversations[user_id] = self.tree
        return self.tree.question
    
    def is_in_conversation(self, user_id):
        return user_id in self.user_conversations
    
    def abandon(self, user_id):
        if user_id in self.user_conversations:
            del self.user_conversations[user_id]
    
    def answer(self, user_id, response):
        if user_id not in self.user_conversations:
            return "Tape !help pour commencer le questionnaire."
        
        current = self.user_conversations[user_id]
        
        if current.result:
            del self.user_conversations[user_id]
            return current.result
        if response.lower() == "oui":
            self.user_conversations[user_id] = current.left
            next_node = current.left
        elif response.lower() == "non":
            self.user_conversations[user_id] = current.right
            next_node = current.right
        else:
            return " Réponds par 'oui' ou 'non' uniquement."
        if next_node.result:
            del self.user_conversations[user_id]
            return next_node.result
        return next_node.question
    
    def reset(self, user_id):
        return self.start_conversation(user_id)
