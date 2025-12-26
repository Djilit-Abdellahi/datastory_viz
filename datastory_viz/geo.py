"""
Fonctions de cartographie appliquant les principes du GIS storytelling
"""
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, HoverTool, LinearColorMapper
from .styles import get_color, COLORS

def styled_choropleth(gdf, value_col, name_col, title="Election Narrative"):
    """
    Améliore une carte choroplèthe avec Bokeh.
    
    Principes appliqués :
    - CRS : Conversion en Web Mercator (EPSG:3857)
    - Storytelling : Utilise la 'Valeur' pour les données quantitatives 
    - Interaction : Info-bulles pour donner de la 'voix' aux données [cite: 4, 791]
    """
    # 1. Préparation des données spatiales (Vector Model) 
    # Conversion obligatoire pour l'affichage Web 
    gdf_web = gdf.to_crs(epsg=3857)
    geosource = GeoJSONDataSource(geojson=gdf_web.to_json())
    
    # 2. Variable visuelle : Valeur (Intensité) 
    # On évite la Teinte (Hue) pour les données ordonnées 
    palette = ["#eff3ff", "#bdd7e7", "#6baed6", "#2171b5", "#084594"]
    color_mapper = LinearColorMapper(palette=palette, 
                                    low=gdf[value_col].min(), 
                                    high=gdf[value_col].max())

    # 3. Construction de la figure (L'empilement des couches)
    p = figure(title=title, height=600, width=950, 
               toolbar_location="below",
               tools="pan, wheel_zoom, reset")
    
    # Minimalisme (Data-Ink Ratio)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # Ajout de la couche thématique (Polygones) 
    p.patches('xs', 'ys', source=geosource,
              fill_color={'field': value_col, 'transform': color_mapper},
              line_color="white", line_width=0.5, fill_alpha=0.8)

    # 4. Interactivité : Hover Tool (Le survol)
    # Extrait le 'Quoi' et le 'Où' de la table attributaire 
    hover = HoverTool(tooltips=[
        ("Région", f"@{name_col}"),
        ("Résultat", f"@{value_col}")
    ])
    p.add_tools(hover)
    
    return p
