# 📊 datastory_viz

Bibliothèque Python de visualisation de données appliquant les principes du **data storytelling** enseignés dans le cours DEML 2025/2026.

## 🎯 Principes Appliqués

✅ **Data-Ink Ratio** : Maximisation du ratio données/encre (pas de chart junk)  
✅ **Attributs Pré-attentifs** : Utilisation stratégique de la couleur, taille, position  
✅ **Gestalt** : Proximité, similarité, clôture, connexion  
✅ **Best Practices** : Axe à zéro pour bar charts, pas de 3D, lisibilité maximale  

## 📦 Installation
```bash
pip install -e .
```

## 🚀 Utilisation
```python
import datastory_viz as dsv

# Graphique linéaire
dsv.styled_line(
    x=[1, 2, 3, 4, 5],
    y=[10, 15, 13, 17, 20],
    title="Mon Graphique",
    highlight_point=4
)

# Graphique à barres
dsv.styled_bar(
    categories=['A', 'B', 'C'],
    values=[10, 20, 15],
    title="Comparaison",
    highlight_index=1
)
```

## 📊 Graphiques Disponibles

- `styled_line()` : Graphiques linéaires
- `styled_bar()` : Graphiques à barres
- `styled_scatter()` : Nuages de points
- `styled_heatmap()` : Heatmaps
- `styled_histogram()` : Histogrammes
- `styled_boxplot()` : Boxplots

## 👨‍💻 Auteur

Djilit Abdellahi - DEML 2025/2026

## 📄 License

MIT License
