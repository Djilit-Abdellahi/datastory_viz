"""
Fichier de démonstration de la bibliothèque datastory_viz
À utiliser pour vos captures d'écran du rendu !
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datastory_viz as dsv

# Données de test
np.random.seed(42)

print("=== Démonstration de datastory_viz ===\n")

# 1. LINE CHART
print("1. Création d'un graphique linéaire...")
months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin']
sales = [120, 135, 125, 160, 180, 195]
fig1, ax1 = dsv.styled_line(
    x=months,
    y=sales,
    title="Évolution des Ventes (2024)",
    xlabel="Mois",
    ylabel="Ventes (K€)",
    highlight_point=5  # Highlight Juin
)
plt.savefig('demo_line.png')
plt.show()

# 2. BAR CHART
print("2. Création d'un graphique à barres...")
products = ['Produit A', 'Produit B', 'Produit C', 'Produit D', 'Produit E']
revenues = [450, 320, 580, 210, 390]
fig2, ax2 = dsv.styled_bar(
    categories=products,
    values=revenues,
    title="Revenus par Produit",
    ylabel="Revenus (K€)",
    orientation='horizontal',
    highlight_index=2  # Highlight Produit C (meilleur)
)
plt.savefig('demo_bar.png')
plt.show()

# 3. SCATTER PLOT
print("3. Création d'un nuage de points...")
x_data = np.random.randn(100) * 10 + 50
y_data = x_data * 1.5 + np.random.randn(100) * 15 + 20
fig3, ax3 = dsv.styled_scatter(
    x=x_data,
    y=y_data,
    title="Corrélation: Budget Marketing vs. Ventes",
    xlabel="Budget Marketing (K€)",
    ylabel="Ventes (K€)",
    show_trend=True
)
plt.savefig('demo_scatter.png')
plt.show()

# 4. HEATMAP
print("4. Création d'une heatmap...")
data_matrix = np.random.rand(5, 6) * 100
df_heatmap = pd.DataFrame(
    data_matrix,
    index=['Équipe A', 'Équipe B', 'Équipe C', 'Équipe D', 'Équipe E'],
    columns=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']
)
fig4, ax4 = dsv.styled_heatmap(
    data=df_heatmap,
    title="Performance par Équipe et Trimestre",
    xlabel="Trimestre",
    ylabel="Équipe",
    fmt='.0f'
)
plt.savefig('demo_heatmap.png')
plt.show()

# 5. HISTOGRAM
print("5. Création d'un histogramme...")
ages = np.random.normal(35, 10, 500)
fig5, ax5 = dsv.styled_histogram(
    data=ages,
    bins=30,
    title="Distribution des Âges des Clients",
    xlabel="Âge",
    ylabel="Nombre de Clients",
    show_kde=True
)
plt.savefig('demo_histogram.png')
plt.show()

# 6. BOXPLOT
print("6. Création d'un boxplot...")
group1 = np.random.normal(100, 15, 100)
group2 = np.random.normal(110, 20, 100)
group3 = np.random.normal(95, 12, 100)
fig6, ax6 = dsv.styled_boxplot(
    data=[group1, group2, group3],
    labels=['Méthode A', 'Méthode B', 'Méthode C'],
    title="Comparaison des Résultats par Méthode",
    ylabel="Score de Performance"
)
plt.savefig('demo_boxplot.png')
plt.show()

print("\n✅ Tous les graphiques ont été générés avec succès !")
print("📁 Fichiers sauvegardés : demo_line.png, demo_bar.png, etc.")