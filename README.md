<h1 style="text-align: center;">Projet 1: BooksOnline</h1>

![Image of OpenClassrooms](https://onatestepourtoi.com/wp-content/uploads/2020/02/Logo_openclassrooms_onatestepourtoi.jpg)

## Résumé du projet

Écrire un script Python qui visite l'ensemble des pages du site [Books to Scrape](http://books.toscrape.com) <br> et en extrait les informations suivantes :

* product_page_url
* universal_ product_code (upc)
* title
* price_including_tax
* price_excluding_tax
* number_available
* product_description
* category
* review_rating
* image_url

À la fin, le programme renvoit les informations extraites dans un fichier 
[.csv](https://fr.wikipedia.org/wiki/Comma-separated_values) <br> ainsi que toutes les couvertures des livres consultés par le programme sous le format [.jpg](https://fr.wikipedia.org/wiki/JPEG)

# Configurer un environnement virtuel Python

## Windows 10

La création d'environnements virtuels est faite en exécutant la commande [venv](https://docs.python.org/fr/3/library/venv.html) :

```bash
python -m venv \path\to\new\virtual\venv
```

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

```bash
.\venv\Scripts\activate.bat
```

Utilisez le gestionnaire de packages [pip](https://pip.pypa.io/en/stable/) pour installer les paquets requis :

```bash
pip install -r requirements.txt
```

Pour lancer le programme :

```bash
py .\all_books.py
```


## Linux

La création d'environnements virtuels est faite en exécutant la commande [venv](https://docs.python.org/fr/3/library/venv.html) :

```bash
python3 -m venv \path\to\new\virtual\venv
```

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

```bash
source venv/bin/activate
```

Utilisez le gestionnaire de packages [pip](https://pip.pypa.io/en/stable/) pour installer les paquets requis :

```bash
pip install -r requirements.txt
```

Pour lancer le programme :

```bash
python3 all_books.py
```
