L'application est visible sur le [Streamlit Cloud](https://cyrilbruyere-streamlit-france-energy-app-m8bme7.streamlitapp.com/).

### Configuration spécifique pour l'application sur le Streamlit Cloud :

Les fichiers **requirements.txt** et **packages.txt** sont dédiés à l'application hébergée sur le Streamlit Cloud et ne permettent pas une configuration correcte de l'environnement de travail.

### Configuration de l'environnement de développement :

Pour une configuration sous Windows, le fichier à utiliser pour la création de l'environnement est le fichier **requires.txt** qui se trouve dans le répertoire ./requirements

**NOTA BENE :**

2 packages d'installation nécessaires à l'installation de Geopandas ne sont pas pris en charge par l'opération pip install pour les dépendances de Geopandas car elles ne sont pas disponibles sur PyPi.
Il est nécessaire de se procurer ces 2 packages par ailleurs, sous forme de wheels. Elles ne sont pas fournies ici.

Pour l'installation proposée dans le fichier requires.txt, il est nécessaire de spécifier le chemin de localisation de ces 2 wheels.
Il faudra corriger l'emplacement en fonction de la configuration du chemin de chacun.
Dans la version en ligne, les wheels se trouvent dans un répertoire wheels créé spécifiquement.
