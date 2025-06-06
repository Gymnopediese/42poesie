# 42 Poème

Un petit programme qui vérifie si un poème respecte les règles d'un **42 poème**.

## Qu’est-ce qu’un 42 poème ?

Un **42 poème** suit l'une des deux structures suivantes :

* **6 vers**, **7 mots par vers**
* **7 vers**, **6 mots par vers**

**ET** chaque vers doit faire **exactement 42 caractères**, espaces inclus.

👉 Les mots sont comptés à la manière de la commande Unix `wc -w` :

> Par exemple, `"j'arrive"` compte comme **un seul mot**, pas deux.

Pour finir, il faut faire rimé les vers avec le paterne de votre choix :

exemples 6 vers:
- a,a,a,b,b,b
- a,a,b,b,c,c
- a,b,a,b,c,c
- a,a,a,a,a,a
- ...

exemples 7 vers:
- a,a,a,b,b,b,b
- a,a,a,a,b,b,b
- a,a,b,b,c,c,c
- ...


## Objectif

Faire un recueil contenant 42 des meuilleurs poème écrit par vos soins !

## Utilisation

1. Clone le repo :

   ```bash
   git clone https://github.com/Gymnopediese/42poesie.git
   ```

2. Place ton poème dans un fichier `.42p`.

3. Lance le programme :

   ```bash
   python3 42poeme.py mon_poeme.42p
   ```

## Exemple

Contenu de `exemple.txt` :

```
lol c'est super dure alors vas falloir attendre avant que j'ai un exemple
```

## Licence

Projet sous licence MIT.
