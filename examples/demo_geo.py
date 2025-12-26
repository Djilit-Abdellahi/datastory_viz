import geopandas as gpd
import datastory_viz as dsv
from bokeh.plotting import show, output_file

print("=== Test de Storytelling Spatial : Mauritanie ===")

# 1. Chargement des données 
# On charge le fichier ADM2 (niveau départemental/moughataa)
# GeoPandas lira automatiquement le .dbf et le .prj associés
shapefile_path = "mrt_admbnda_adm2_ansade_20240327.shp"
gdf = gpd.read_file(shapefile_path)

# 2. Simulation de données électorales (Le Récit)
# En attendant les vrais chiffres, on crée une colonne fictive de participation
import numpy as np
gdf['Participation'] = np.random.uniform(40, 95, size=len(gdf))

# 3. Création de la carte avec votre bibliothèque
# On utilise Bokeh pour l'interactivité (Survol/Zoom) demandée
print("Construction du récit interactif...")
p = dsv.styled_choropleth(
    gdf=gdf,
    value_col="Participation",
    name_col="ADM2_FR", # Nom de la moughataa dans votre fichier .dbf
    title="Analyse Spatiale : Participation Électorale en Mauritanie"
)

# 4. Exportation
output_file("election_mauritanie_bokeh.html")
print("\n✅ Succès ! La carte interactive est prête dans 'election_mauritanie_bokeh.html'.")
show(p)
