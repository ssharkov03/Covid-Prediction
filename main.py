import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go  # Offline mode

df = pd.read_csv('C:/Users/Владислав/PycharmProjects/tg_bot/covid_data_train.csv',sep=";")
df = df.drop('Unnamed: 0', axis=1)


def to_int_size(value):
    try:
        return np.log(int(value))
    except:
        return 1


region = df.district
list(df.district.unique())
capital = df[df['name'] == 'Лангепас']


def graph_map(df):
    fig = go.Figure(data=[go.Scattermapbox(lat=df['lat'], lon=df['lng'], text=df['name'], name='map'),
                          go.Scattermapbox(lat=df['lat'], lon=df['lng'], text=df['name'],
                                           marker=dict(colorbar=dict(title="inf_rate"),
                                                       color=df['inf_rate'],
                                                       size=df['population'].map(to_int_size)), name='inf_rate'),

                          go.Scattermapbox(lat=df['lat'], lon=df['lng'], text=df['name'],
                                           marker=dict(colorbar=dict(title="ivl_per_100k"),
                                                       color=df['ivl_per_100k'],
                                                       size=df['population'].map(to_int_size)), name='ivl_per_100k')])
    map_center = go.layout.mapbox.Center(lat=float(capital['lat']), lon=float(capital['lng']))
    fig.update_coloraxes(showscale=False)
    fig.update(layout_showlegend=False)
    fig.update_layout(mapbox_style="open-street-map", mapbox=dict(center=map_center, zoom=2))
    fig.update_layout(width=1200,
                      height=700,
                      updatemenus=[
                          dict(
                              type="buttons",
                              direction="up",
                              buttons=list([
                                  dict(label="map",
                                       method="restyle",
                                       args=[{"visible": [True, False, False]},
                                             ]),

                                  dict(label="inf_rate",
                                       method="restyle",
                                       args=[{"visible": [False, True, False]},
                                             ]),

                                  dict(label="ivl_per_100k",
                                       method="restyle",
                                       args=[{"visible": [False, False, True]}]
                                       )
                              ]),
                              showactive=True,
                          ),
                          ]

                      )

    fig.write_html("C:/Users/Владислав/PycharmProjects/tg_bot/region.html")
def check_flag(flag,name):
    if flag == 1:
        df1 = df.copy()
        df1['name'] = df1['name'][region == region[list(region).index(name)]]
        df1['lat'] = df1['lat'][region == region[list(region).index(name)]]
        graph_map(df1)
    else:
        graph_map(df)