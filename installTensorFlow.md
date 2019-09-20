## Installation de Tensor Flow

Nous utiliserons **Tensor Flow 2.0-rc1**.
Celui ci utilise **Python 3.5 64 bits** pour fonctionner.

Installez donc python 3.5 (64 bits) sur votre machine.

### Création d'un environnement virtuel pour python

Puis, pour éviter de mixer les versions de pythons et les librairies,
nous utiliserons un environnement virtuel pour python.
- Ouvrez un terminal (ou l'invite de commande sous windows).
- placez vous dans le répertoire ou vous voulez travailler

Si *PATH* contient le chemin de votre python 3.5, on crée un environnement
virtuel *monVenv* dans le répertoire courant comme suit :

Sous windows
```
PATH\python.exe -m venv monVenv
```
Sous Linux :
```
python35 -m venv monVenv
```

Pour des raisons pratiques liées à git, nous prendrons *venv* comme nom de
répertoire pour l'environnement virtuel dans le repertoire courant.
La commande adaptée est donc

sous windows :
```
PATH\python -m venv venv
```
Sous Linux :
```
python35 -m venv venv
```

### Activation d'un environnement virtuel pour python

Sous windows On active cet environnement virtuel en appelant
```
venv\Scripts\activate.bat
```
Sous Linux :
```
source venv/bin/activate
```

On peut vérifier que la commande python appelle maintenant le python de cet
environnement virtuel :
```
python --version
```
doit répondre
```
python 3.5 64 bits
```

### Mise a jour de pip

Pip est le gestionnaire de paquets de python.
Mettez le a jour quand vous créez un environnement virtuel
(sans quoi l'installation de Tensor Flow ne fonctionnera pas)
```
python -m pip install --upgrade pip
```


### Installation des modules pythons nécessaires aux TP.

Il vous faut installer
- tensorFlow
- matplotlib
- plein d'autres choses

l'installation d'un module se fait par la commande
```
python -m pip install NomModule
```

Pour simplifier un peu, j'ai regroupé dans un fichier les noms des modules
et leurs numéros de versions dans ce fichier :
[requirements.txt](requirements.txt)
Copiez ce fichier dans votre répertoire courant (pas le répertoire *venv*)


Vous pouvez installer tout en une commande :
```
python -m pip install -r requirements.txt
```

Attendez un peu et ca doit être bon.
