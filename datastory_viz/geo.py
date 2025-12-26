
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, HoverTool, LinearColorMapper
import pandas as pd
from .styles import get_color, COLORS

def styled_choropleth(gdf, value_col, name_col, title="Election Narrative"):
    """
    Améliore une carte choroplèthe avec Bokeh.
    """
    # 1. Nettoyage des données (Correction de l'erreur JSON Timestamp)
    # Convertit les colonnes datetime64 (comme 'date' et 'validOn') en chaînes
    for col in gdf.columns:
        if pd.api.types.is_datetime64_any_dtype(gdf[col]):
            gdf[col] = gdf[col].dt.strftime('%Y-%m-%d')

    # 2. Préparation des données spatiales (Vector Model) 
    # Conversion en Web Mercator pour l'alignement avec les tuiles de fond
    gdf_web = gdf.to_crs(epsg=3857)
    geosource = GeoJSONDataSource(geojson=gdf_web.to_json())
    
    # 3. Variable visuelle : Valeur (Intensité) 
    palette = ["#eff3ff", "#bdd7e7", "#6baed6", "#2171b5", "#084594"]
    color_mapper = LinearColorMapper(palette=palette, 
                                    low=gdf[value_col].min(), 
                                    high=gdf[value_col].max())

    # 4. Construction de la figure (Alignée sur Bokeh 3.x)
    p = figure(title=title, height=600, width=950, 
               x_axis_type="mercator", y_axis_type="mercator",
               toolbar_location="below",
               tools="pan, wheel_zoom, reset")
    
    # Ajout du fond de carte interactif
    p.add_tile("CartoDB Positron")
    
    # Minimalisme (Data-Ink Ratio)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # 5. Ajout des polygones (Moughataas) 
    p.patches('xs', 'ys', source=geosource,
              fill_color={'field': value_col, 'transform': color_mapper},
              line_color="white", line_width=0.5, fill_alpha=0.7)

    # 6. Interactivité : Hover Tool
    hover = HoverTool(tooltips=[
        ("Région", f"@{name_col}"),
        ("Valeur", f"@{value_col}{{0.0}}")
    ])
    p.add_tools(hover)
    
    return p