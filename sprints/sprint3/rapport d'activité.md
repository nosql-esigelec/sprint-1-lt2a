### Rapport d'Activité - Sprint 3

**Titre** : Déploiement sur Google Cloud Platform avec Terraform et Ansible

**Date** : [25/11/2023]

**Équipe** :
LADIBE SAMUEL\
  TEGUE YOMBI ELISEE\
  AIZANSI SYDNEY CAREL\
  AKPOVO VIGNON JEFFERSON

---

#### 1. Objectifs du Sprint
- Mise en place d'une infrastructure cloud robuste et évolutive sur Google Cloud Platform (GCP) en utilisant Terraform pour la gestion des ressources.
- Automatisation de la configuration des serveurs et des services avec Ansible, en mettant l'accent sur la sécurité et l'efficacité.
- Déploiement d'une base de données MongoDB et d'une base données Neo4J dans un environnement conteneurisé.

#### 2. Résumé des Activités
- **Terraform** : Création de modules Terraform pour déployer des instances de Compute Engine, configurer le réseau VPC et les règles de pare-feu. 
  - Exemple : Provisionnement de deux instances VM pour héberger des nœuds MongoDB et deux instances pour héberger des noeuds Neo4J avec des disques SSD persistants pour le stockage des données.
- **Ansible** : Développement de playbooks Ansible pour l'installation et la configuration de Docker et MongoDB sur les VMs.
  - Exemple : Playbook pour installer Docker, tirer l'image MongoDB, et configurer les variables d'environnement nécessaires pour l'authentification.

#### 3. Résultats et Livrables
- **Infrastructure GCP** :
  - Quatre instances VM dans un réseau VPC sécurisé avec des règles de pare-feu limitant l'accès aux ports nécessaires.
- **Automatisation avec Ansible** :
  - Playbooks pour la configuration initiale des serveurs, l'installation de Docker, et le déploiement de MongoDB et Neo4J.
- **Documentation** :
  - Documentation détaillée sur la structure du code Terraform et les étapes des playbooks Ansible.

#### 4. Défis et Solutions
- **Défi** : Difficulté à gérer les dépendances entre ressources dans Terraform.
  - **Solution** : Utilisation de l'attribut `depends_on` pour assurer un ordre de création approprié.
- **Défi** : Problèmes de connexion initiale avec Ansible due à des changements de clés SSH.
  - **Solution** : Mise à jour des clés SSH et utilisation de la commande `ssh-keyscan` pour ajouter automatiquement les hôtes à `known_hosts`.
- **Défi** : Problèmes de commandes de shell mongo
  - **Solution** : Documentation sur l'utilisation de l'image mongodb et application de la commande shell `mongosh` pour les version 4+ et récentes.
- **Défi** : Gestion de la configuration de deux ports pour la base de données Neo4J
  - **Solution** : ajout des variables d'environnement au démarrage du conteneur pour configurer les adresses ip de connexion bolt et http à chacun des nodes neo4j et aussi la plage d'adresses autorisées à interroger la BD neo4j  

#### 5. Retours d'Expérience et Apprentissages
- Importance de la planification détaillée pour la gestion des ressources cloud.
- Avantages de l'automatisation dans la réduction des erreurs humaines et l'amélioration de l'efficacité.
- Nécessité de tests réguliers pour identifier et résoudre les problèmes rapidement.

#### 6. Prochaines Étapes et Améliorations
- Intégration continue et déploiement continu (CI/CD) pour automatiser davantage les processus de mise à jour.
- Renforcement des mesures de sécurité, notamment par la mise en place de groupes de sécurité plus restrictifs et le chiffrement des données.

---

#### Conclusion
Le sprint 3 a été un succès notable dans l'avancement de notre projet. L'utilisation de Terraform et Ansible pour déployer et configurer notre infrastructure sur GCP a non seulement amélioré notre efficacité mais a également posé les fondations pour une gestion plus agile et sécurisée de notre environnement cloud. Les défis rencontrés ont été des opportunités d'apprentissage précieuses, nous permettant d'affiner nos compétences et notre compréhension des meilleures pratiques dans le déploiement cloud. Alors que nous nous tournons vers le prochain sprint, notre objectif est de continuer à renforcer notre infrastructure, d'améliorer notre pipeline de CI/CD, et de maintenir un haut niveau de sécurité et de performance.