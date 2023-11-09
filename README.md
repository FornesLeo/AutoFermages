# Documentations auto fermages

Bienvenue sur le projet de documentation des fermages.

Ce projet a pour but de créer un programme qui permet d'automatiser le calcul des **fermages** pour chaque bailleurs et de générer des documents (lettres, chèque) présonnaliser pour chaque bailleurs.

## Utilisation

Pour lancer le programme, il suffit de lancer le l'executable **fermage.exe**
Ensuite on rentre l'indice national fournit par le gouvernement français trouvable via internet, exemple : **116,46**

Ensuite on rentre La variation de l'indice national des fermages par rapport à l'année dernière, exemple : **1.53**

Une fois les information rentré, le programme va générer un dossier, exemple : **2023**
A l'intérieur de ce dossier, il y aura:
- une **fiche_résumer** qui contient un récapitulatif sur les 3 dernières année
- un **dossier cheques** qui contient les chèques à envoyer aux bailleurs
- un **dossier lettres** qui contient les lettres à envoyer aux bailleurs

## Ajouter mofiier un bailleur

Pour ajouter un bailleur, il suffit de modifier le fichier **data.csv** qui se trouve dans le dossier **config**.

Vous pouvez l'ouvrir avec un tableur comme Excel ou LibreOffice Calc.

Le fichier est organisé en 3 étapes:

### 1. Les informations du bailleur
- **Nom** : Le nom du bailleur
- **Adresse** : L'adresse du bailleur
- **Code postal Ville** : Le code postal et la ville du bailleur

### 2. Les informations des parcelles
- **Commune** : Le nom de la commune
- **Section** : Le nom de la section
- **Numéro** : Le numéro de la parcelle
- **Superficie** : La superficie de la parcelle en ha

Si un propriétaire possède plusieurs parcelles, il suffit de rajouter une ligne avec les informations de la parcelle a la suite.

### 3. Un saut de ligne pour séparer les bailleurs

exemple:
```csv
Nom Prénom;Adresse;Code Postal Ville;
Secteur Parcel;Section ;Plan ;Surface
;;;
CREMMEL JEAN-PAUL;73 RUE PRINCIPALE;67500 BATZENDORF;
BATZENDORF;36;160/88;0.61
BATZENDORF;36;161/89;5.39
;;;
DISS JEAN;;67270 MINVERSHEIM;
MINVERSHEIM;24;247;0.46
;;;
```

## Installer le programme

**Prérequis**:
Installer [Python](https://www.python.org/downloads/)

Pour installer le programme, il suffit de lancer le fichier **install.bat** qui se trouve à la racine du projet.

## Compiler le programme

Pour compiler le programme, il suffit de lancer le fichier **buil.bat** qui se trouve à la racine du projet.