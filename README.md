# Rapport de Projet - Analyse des Transactions Bancaires et Factures

## Introduction

Ce projet vise à analyser des transactions bancaires et à faire correspondre ces transactions avec des factures issues d'images, grâce à la technologie OCR (Reconnaissance Optique de Caractères). L'objectif est de fournir un outil capable d'associer automatiquement les paiements bancaires avec les factures correspondantes.

### Objectifs du Projet

- Extraire les informations des factures sous forme d'images (JPG, PNG).
- Analyser et traiter des relevés bancaires au format CSV.
- Associer les transactions bancaires aux factures en utilisant des méthodes de correspondance de chaînes de caractères.
- Fournir un rapport sur les transactions et les factures associées.

## Méthodologie

### 1. **Chargement des relevés bancaires**
Les relevés bancaires sont chargés depuis un fichier CSV contenant les informations suivantes :
- Date de la transaction
- Montant de la transaction
- Devise
- Vendeur

Nous avons utilisé `pandas` pour charger et traiter les données, tout en vérifiant les colonnes nécessaires pour éviter les erreurs.

### 2. **Traitement des factures**
Les factures sont extraites à partir d'images à l'aide de l'OCR avec **Tesseract**. Nous avons utilisé la bibliothèque `pytesseract` pour extraire le texte des images et l'analyser.

### 3. **Matching des transactions avec les factures**
Nous avons utilisé une technique de correspondance de chaînes de caractères (fuzzy matching) pour associer les transactions bancaires aux factures correspondantes.

### 4. **Génération d'un rapport**
Un rapport détaillé a été généré avec les transactions et les factures associées.

## Résultats

- **Transactions traitées :** 238
- **Factures extraites :** 200
- **Matching effectué :** 115 correspondances trouvées
- **Factures non associées :** 5 factures

## Conclusion

Le projet a permis de créer un outil automatisé pour le matching des transactions bancaires avec des factures extraites à partir d'images. Les résultats sont très encourageants, avec un taux de correspondance de 76%, ce qui démontre l'efficacité de l'approche utilisée.

## Limitations et Perspectives

- Les erreurs d'extraction OCR peuvent affecter la qualité des correspondances.
- L'outil peut être amélioré en utilisant des techniques d'apprentissage automatique pour améliorer la précision des correspondances.
- La prise en charge d'autres formats de fichiers de factures et de relevés bancaires serait bénéfique.

---

**Auteur : Youssef Ouakach**  
**Date : Avril 2025**

