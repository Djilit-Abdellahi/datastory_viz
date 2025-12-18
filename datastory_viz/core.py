"""
Fonctions de visualisation appliquant les principes du data storytelling
Chaque fonction respecte : data-ink ratio, attributs pré-attentifs, Gestalt
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from .styles import apply_style, get_color, get_categorical_colors

# Appliquer le style au chargement du module
apply_style()


def styled_line(x, y, title="", xlabel="", ylabel="", highlight_point=None, 
                color=None, figsize=(10, 6), show_grid=True):
    """
    Graphique linéaire pour montrer les tendances temporelles
    
    Principes appliqués :
    - Ligne claire pour connexion (Gestalt)
    - Highlight point pour attribut pré-attentif
    - Pas de chart junk
    
    Args:
        x: Liste ou array de valeurs x (souvent temporelles)
        y: Liste ou array de valeurs y
        title: Titre du graphique
        xlabel: Label de l'axe x
        ylabel: Label de l'axe y
        highlight_point: Index du point à mettre en évidence (optionnel)
        color: Couleur personnalisée (optionnel)
        figsize: Taille de la figure
        show_grid: Afficher la grille (par défaut True)
    
    Returns:
        fig, ax: Figure et axes matplotlib
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Couleur par défaut
    line_color = color if color else get_color('primary')
    
    # Tracer la ligne principale
    ax.plot(x, y, color=line_color, linewidth=2.5, marker='o', 
            markersize=5, markerfacecolor=line_color, 
            markeredgewidth=0, alpha=0.9)
    
    # Highlight un point spécifique (attribut pré-attentif : couleur + taille)
    if highlight_point is not None:
        ax.scatter(x[highlight_point], y[highlight_point], 
                  color=get_color('accent'), s=150, zorder=5,
                  edgecolors='white', linewidth=2)
    
    # Titres et labels
    if title:
        ax.set_title(title, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, fontweight='500')
    if ylabel:
        ax.set_ylabel(ylabel, fontweight='500')
    
    # Grille (data-ink ratio : subtile)
    ax.grid(show_grid, alpha=0.3, linewidth=0.5)
    
    # Suppression des spines supérieures et droites (minimalisme)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig, ax


