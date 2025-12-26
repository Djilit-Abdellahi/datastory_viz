import os
import sys
import numpy as np
import geopandas as gpd
from bokeh.io import output_file, show

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datastory_viz.geo import styled_choropleth

def run_geo_demo():
    # File path for the specific shapefile
    shapefile_path = "mrt_admbnda_adm2_ansade_20240327.shp"
    
    if not os.path.exists(shapefile_path):
        print(f"Error: {shapefile_path} not found.")
        return

    # Load data using geopandas
    gdf = gpd.read_file(shapefile_path)

    # Generate dummy values for visualization demo
    # Standard column for region names in this specific file is often 'ADM2_FR'
    name_col = 'ADM2_FR' 
    value_col = 'result_value'
    
    gdf[value_col] = np.random.uniform(0, 100, size=len(gdf))

    # Configure Bokeh output
    output_path = "demo_output.html"
    output_file(output_path, title="Interactive Geo Demo")

    # Call the library function
    plot = styled_choropleth(
        gdf=gdf,
        value_col=value_col,
        name_col=name_col,
        title="Interactive Mauritania Administrative Map"
    )

    # Display result
    print(f"Opening {output_path}...")
    show(plot)

if __name__ == "__main__":
    run_geo_demo()
