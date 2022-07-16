import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go  # Offline mode

df = pd.read_csv('C:/Users/Владислав/PycharmProjects/tg_bot/covid_data_train.csv',sep=";")
df1 = pd.read_csv('C:/Users/Владислав/PycharmProjects/tg_bot/covid_data_test.csv')
pred = pd.read_csv('C:/Users/Владислав/PycharmProjects/tg_bot/NSU-ES-Team.csv')
df1 = df1.drop('Unnamed: 0', axis=1)
df1['inf_rate'] = pred
df = df.drop('Unnamed: 0', axis=1)
df = pd.concat([df,df1],axis=0)

def to_int_size(value):
    try:
        return np.log(int(value))
    except:
        return 1


region = df.district
list(df.district.unique())
capital = df[df['name'] == 'Лангепас']


def graph_map(df):
    fig = go.Figure(data=[go.Scattermapbox(lat=df['lat'], lon=df['lng'], text=df['name'], name='общая карта'),
                          go.Scattermapbox(lat=df['lat'], lon=df['lng'], text=df['name'],
                                           marker=dict(colorbar=dict(title="частота заражения"),
                                                       color=df['inf_rate'],
                                                       size=df['whole_population'].map(to_int_size)), name='частота заражения'),

                          go.Scattermapbox(lat=df['lat'], lon=df['lng'], text=df['name'],
                                           marker=dict(colorbar=dict(title="ИВЛ на 100 тыс."),
                                                       color=df['ivl_per_100k'],
                                                       size=df['whole_population'].map(to_int_size)), name='ИВЛ на 100 тыс.'),
                          go.Scattermapbox(lat=df['lat'], lon=df['lng'], text=df['name'],
                                           marker=dict(colorbar=dict(title="ЭКМО на 100 тыс."),
                                                       color=df['ekmo_per_100k'],
                                                       size=df['whole_population'].map(to_int_size)), name='ЭКМО на 100 тыс.')

                          ])
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
                                  dict(label="общая карта",
                                       method="restyle",
                                       args=[{"visible": [True, False, False,False]},
                                             ]),

                                  dict(label="частота заражения",
                                       method="restyle",
                                       args=[{"visible": [False, True, False,False]},
                                             ]),

                                  dict(label="ИВЛ на 100 тыс.",
                                       method="restyle",
                                       args=[{"visible": [False, False, True,False]}]
                                       ),
                                  dict(label="ЭКМО на 100 тыс.",
                                       method="restyle",
                                       args=[{"visible": [False, False,False, True]}]
                                       ),



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