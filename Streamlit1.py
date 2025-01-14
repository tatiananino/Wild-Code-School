import streamlit as st
from datetime import date, time
import pandas as pd
import seaborn as sns # type: ignore


st.title("Bienvenue sur le site web de Tatiana NINO")
df_taxis = sns.load_dataset('taxis')

# Crear una lista de arrondissements posibles
arrondissements = df_taxis['pickup_zone'].unique()


# Agregar un selector para que el usuario elija un arrondissement
selected_arrondissement = st.selectbox(
    "Choisissez un arrondissement de récupération",
    arrondissements
)
# Filtrar el dataset en función de la selección del usuario
filtered_data = df_taxis[df_taxis['pickup_zone'] == selected_arrondissement]

# Mostrar información sobre el arrondissement seleccionado
st.write(f"Tu as Choisis: {selected_arrondissement}")

arrondissement_images = {
    "Lenox Hill West": "https://www.forbesglobalproperties.com/wp-content/uploads/2023/08/20232F082F172F202F402F112F8b6ca9d6-4e32-4885-81c7-3b519001d1de2F20230817T203329_WM_JON_8581-430382-1692305772-scaled.jpg",
    "Upper West Side South": "https://ewnqp79wvj7.exactdn.com/wp-content/uploads/2019/10/Upper-West-Side-rue-et-maisons.jpg?strip=all&lossy=1&w=2560&ssl=1",
    "Alphabet City": "https://newyorkcrazygirl.wordpress.com/wp-content/uploads/2017/11/street-art-alphabet-city-manhattan-3.jpg",
    "Hudson Sq": "https://upload.wikimedia.org/wikipedia/commons/0/0d/15-23_Charlton_Street_from_east.jpg",
    "Midtown East": "https://media.umbraco.io/corcoran-heartcore/3gxhremd/midtowneast_neighborhood.jpg",
    "Times Sq/Theatre District": "https://findhotels.nyc/wp-content/uploads/2017/06/Times_Square_1-2-1200x803.jpg",
    "Battery Park City" : "https://upload.wikimedia.org/wikipedia/commons/d/d4/Battery_Park_City.jpg",
    "Murray Hill" : "https://a.travel-assets.com/findyours-php/viewfinder/images/res70/472000/472360-Murray-Hill.jpg",
    "East Harlem South" : "https://www.newyorklatinculture.com/wp-content/uploads/2022/11/East-Harlem-El-Barrio-1645-Lexington-copyright-Zhukovsky-Dreamstime-1200x628-1.jpg",
    "Lincoln Square East" : "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Lincoln_Center_Twilight.jpg/1200px-Lincoln_Center_Twilight.jpg"
    # Agregar más entradas con las URLs de las imágenes correspondientes

}

# Mostrar la imagen asociada al arrondissement seleccionado
# Verificar si la URL existe en el diccionario
image_url = arrondissement_images.get(selected_arrondissement)

if image_url:
    st.image(image_url, caption=f"Image de {selected_arrondissement}",  use_container_width=True)
else:
    st.warning(f"Aucune image trouvée pour {selected_arrondissement}.")