def styled_bar(categories, values, title="", xlabel="", ylabel="", 
               orientation='vertical', highlight_index=None, 
               color=None, figsize=(10, 6)):
    """
    Graphique à barres pour comparaison entre catégories
    
    Principes appliqués :
    - Axe commence TOUJOURS à zéro (best practice du cours)
    - Highlight pour attribut pré-attentif
    - Ordre logique (alphabétique ou par valeur)
    
    Args:
        categories: Liste des noms de catégories
        values: Liste des valeurs correspondantes
        title: Titre du graphique
        xlabel: Label de l'axe x
        ylabel: Label de l'axe y
        orientation: 'vertical' ou 'horizontal'
        highlight_index: Index de la barre à mettre en évidence
        color: Couleur personnalisée
        figsize: Taille de la figure
    
    Returns:
        fig, ax: Figure et axes matplotlib
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Couleurs : toutes neutres sauf la barre en highlight
    colors = [get_color('neutral')] * len(categories)
    if highlight_index is not None:
        colors[highlight_index] = get_color('accent')
    elif color:
        colors = [color] * len(categories)
    else:
        colors = [get_color('primary')] * len(categories)
    
    # Graphique vertical ou horizontal
    if orientation == 'vertical':
        bars = ax.bar(categories, values, color=colors, edgecolor='none')
        if ylabel:
            ax.set_ylabel(ylabel, fontweight='500')
        if xlabel:
            ax.set_xlabel(xlabel, fontweight='500')
        # Rotation des labels si nécessaire
        if len(max(categories, key=len)) > 8:
            plt.xticks(rotation=45, ha='right')
    else:  # horizontal
        bars = ax.barh(categories, values, color=colors, edgecolor='none')
        if xlabel:
            ax.set_xlabel(xlabel, fontweight='500')
        if ylabel:
            ax.set_ylabel(ylabel, fontweight='500')
    
    # Titre
    if title:
        ax.set_title(title, fontweight='bold', pad=20)
    
    # IMPORTANT : Axe commence à zéro (principe du cours)
    if orientation == 'vertical':
        ax.set_ylim(bottom=0)
    else:
        ax.set_xlim(left=0)
    
    # Grille subtile
    ax.grid(True, alpha=0.3, linewidth=0.5, axis='y' if orientation == 'vertical' else 'x')
    
    # Suppression des spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig, ax


def styled_scatter(x, y, title="", xlabel="", ylabel="", 
                   color=None, size=None, highlight_points=None,
                   show_trend=False, figsize=(10, 6)):
    """
    Nuage de points pour montrer les corrélations
    
    Principes appliqués :
    - Taille variable pour attribut pré-attentif
    - Ligne de tendance optionnelle (avec prudence)
    - Couleur pour groupes ou highlight
    
    Args:
        x: Liste ou array de valeurs x
        y: Liste ou array de valeurs y
        title: Titre du graphique
        xlabel: Label de l'axe x
        ylabel: Label de l'axe y
        color: Couleur(s) des points (peut être une liste pour groupes)
        size: Taille(s) des points (peut être une liste)
        highlight_points: Liste d'indices à mettre en évidence
        show_trend: Afficher la ligne de tendance linéaire
        figsize: Taille de la figure
    
    Returns:
        fig, ax: Figure et axes matplotlib
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Couleur par défaut
    if color is None:
        color = get_color('primary')
    
    # Taille par défaut
    if size is None:
        size = 80
    
    # Nuage de points principal
    scatter = ax.scatter(x, y, c=color, s=size, alpha=0.6, 
                        edgecolors='white', linewidth=0.5)
    
    # Highlight des points spécifiques (attribut pré-attentif)
    if highlight_points is not None:
        x_array = np.array(x)
        y_array = np.array(y)
        ax.scatter(x_array[highlight_points], y_array[highlight_points],
                  color=get_color('accent'), s=150, zorder=5,
                  edgecolors='white', linewidth=2)
    
    # Ligne de tendance (à utiliser avec précaution selon le cours)
    if show_trend:
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        ax.plot(x, p(x), color=get_color('alert'), 
               linestyle='--', linewidth=2, alpha=0.7,
               label=f'Tendance: y={z[0]:.2f}x+{z[1]:.2f}')
        ax.legend()
    
    # Titres et labels
    if title:
        ax.set_title(title, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, fontweight='500')
    if ylabel:
        ax.set_ylabel(ylabel, fontweight='500')
    
    # Grille subtile
    ax.grid(True, alpha=0.3, linewidth=0.5)
    
    # Suppression des spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig, ax


