"""
datastory_viz - Bibliothèque de visualisation pour le data storytelling
Applique automatiquement les best practices du cours DEML 2025/2026
"""

__version__ = "1.0.0"
__author__ = "Votre Nom"

# Import des fonctions principales
from .core import (
    styled_line,
    styled_bar,
    styled_scatter,
    styled_heatmap,
    styled_histogram,
    styled_boxplot,
)

# Import du style
from .styles import apply_style, get_color, get_categorical_colors

# Appliquer le style par défaut
apply_style()

# Définir ce qui est exporté avec "from datastory_viz import *"
__all__ = [
    'styled_line',
    'styled_bar',
    'styled_scatter',
    'styled_heatmap',
    'styled_histogram',
    'styled_boxplot',
    'apply_style',
    'get_color',
    'get_categorical_colors',
]