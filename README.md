# Site du Dr Andrei Bursuc

Version préparée le 13 septembre 2026. Site statique bilingue prêt pour GitHub Pages. Le site actuel et les dépôts GitHub existants n’ont pas été modifiés. Aucune mention de la Rive-Sud.

## Voir le résultat avant publication

Décompresser le ZIP, puis ouvrir **index.html** dans un navigateur sur ordinateur. Conserver tous les dossiers à côté du fichier. Les pages françaises et anglaises, les photos et les six outils sont inclus. Les vidéos YouTube nécessitent une connexion Internet; certains navigateurs limitent les vidéos dans un fichier ouvert localement. Les vérifier après publication.

## 1. Déposer le nouveau site sur GitHub

1. Se connecter au compte **mrandreibursuc-create** sur GitHub, de préférence sur ordinateur.
2. Créer un **nouveau dépôt public** nommé **andreibursuc-site**. Ne pas remplacer le dépôt `Nerve-explorer`.
3. Avec **Add file → Upload files** (ou « uploading an existing file » dans un dépôt vide), déposer **le contenu décompressé** : `index.html`, les dossiers `assets`, `education`, `en`, `tools`, `home`, `data`, `scripts`, et les autres fichiers. Ne pas déposer uniquement le ZIP ni un dossier parent contenant tout.
4. Enregistrer avec **Commit changes**. Le fichier `index.html` doit être directement à la racine du dépôt.
5. Ouvrir **Settings → Pages**. Choisir **Deploy from a branch**, puis **main**, dossier **/(root)**, et enregistrer.
6. Attendre la publication. GitHub affichera le lien du site. Pour ce nom de dépôt, l’adresse attendue est `https://mrandreibursuc-create.github.io/andreibursuc-site/`.

