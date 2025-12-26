from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, HoverTool, LinearColorMapper
from bokeh.palettes import RdBu
from bokeh.tile_providers import get_provider, Vendors
import json

def styled_choropleth(gdf, value_col, name_col, title="Election Narrative"):
    """
    AMELIORATED VERSION:
    - Background: Added interactive Map Tiles (CartoDB)
    - Palette: Uses RdBu (Red-Blue) for election storytelling
    - CRS: Handles EPSG:3857 for Web Mercator alignment
    """
    
    # 1. Prepare Data (Keep your GeoPandas logic - it's better than manual math!)
    gdf_web = gdf.to_crs(epsg=3857)
    geosource = GeoJSONDataSource(geojson=gdf_web.to_json())
    
    # 2. Variable visuelle : Red to Blue Palette (Professional for elections)
    # RdBu[10] gives 10 levels from Red to Blue
    palette = RdBu[10] 
    color_mapper = LinearColorMapper(palette=palette, 
                                    low=gdf[value_col].min(), 
                                    high=gdf[value_col].max())

    # 3. Construction de la figure with Mercator axis
    p = figure(title=title, height=600, width=950, 
               x_axis_type="mercator", y_axis_type="mercator",
               tools="pan, wheel_zoom, reset")
    
    # ADDED: Background Tiles (This is a major amelioration)
    tile_provider = get_provider(Vendors.CARTODB_POSITRON)
    p.add_tile(tile_provider)

    # 4. Ajout de la couche (Polygones)
    p.patches('xs', 'ys', source=geosource,
              fill_color={'field': value_col, 'transform': color_mapper},
              line_color="white", line_width=0.5, fill_alpha=0.7)

    # 5. Interactivité : Improved Hover Tool
    hover = HoverTool(tooltips=[
        ("Région", f"@{name_col}"),
        ("Résultat", f"@{value_col}{{0.0}}%"), # Added percentage formatting
    ])
    p.add_tools(hover)
    
    return p
