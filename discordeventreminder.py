import pickle
import time
import datetime


_FILENAME = "dates.pkl"     # Je suis sympa "comme même"


class DiscordEventReminder:
    """
    ETAPE 1:
    faire a = DiscordEventReminder.load() pour autaumatiquement gérer les conneries de ficheirs

    ETABE 2:
    add(titre, dd/mm/yyyy), pr ajouter un event
    delete(id) pour suppriemr l'élément avec l'ID id (pas l'index)
    reset() pour tout virer mais ca vire TOUT et DEFINITIVEMENT si pas de sauvegarde du ficheir

    ETAPE ETAPE:
    str(objet), que tu va implementer pour donner le bon résultat

    ETAPE -1:
    linker mes fonctions à des commandes

    ETAPE ?@é#{|$£:; DROP TABLE EVENTS
    On peut niquer le systeme de pleins de facons différentes je pense
    """
    def __init__(self):
        self.dates = []
        self.id = 0

    #   O(1), LES DEVELOPPEURS LE DETESTENT !
    def add(self, titre, date):
        """
        :param date: format dd/mm/yyyy
        :type date: str
        """
        try:
            #   TODO: Bon voila ca donne le timestamp de la date demandée. gère les pbs qui peuvent arriver
            timestamp = time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())
        #   PAS d'exceptions svp, au pire ca ajoute pas
        except Exception:
            return

        self.dates.append((self.id, titre, timestamp))
        self.id += 1
        self.save()

    #   O(n) DEGEULASSE
    def delete(self, id):
        """
        :param id: ID de l'event à suppriemr
        :type id: int
        """
        for i, date in enumerate(self.dates):
            if date[0] == id:
                del self.dates[i]
                self.save()
                return

    #   O(1) super... ca sert à rien
    def reset(self):
        # EVITE D'IMPLEMENTER CA, CA SUPPRIME TOUT
        self.dates = []
        self.id = 0
        self.save()

    def save(self):
        with open(_FILENAME, "wb") as file:
            pickle.dump(obj=self, file=file)

    @staticmethod
    def load():
        try:
            with open(_FILENAME, "rb") as file:
                ohoyo = pickle.load(file)
        except Exception:
            with open(_FILENAME, "wb") as file:
                ohoyo = DiscordEventReminder()
                ohoyo.save()
        assert ohoyo is not None, "GRAVE ERREUR CHARGEMENT FICHIER, VOIR CODE"
        return ohoyo

    def __str__(self):
        res = ""

        for event in self.dates:
            # TODO: amuse toi avec les timestamps pour imprimer le temps restant, la ta le timestamp de la date de l'event
            res += str(event[0]) + ":" + str(event[1]) + " - " + str(event[2]) + "\n"
        return res


if __name__ == "__main__":
    # Connexion au DiscordEventReminder
    a = DiscordEventReminder.load()

    # Ajout d'éléments dans l'objet
    a.add("Deux MIL X 9", "01/01/2019")     # ID:0
    a.add("Id est un", "01/01/2019")        # ID:1

    # délétationnage de l'élément d'ID 1, si il existe
    a.delete(1)     # delete "Id est un"

    # Re ajout
    a.add("ID est 2", "01/01/2019")         # ID:2  /!\ l'ID est TJRS incrémenté de 1 !

    # Voila
    print(a)
