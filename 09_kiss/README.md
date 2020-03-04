## KISS

![statement](challenge.png)

Pour ce challenge, après avoir regardé en détail les réponses serveur, après avoir téléchargé le template de KISS original et regardé si il n'y avait aucune différence entre le template et les fichiers sur le serveur, nous avons décidé d'utiliser quelques outils.

Une fois que nous avions trouvé le bon outil, c'était évident que nous étions sur la bonne piste. Nous avons donc utilisé **wfuzz** pour tester un tas de pages d'administrations possible sur le site, mais cet outils ne vous donnera rien si vous chercher à la racine du serveur par contre si vous regardez bien l'url qu'on a sur le site, on est dans le dossier "public" on va donc lancer wfuzz dans le dossier "private" en espérant trouver ce qu'on cherche.

```

```
