"""
Nous recevons des int de la part de Tino (réponse de l'utilisateur), et nous renvoyons des chaines de caractères string à Tino.
"""

import sys
sys.path.insert(1, '../model')
import model as md

class Cockpit:
    VFR = 'Light VFR'
    IFR = 'Light IFR'
    MH = 'Medium and Heavy'
    DK = 'Don\'t know'
    cockpit = {0: VFR, 1: IFR, 2: MH, 3: DK}

class Categories:
    Fx = 'FlytX'
    Co = 'Connectivity'
    Localisation = 'Localisation and Primary Reference'
    Surveillance = 'Surveillance'
    RadioComNavAudio = 'Radio Communication Navigation and Audio System'
    AutoPilot = 'Autopilot System'
    Extension = 'Extension'
    DK = 'Don\'t know'
    Piece = {0: Fx, 1: Co, 2: Localisation, 3: Surveillance, 4: RadioComNavAudio, 5: AutoPilot, 6: Extension, 7: DK}

class Question:
    """
    Class allows programm to ask many questions with different proposition.
    It take int as a parameter, return string or int
    """
    cock = Cockpit()
    cat = Categories()

    def FirstQuestion(self):
        print("Voulez-vous un cockpit ou une pièce détachée ?")
        a = input() #a = 0 or 1, 0 = Cockpit / 1 = PieceDetache
        a = int(a)
        return a

    def QuestionCockpitCat(self):
        print("Quel est la catégorie du cockpit que vous souhaitez acheter ?")
        for i in self.cock.cockpit:
            print(self.cock.cockpit[i])
        a = input() #a = 0, 1, 2, or 3
        a = int(a)
        if a == 3:
            print('Nous allons vous aider à trouver le cockpit de vos rêves')
            print(q.impress_customer())
            return
        print('lien vers un cockpit ' + self.cock.cockpit[a])
        return self.cock.cockpit[a]

    def QuestionDetache(self):
        print("Avez-vous déjà acheté ce produit ?")
        a = input() # a = 1 for yes, or a = 0 for No.
        a = int(a)
        return a


    def QuestionPieceCat(self, a):
        """
        Argument :
        ==========
        a is an int, it indicate if we use the first question or the second
        a == 1 : means that the product has been purchased before
        a == 0 : means that the product has never been purchased
        """
        if a == 1:
            print("Dans quelle catégorie l’article que vous avez déjà acheté est-il situé ?")
        else:
            print("Dans quelle catégorie l’article que vous voulez acheter est-il situé ?")

        for i in self.cat.Piece:
            print(self.cat.Piece[i])
        b = input() #b = [0,7]
        b = int(b)
        #Voir dans l'historique du client

        if a == 1 and b != 7:
            print('lien vers l\'article le plus acheté dans la catégorie : ' + self.cat.Piece[b]) #TODO Voir dans l'historique du client après
            print('Est-ce bien cet article ?')
            x = input()
            x = int(x)
            if x == 0:
                print('lien vers l\'article le deuxième plus acheté dans la catégorie : ' + self.cat.Piece[b])
            elif x == 1:
                print('Great, we are happy to make you happy')
        elif a == 1 and b == 7:
            print('Trouver les 3 premiers articles de catégorie différente les plus achetés de son historique') #TODO Voir dans l'historique du client après
        elif a == 0 and b != 7:
            print('liste de lien vers les article de la catégorie : ' + self.cat.Piece[b]) #TODO Machine Learning 2, to precise the article, in particulary for the categories FlytX, Radio and Communication
            # Trouver un article que le client n'a jamais acheté dans la categorie b
            # b = predict() function that asks questions and return an an article
            # return Lien vers article
        elif a == 0 and b == 7:
            print('Nous vous invitons à vous renseigner sur les différentes pièces détachées de cockpit que nous proposons, à bientôt !')
            print('Lien vers une description des différentes catégories de pièces détachées') #Il ne nous resterai que 2 questions pour déterminer un article parmis tous les choix possibles
        return self.cat.Piece[b]

    def Customisation(self):
        """
        return the list which correspond the cockpit customized with each feature enter by the customers
        """
        cockpit = [] #liste
        IDU = ['IDU']
        print('Choisir le nombre de ' + IDU[0])
        print('Choisir un nombre entre 1 et 4')
        a = input()
        a = int(a)
        cockpit.append(a)

        features = ['Primary Flight Display & Navigation (PFD/ND)', 'Synthetic Vision System (SVS)', 'Digital Map', 'Enhanced System Pages (EWD)', 'Basic System Pages', \
                    'High End Flight Management System (FMS)', 'Basic Flight Management System (FMS)', 'Flight Warning System (FWS)', 'Centralised Maintenance System (CMS)', \
                    'Cursor Control Device (CCD)', 'Standby Instrument (STDBY)', 'Flight & Voice data recorder (VDR)', 'Tablet Universal Adaptor', 'Secure Server', \
                    'Satellite Communication', 'Air Data Unit & probes (ADU)', 'Global Navigation System (GNSS)', 'Radio Altimeter & antennas (RA)', \
                    'Terrain Awareness Warning System (TAWS or HTAWS)', 'Traffic Collision Avoidance System (TCAS)', 'Traffic Advisory System (TAS)', 'Mode S Transponder (XPDR)', \
                    'Weather Radar (WXR)', 'Audio System', 'Very high Frequency Radio Terminal (VHF)', 'VHF Omnidirect. Range & Instrument Landing System (VOR/ILS)', \
                    'Automatic Direction Finder (ADF)', 'Distance Measuring Equipment (DME)', 'Emergency Locator Transmitter (ELT)', 'High Frequency Terminal (HF)', \
                    '3-Axis Autopilot System', '4-Axis Autopilot System', 'Localizer Performance with Vertical Guidance (LPV)', 'Search & Rescue System (SAR)', \
                    'Helicopter Emergency Medical Service (HEMS)', 'FLIR (camra / law enforcement)', 'VIP incl SATCOM', 'Tablet for electronic Flight Bag (Thales Pad)', \
                    'Enhanced Vision System (EVS)']

        for i in features:
            print('Choisir le nombre de ' + i)
            a = input()
            a = int(a)
            cockpit.append(a)
        return cockpit

    def impress_customer(self):
        """
        predict his cockpit
        """
        liste = self.Customisation()
        output = md.predict(liste)
        print(" ========  LE COCKPIT QUI SE RAPPROCHE LE PLUS DES CARACTERISTIQUES DEMANDEES EST LE : ====== ")
        return md.predictToString(output)

if __name__ == '__main__':
    """
    Le machine learning est nécessaire dans deux cas :
    - Le cas où le client veut un cockpit mais qu'il ne connaît pas la catégorie de celui-ci
    - Le cas où le client veut un article qu'il n'a jamais acheté mais qu'il connait la catégorie de cet article (Natural Langage Processing)
    """
    q = Question()
    a = q.FirstQuestion()
    if a == 0:
        q.QuestionCockpitCat()
    elif a == 1:
        c = q.QuestionDetache()
        q.QuestionPieceCat(c)

    print('FIN')