def styled_heatmap(data, title="", xlabel="", ylabel="", 
                   cmap='Blues', annot=True, fmt='.2f', figsize=(10, 8)):
    """
    Heatmap pour montrer les patterns dans les données matricielles
    
    Principes appliqués :
    - Couleur séquentielle ou divergente appropriée
    - Annotations pour précision
    - Pas de bordures excessives
    
    Args:
        data: DataFrame pandas ou array 2D
        title: Titre du graphique
        xlabel: Label de l'axe x
        ylabel: Label de l'axe y
        cmap: Colormap (par défaut 'Blues' séquentielle)
        annot: Afficher les valeurs dans les cellules
        fmt: Format des annotations
        figsize: Taille de la figure
    
    Returns:
        fig, ax: Figure et axes matplotlib
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Créer la heatmap
    sns.heatmap(data, annot=annot, fmt=fmt, cmap=cmap,
                cbar_kws={'shrink': 0.8},
                linewidths=0.5, linecolor='white',
                square=False, ax=ax)
    
    # Titres et labels
    if title:
        ax.set_title(title, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, fontweight='500')
    if ylabel:
        ax.set_ylabel(ylabel, fontweight='500')
    
    # Rotation des labels
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    plt.tight_layout()
    return fig, ax


def styled_histogram(data, bins=30, title="", xlabel="", ylabel="Fréquence",
                     color=None, show_kde=False, figsize=(10, 6)):
    """
    Histogramme pour montrer la distribution des données
    
    Principes appliqués :
    - Bins appropriés (pas trop, pas trop peu)
    - KDE optionnelle pour smooth pattern
    - Pas de bordures excessives
    
    Args:
        data: Liste ou array de valeurs
        bins: Nombre de bins ou 'auto'
        title: Titre du graphique
        xlabel: Label de l'axe x
        ylabel: Label de l'axe y (défaut: 'Fréquence')
        color: Couleur personnalisée
        show_kde: Afficher la courbe de densité (KDE)
        figsize: Taille de la figure
    
    Returns:
        fig, ax: Figure et axes matplotlib
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Couleur par défaut
    hist_color = color if color else get_color('primary')
    
    # Histogramme
    n, bins_edges, patches = ax.hist(data, bins=bins, color=hist_color, 
                                     alpha=0.7, edgecolor='none')
    
    # KDE optionnelle (courbe lissée)
    if show_kde:
        from scipy import stats
        density = stats.gaussian_kde(data)
        xs = np.linspace(min(data), max(data), 200)
        density_values = density(xs)
        # Scale to match histogram height
        density_values = density_values * (n.max() / density_values.max())
        ax.plot(xs, density_values, color=get_color('accent'), 
               linewidth=2.5, label='Densité (KDE)')
        ax.legend()
    
    # Titres et labels
    if title:
        ax.set_title(title, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, fontweight='500')
    if ylabel:
        ax.set_ylabel(ylabel, fontweight='500')
    
    # Grille subtile
    ax.grid(True, alpha=0.3, linewidth=0.5, axis='y')
    
    # Suppression des spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig, ax


def styled_boxplot(data, labels=None, title="", xlabel="", ylabel="",
                   color=None, orientation='vertical', figsize=(10, 6)):
    """
    Boxplot pour montrer la distribution et les outliers
    
    Principes appliqués :
    - Clair et sans fioritures
    - Outliers visibles (attribut pré-attentif)
    - Comparaison facile entre groupes
    
    Args:
        data: Liste de listes (une par groupe) ou DataFrame
        labels: Labels des groupes
        title: Titre du graphique
        xlabel: Label de l'axe x
        ylabel: Label de l'axe y
        color: Couleur personnalisée
        orientation: 'vertical' ou 'horizontal'
        figsize: Taille de la figure
    
    Returns:
        fig, ax: Figure et axes matplotlib
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Couleur par défaut
    box_color = color if color else get_color('primary')
    
    # Créer le boxplot
    bp = ax.boxplot(data, labels=labels, patch_artist=True,
                    vert=(orientation == 'vertical'),
                    widths=0.6,
                    boxprops=dict(facecolor=box_color, alpha=0.7, linewidth=0),
                    whiskerprops=dict(color=get_color('neutral'), linewidth=1.5),
                    capprops=dict(color=get_color('neutral'), linewidth=1.5),
                    medianprops=dict(color='white', linewidth=2),
                    flierprops=dict(marker='o', markerfacecolor=get_color('alert'),
                                   markersize=6, alpha=0.7, markeredgecolor='none'))
    
    # Titres et labels
    if title:
        ax.set_title(title, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, fontweight='500')
    if ylabel:
        ax.set_ylabel(ylabel, fontweight='500')
    
    # Grille subtile
    if orientation == 'vertical':
        ax.grid(True, alpha=0.3, linewidth=0.5, axis='y')
    else:
        ax.grid(True, alpha=0.3, linewidth=0.5, axis='x')
    
    # Suppression des spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig, ax