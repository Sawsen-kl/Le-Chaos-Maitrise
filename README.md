# Projet CasaMode - Exercice "Le Chaos Maîtrisé" 🧪

## ✅ Rappel des Rôles de l’équipe

- **Amine** – Product Owner (PO)
- **Canada** – Scrum Master
- **Sawsen** – DevOps

---

## 🔄 Daily Scrum du 8 juillet 2025

### **Amine**
- **Hier** : J’ai mis à jour le backend (signup/login), et organisé le dépôt Git.
- **Aujourd’hui** : Je vais aider à la gestion des branches, faire les revues et préparer la remise du sprint.
- **Blocages** : Aucun pour l’instant.

### **Sawsen**
- **Hier** : J’ai préparé le setup initial avec `.gitignore`, `requirements.txt` et Flask.
- **Aujourd’hui** : Je vais ajouter la gestion des erreurs sur l’API et tester les routes.
- **Blocages** : Problème de connexion locale avec PostgreSQL (résolu).

### **Canada**
- **Hier** : J’ai configuré la protection de `main` et ouvert les premières PR.
- **Aujourd’hui** : Je vais faire les merges, surveiller les conflits et vérifier les tests.
- **Blocages** : Aucun, tout roule.

---

## 🌿 Branches créées

- `feature/signup-endpoint` – Ajout du formulaire d’inscription (Amine)
- `feature/login-endpoint` – Route sécurisée de login utilisateur (Canada)
- `feature/reset-password` – Route de réinitialisation mot de passe (Sawsen)

---

## 🔁 Protection GitHub mise en place

✅ `main` protégée avec "Require pull request before merging"  
✅ Aucun push direct accepté  
✅ Toutes les PRs ont été relues et commentées avant merge  

---

## 📌 Merges et Reviews

Chaque PR a été revue par un autre membre de l’équipe :

- `feature/signup-endpoint` – Revue par Canada → **LGTM**
- `feature/login-endpoint` – Revue par Sawsen → **LGTM**
- `feature/reset-password` – Revue par Amine → **LGTM**

---

## 📌 Bonus

- `.gitignore` généré (stack : Python/Flask/PostgreSQL)
- Issue ouverte : "Frontend - création de la page login" (non encore assignée)
