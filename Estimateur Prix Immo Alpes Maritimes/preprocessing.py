import pandas as pd
import googlemaps

API_KEY = "votreClé"  # Omis pour des raisons de securité
gmaps = googlemaps.Client(key=API_KEY)

dataset = pd.read_csv('./data-ventes-fonciers.csv', sep=';')

listQuartier = []


def get_quartier(objet):
    if objet and len(objet):
        for i in range(len(objet)):
            if objet[i]['types']['neighborhood']:
                return objet[i]['types']['neighborhood']
            return 0

    return 0


for row in dataset.rows:
    adrBrut = [row['No Voie'], row['Type de voie'], row['Voie'], row['Code postal'], row['Commune'], 'France']
    adrParsed = " ".join(adrBrut)
    infoAdr = gmaps.geocode(adrParsed)
    quartier = get_quartier(infoAdr)
    listQuartier.append(quartier)

dataset['Quartier'] = listQuartier

