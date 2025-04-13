import pandas as pd
import json
from app.repositories.planet_habitability_repository import PlanetHabitabilityRepository

class PlanetHabitabilityService:
    """
    Lógica de negocio y transformación de datos para la habitabilidad planetaria.
    """

    @staticmethod
    def classify_ihp(ihp):
        if ihp < 0.2:
            return "Planeta hostil, inhabitable"
        elif ihp < 0.4:
            return "Habitabilidad muy baja, requiere tecnología avanzada"
        elif ihp < 0.6:
            return "Potencialmente habitable con infraestructura significativa"
        elif ihp < 0.8:
            return "Habitable con modificaciones menores"
        else:
            return "Altamente habitable, similar a la Tierra"
        
    @staticmethod
    def get_habitability_by_planet(planet_id):

        habitability_data = PlanetHabitabilityRepository.get_by_id(planet_id)

        if not habitability_data:
            return {"error": "Planet not found"}, 404

        df = pd.DataFrame(data.__dict__ for data in habitability_data)
        df = df.drop(columns=['_sa_instance_state']) ##?

        avg_ihp = df['ihp'].mean()
        df["ihp"] = avg_ihp
        df["classification"] = df["ihp"].apply(PlanetHabitabilityService.classify_ihp)
        df = df.drop(columns=['id_mission', 'scanning_date', 'distance'])
        # classification = PlanetHabitabilityService.classify_ihp(avg_ihp)

        return df.iloc[0].to_dict(), 200
    
        # return {
        #     "id_planet": planet_id,
        #     "planet_name": df["name"].iloc[0],
        #     "ihp": round(avg_ihp, 3),
        #     "classification": classification
        # }, 200
        # to_json(orient='records')


        # ihp = habitability_data[0].ihp if habitability_data else None
        # classification = PlanetHabitabilityService.classify_ihp(ihp) if ihp is not None else None

        # return {
        #     "id_planet": planet_id,
        #     "ihp": ihp,
        #     "classification": classification
        # }, 200

    @staticmethod
    def get_planet_ranking():
        habitability_data = PlanetHabitabilityRepository.get_all()
        if not habitability_data:
            return {"error": "No data available"}, 404
        
        df = pd.DataFrame(data.__dict__ for data in habitability_data)
        df = df.drop(columns=['_sa_instance_state'])
        # print('df: ', df)

        grouped = df.groupby(['id_planet', 'name'], as_index=False).agg({'ihp': 'mean'})
        # print('grouped: ', grouped)
        grouped['classification'] = grouped['ihp'].apply(PlanetHabitabilityService.classify_ihp)
        # print('grouped with classification: ', grouped)
        grouped = grouped.sort_values(by='ihp', ascending=False)
        # print('grouped sorted: ', grouped)

        if grouped.empty:
            return {"error": "No data available"}, 404

        return grouped.to_dict(orient='records'), 200
    
    
    @staticmethod
    def get_planet_tendences():
        habitability_data = PlanetHabitabilityRepository.get_all()
        if not habitability_data:
            return {"error": "No data available"}, 404
        
        # Convertir los datos de los escaneos a un DataFrame
        df = pd.DataFrame(data.__dict__ for data in habitability_data)
        df = df.drop(columns=['_sa_instance_state'])

        # Agrupar por id_planet, name y scanning_date para obtener el promedio de ihp (aunque aquí es innecesario, ya que hay solo un escaneo por planeta)
        grouped = df.groupby(['id_planet', 'name', 'scanning_date'], as_index=False).agg({'ihp': 'mean'})
        grouped['classification'] = grouped['ihp'].apply(PlanetHabitabilityService.classify_ihp)

        # Ordenar por id_planet y scanning_date
        grouped = grouped.sort_values(by=['id_planet', 'scanning_date'])
        print('grouped sorted: ', grouped)

        planet_tendencies = []

        # Agrupar los escaneos por planeta (id_planet) para crear la tendencia
        for id, data in grouped.groupby('id_planet'):
            data = data.reset_index(drop=True)  # Reiniciar el índice para cada grupo
            print('id: ', id, 'data: ', data)
            planet_name = data['name'].iloc[0]  # Tomar el nombre del planeta
            tendencies = []

            # Aquí, se analiza la tendencia entre los escaneos
            for i, row in data.iterrows():
                print("----------------")
                print('i: ', i, 'row: ', row)
                trend = "Initial"

                # Compara el escaneo actual con el anterior para determinar la tendencia
                if i > 0:
                    prev_ihp = data['ihp'].iloc[i - 1]
                    current_ihp = row['ihp']

                    if current_ihp > prev_ihp:
                        trend = "Increasing"
                    elif current_ihp < prev_ihp:
                        trend = "Decreasing"
                    else:
                        trend = "Equal"

                tendencies.append({
                    "date": row['scanning_date'].strftime("%Y-%m-%d"),
                    "classification": row['classification'],
                    "ihp": row['ihp'],
                    "trend": trend,
                })

            # Agregar las tendencias por planeta
            planet_tendencies.append({
                "id_planet": id,
                "name": planet_name,
                "tendencies": tendencies
            })

        return planet_tendencies, 200
    

    @staticmethod
    def get_tendencies_by_planet_id(planet_id):
        data = PlanetHabitabilityRepository.get_by_planet_id(planet_id)
        if not data:
            return None

        df = pd.DataFrame([d.__dict__ for d in data])
        df = df.drop(columns=['_sa_instance_state'])

        df = df.sort_values(by='scanning_date')
        df['classification'] = df['ihp'].apply(PlanetHabitabilityService.classify_ihp)

        tendencies = df[['scanning_date', 'ihp', 'classification']].to_dict(orient='records')

        return {
            "planet": df["name"].iloc[0],
            "tendencies": tendencies
        }
        


    # @staticmethod
    # def list_planet_habitability():
    #     """
    #     Listar todos los planetas con su índice de habitabilidad.
    #     """
    #     habitability_data = PlanetHabitabilityRepository.get_all()
    #     return habitability_data  # Retorna los datos sin serializar para mayor flexibilidad

    # @staticmethod
    # def get_planet_habitability_by_id(planet_id):
    #     """
    #     Obtener la información de habitabilidad de un planeta por su ID.
    #     """

    #     habitability_data = PlanetHabitabilityRepository.get_by_id(planet_id)

    #     if not habitability_data:
    #         return {"error": "Planet not found"}, 404

    #     return habitability_data, 200
