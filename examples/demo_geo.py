import os
import sys
import numpy as np
import geopandas as gpd
from bokeh.io import output_file, save
import pyogrio

# Configuration pour restaurer l'indexation si les fichiers .shx sont mal lus
pyogrio.set_gdal_config_options({"SHAPE_RESTORE_SHX": "YES"})

# Ajout du chemin pour accéder à datastory_viz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datastory_viz.geo import styled_choropleth

def run_geo_demo():
    # Chemin vers votre dossier mrshape
    shapefile_path = "mrshape/mrt_admbnda_adm2_ansade_20240327.shp"
    
    if not os.path.exists(shapefile_path):
        print(f"Erreur : Shapefile introuvable à {shapefile_path}")
        return

    print("Step 1: Chargement du Shapefile Mauritanie ADM2...")
    gdf = gpd.read_file(shapefile_path)

    # Utilisation des colonnes identifiées dans le notebook
    name_col = 'ADM2_EN' # Nom de la Moughataa
    value_col = 'demo_results'
    gdf[value_col] = np.random.uniform(10, 100, size=len(gdf))

    # Configuration de la sortie
    output_path = "demo_output.html"
    output_file(output_path, title="Mauritania Demo")

    print("Step 2: Création de la carte interactive (Nettoyage JSON inclus)...")
    plot = styled_choropleth(gdf, value_col, name_col, "Carte Administrative Mauritanie")

    print(f"Step 3: Sauvegarde du fichier : {output_path}")
    save(plot)
    print("\nSUCCÈS ! Ouvrez le fichier 'demo_output.html' manuellement dans votre navigateur.")

if __name__ == "__main__":
    run_geo_demo()