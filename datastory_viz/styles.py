"""
Configuration du style visuel basée sur les principes du data storytelling
Principes appliqués :
- Data-Ink Ratio maximal
- Attributs pré-attentifs (couleur, taille, position)
- Gestalt (proximité, similarité, clôture)
- Pas de chart junk
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Palette de couleurs professionnelle et accessible
# Utilise des couleurs distinctes (principe de similarité Gestalt)
COLORS = {
    'primary': '#2E86AB',      # Bleu professionnel
    'secondary': '#A23B72',    # Violet pour contraste
    'accent': '#F18F01',       # Orange pour highlight
    'success': '#06A77D',      # Vert
    'alert': '#D00000',        # Rouge pour alertes
    'neutral': '#6C757D',      # Gris
    'background': '#FFFFFF',   # Blanc
    'text': '#212529',         # Noir doux
}

# Palette catégorielle (pour multiple catégories)
CATEGORICAL_PALETTE = [
    '#2E86AB', '#A23B72', '#F18F01', 
    '#06A77D', '#C73E1D', '#6C757D'
]

# Palette séquentielle (pour données continues)
SEQUENTIAL_PALETTE = sns.color_palette("Blues", n_colors=8)

# Palette divergente (pour données avec point neutre)
DIVERGING_PALETTE = sns.diverging_palette(240, 10, n=11, as_cmap=False)


def apply_style():
    """
    Applique le style global à tous les graphiques
    Basé sur les principes du cours : data-ink ratio, clarté, lisibilité
    """
    # Style de base
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Configuration matplotlib
    plt.rcParams.update({
        # Police - Lisibilité avant tout
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'font.size': 11,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        
        # Couleurs - Cohérence visuelle (Gestalt : similarité)
        'axes.prop_cycle': plt.cycler(color=CATEGORICAL_PALETTE),
        'axes.facecolor': COLORS['background'],
        'figure.facecolor': COLORS['background'],
        'axes.edgecolor': COLORS['neutral'],
        'axes.labelcolor': COLORS['text'],
        'text.color': COLORS['text'],
        'xtick.color': COLORS['text'],
        'ytick.color': COLORS['text'],
        
        # Grilles - Légères (data-ink ratio)
        'grid.color': '#E0E0E0',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.3,
        'axes.grid': True,
        'axes.grid.axis': 'y',  # Seulement grille horizontale par défaut
        
        # Lignes et marqueurs
        'lines.linewidth': 2,
        'lines.markersize': 6,
        'patch.linewidth': 0,
        
        # Spines (bordures) - Minimalisme (clôture Gestalt)
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True,
        'axes.linewidth': 1,
        
        # Figure
        'figure.figsize': (10, 6),
        'figure.dpi': 100,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
        
        # Légende - Espace blanc et clarté
        'legend.frameon': False,
        'legend.loc': 'best',
    })


def get_color(name):
    """Récupère une couleur de la palette"""
    return COLORS.get(name, COLORS['primary'])


def get_categorical_colors(n=None):
    """Récupère n couleurs catégorielles"""
    if n is None:
        return CATEGORICAL_PALETTE
    return CATEGORICAL_PALETTE[:n]