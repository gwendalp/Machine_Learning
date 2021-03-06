# Approche Multiclasse

**Multiclasse :** 
On utilise une approche multiclasse car ici le but n'est pas de séparer un jeu de données en deux classes, mais bien en 10 classes distinctes ({0, 1, ..., 8, 9}).

# Possibilités de la Multiclasse

* Répéter 10 fois un classification (séparation entre les données présentant le chiffre i, et les autres, pour tous les i appartenants à [0, 9])
* Utiliser un réseau de neuronnes qui prends en entrée les différents pixels de l'image et qui sort la probabilité que le chiffré présenté en entrée soit le i-ième chiffre.

# Approche par réseau de neurones

**Réseau de neurones :** On présente en entrée un jeu de données. Celles-ci sont convoluées à l'aide de matrices afin de réduire l'information, et d'avoir en sortie les différentes classes souhaitées. L'idée est de pouvoir concevoir un réseau de neurones qui peut avoir plusieurs couches cachées entre l'entrée et la sortie, ce qui complexifie le réseau, et permet de résoudre des problèmes de classifications plus complexes. Chaque neurone multiplie sa valeur d'entrée par une variable, puis passe le résultat dans une sigmoïde, et on obtient la valeur de sortie du neurone qui va alimenter la couche suivante. Ensuite lors de la phase d'entrainement, on peut comparer le résultat obtenu avec le résultat attendu, et ainsi modifier les coefficients pour ajuster le réseau de neurones.