[Configurer la publication GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

À ce stade, **andreibursuc.com affiche toujours le Google Site**. Vérifier le nouveau site : navigation FR/EN, téléphone, courriel, photos, six outils et vidéos. Sur téléphone, vérifier le menu et le bouton « Ouvrir en pleine page » des outils. Les applications éducatives conservent leur propre mise en page.

## 2. Préparer le domaine

Le domaine et l’hébergement sont deux choses distinctes. Garder l’abonnement au domaine; aucun transfert de registraire n’est nécessaire. Le prestataire qui gère actuellement les DNS n’a pas été identifié dans ce travail.

Dans les paramètres du **compte GitHub**, rubrique **Pages**, vérifier le domaine `andreibursuc.com` avec le TXT fourni par GitHub. Conserver ce TXT. [Vérification du domaine](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages).

Ensuite, dans **le dépôt andreibursuc-site → Settings → Pages → Custom domain**, saisir **www.andreibursuc.com**, puis enregistrer. GitHub créera le fichier `CNAME`. Ce fichier est volontairement absent du ZIP pour permettre le premier essai à l’adresse GitHub.

## 3. Faire pointer l’adresse vers GitHub

**Configurer d’abord le domaine dans GitHub**, puis modifier les DNS chez leur gestionnaire. Garder une copie des valeurs actuelles pour un retour arrière.

| Type | Nom / hôte | Valeur |
|---|---|---|
| CNAME | www | mrandreibursuc-create.github.io |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

`@` désigne le domaine sans www; certains interfaces demandent de laisser ce champ vide. Le CNAME contient le nom ci-dessus, **sans https://, sans chemin et sans nom de dépôt**.

Remplacer les anciennes destinations web conflictuelles pour `www` et `@`, y compris d’éventuels AAAA ou redirections vers Google Sites. **Conserver les MX et les TXT de messagerie et de vérification.** Ne pas changer les serveurs de noms pour cette opération.

Dans GitHub Pages, attendre la validation DNS et activer **Enforce HTTPS** dès qu’il est disponible. La propagation DNS et l’émission du certificat peuvent prendre jusqu’à 24 heures. Vérifier les adresses avec et sans www; GitHub redirige vers la version choisie quand les deux sont correctement configurées. [Configuration officielle du domaine](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## 4. Retirer le Google Site seulement après la bascule

Quand **https://www.andreibursuc.com** affiche le nouveau site avec HTTPS, vérifier aussi l’onglet Éducation et les anciens liens partagés.

La modification des DNS remplace déjà le site affiché à cette adresse. Il n’est pas nécessaire de supprimer immédiatement le document Google Sites. Conserver une copie privée. Pour retirer aussi la publication sur l’adresse native `sites.google.com`, utiliser le menu de publication de Google Sites pour annuler la publication, si cette option est proposée, ou restreindre l’accès au site publié. [Publication et partage Google Sites](https://support.google.com/sites/answer/6372880?hl=fr).

Les anciens chemins sous **andreibursuc.com/education/** sont conservés. `/home` renvoie vers l’accueil. En revanche, un ancien lien **sites.google.com/...** ne peut pas être redirigé par le nouveau site : le corriger là où il a été partagé, ou conserver provisoirement une page Google Sites indiquant la nouvelle adresse avant de la retirer.

## 5. Mettre Google à jour

Dans Google Search Console, garder la propriété du domaine existante ou la vérifier. Soumettre `https://www.andreibursuc.com/sitemap.xml`, inspecter l’accueil et demander son indexation. Le nouveau site contient des titres FR/EN, des descriptions, des liens de langue, des adresses canoniques, une fiche structurée Person et un favicon AB au format PNG.

Le classement, la photo dans les résultats et l’affichage du favicon restent décidés par Google. Le changement de site ne garantit pas une première position. [Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start) · [Favicon](https://developers.google.com/search/docs/appearance/favicon-in-search).

## Modifications ultérieures

- **Coordonnées et liens** : modifier `data/site.json`, puis lancer `python3 scripts/build.py` et publier les pages régénérées. Le JSON seul ne modifie pas les pages déjà générées.
- **Présentation et textes** : `scripts/build.py`.
- **Style** : `assets/style.css`; menu mobile : `assets/site.js`.
- **Photos** : `assets/portrait.jpg`, `emg.jpg`, `spasticite.jpg`, `infiltrations.jpg`, `migraine.jpg`.
- **Outils** : les six fichiers autonomes sont dans `tools/`. La liste et les pages d’accès sont générées depuis `TOOLS` dans `scripts/build.py`.

On peut demander ces changements à l’assistant; il n’est pas nécessaire de modifier soi-même le code. Les outils sont des copies des dépôts `Nerve-explorer`, `fascicle` et `nerveblockerfinal` : les futures modifications de ces dépôts ne seront pas automatiquement reportées ici. Modifier les copies publiées dans ce nouveau dépôt, ou effectuer une synchronisation explicite. Garder le fichier `CNAME` créé par GitHub lors des futures mises à jour.

## Vérification effectuée

Les liens locaux, fichiers d’images, chemins historiques, métadonnées JSON et la syntaxe JavaScript ont été vérifiés. Les fichiers actifs des outils sont identiques aux sources récupérées sur GitHub. Les anciens outils séparés de blocs ont été remplacés par des redirections vers la version combinée. Aucun audit médical ni test complet des interactions de ces outils n’a été effectué. La mise en page responsive est implémentée; le rendu dans les navigateurs et les vidéos devront être vérifiés sur l’adresse GitHub avant de modifier les DNS.

## Modifications de la version 2

- Coordonnées de la clinique visibles dans la présentation du haut, avec liens de téléphone, courriel et itinéraire. Le bouton principal appelle directement la clinique.
- Hauteur des photos rendue proportionnelle à leur largeur : les cinq images existantes sont conservées sans régénération.
- Ajout de l’explorateur des fascicules intraneuraux FR/EN.
- Un seul explorateur de blocs moteurs, membres supérieurs et inférieurs. Les anciennes adresses conduisent au nouvel outil.
- FAQ de dix réponses par langue, dans `/faq/` et `/en/faq/`, avec liens depuis l’accueil et sources médicales. Les textes se modifient dans `scripts/faq_content.py`, puis se régénèrent avec `python3 scripts/build.py`. Aucun avis de validation médicale par le Dr Bursuc n’est ajouté.

Pour mettre à jour un dépôt existant, remplacer les fichiers par le contenu de ce ZIP **en conservant le CNAME existant**. Déposer également les nouveaux dossiers `faq`, les sous-dossiers ajoutés à `education` et `en`, ainsi que les nouveaux fichiers `tools/fascicle.html` et `tools/motor-blocks.html`. Les fichiers d’anciens blocs doivent aussi être remplacés pour que leurs redirections soient actives.

### FAQ et visibilité

Le texte des réponses est présent dans le HTML, consultable sans JavaScript. Les pages FR/EN ont leurs titres, descriptions, adresses canoniques, liens de langue et entrées dans le sitemap. La FAQ répond à des besoins de lecture et de découverte; elle ne garantit ni trafic ni citation par une IA. Google a retiré les résultats enrichis de FAQ depuis le 7 mai 2026; aucun affichage de ce type n’est promis. [Mises à jour Google](https://developers.google.com/search/updates) · [Fonctions IA de Google Search](https://developers.google.com/search/docs/appearance/ai-features).
