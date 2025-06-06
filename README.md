# 42 Poème

Un petit programme qui vérifie si un poème respecte les règles d'un **42 poème**.

## Qu’est-ce qu’un 42 poème ?

Un **42 poème** suit l'une des deux structures suivantes :

* **6 lignes**, **7 mots par ligne**
* **7 lignes**, **6 mots par ligne**

**ET** chaque ligne doit faire **exactement 42 caractères**, espaces inclus.

👉 Les mots sont comptés à la manière de la commande Unix `wc -w` :

> Par exemple, `"j'arrive"` compte comme **un seul mot**, pas deux.

## Utilisation

1. Clone le repo :

   ```bash
   git clone [https://github.com/<ton-nom>/42-poeme.git](https://github.com/Gymnopediese/42poesie.git)
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
