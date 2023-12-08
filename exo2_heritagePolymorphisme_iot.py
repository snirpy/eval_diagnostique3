class DispositifEclairage:
    def __init__(self, identifiant, type_dispositif):
        self.identifiant = identifiant
        self.type_dispositif = type_dispositif

    def allumer(self):
                print(f"Identifiant de l'ampoule  ({self.identifiant}): Type: {self.type_dispositif}")


class AmpouleIntelligente(DispositifEclairage):
    def __init__(self, identifiant, type_dispositif, intensite_luminosite):
        super().__init__(identifiant, type_dispositif)
        self.intensite_luminosite = intensite_luminosite

    def allumer(self):
        print(f"Ampoule Intelligente ({self.identifiant}): Luminosité {self.intensite_luminosite}%")


class BandeLEDIntelligente(DispositifEclairage):
    def __init__(self, identifiant, type_dispositif, longueur):
        super().__init__(identifiant, type_dispositif)
        self.longueur = longueur

    def allumer(self):
        print(f"Bande LED Intelligente ({self.identifiant}): Longueur {self.longueur} cm")


# Création de trois instances de dispositifs d'éclairage
# Création de trois instances de dispositifs d'éclairage
ampoule_intelligente = AmpouleIntelligente("Lumiere001","Ampoule001", 75)
bande_led_intelligente = BandeLEDIntelligente("Lumiere002","BandeLED001", 120)
dispositif_eclairage = DispositifEclairage("Lumiere003", "Lumière générique")

# Affichage des informations de chaque dispositif en appelant la méthode appropriée
ampoule_intelligente.allumer()
bande_led_intelligente.allumer()
dispositif_eclairage.allumer()