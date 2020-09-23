import pandas as pd
import numpy as np


def city_finder(city_name):
    df=pd.read_html('https://worldpopulationreview.com/world-cities')
    df=df[0]
    statistics= df.iloc[np.where(df['Name']==city_name)]
    name=statistics['Name']
    population= statistics['2020 Population']
    Response= str('population of '+ name +' is: '+ str(population))

    print(type(Response))
    return {'fulfillmentText': Response}




city_finder('Delhi')