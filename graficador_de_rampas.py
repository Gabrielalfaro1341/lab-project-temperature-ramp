import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm

def graficadorrampa(directorio):
    df = pd.read_csv(directorio, delimiter=',')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8),sharex=True)
    nombre = directorio.split('/')
    path=[n+'/' for n in nombre[:-1]]
    direccion=''
    for i in path:
        direccion+=i
    # creando grafico de temperatura
    maximo = df['SensorTempertarure(K)'].max()
    minimo = df['SensorTempertarure(K)'].min()
    print(maximo)
    indice = df.index[df['SensorTempertarure(K)'] == maximo].tolist()
    ax1.plot(df.loc[:indice[-1], 'SensorTempertarure(K)'], df.loc[:indice[-1], 'DeltaP(Deg)'])
    ax1.plot(df.loc[indice[-1] + 1:, 'SensorTempertarure(K)'], df.loc[indice[-1] + 1:, 'DeltaP(Deg)'], color='red')
    ax1.set_ylabel('Delta P°', fontsize=13)
    ax1.set_title('Rampa de Temperatura ' + nombre[-1].replace('.txt', ''), fontsize=13)
    ax1.xaxis.grid(linestyle='--')
    # creando grafico de straylight
    ax2.plot(df.loc[:indice[-1], 'SensorTempertarure(K)'], df.loc[:indice[-1], 'StraylightVoltage(V)']*1000, alpha=.3)
    ax2.plot(df.loc[indice[-1] + 1:, 'SensorTempertarure(K)'], df.loc[indice[-1] + 1:, 'StraylightVoltage(V)']*1000,
             color='red', alpha=.3)

    ax2.set_ylabel('StraylightVoltage(mV)', fontsize=13)
    ax2.set_xlabel('Temperatura (K)', fontsize=13)
    ax2.set_xticks(range(300, int(maximo)+5, 10))
    ax2.set_ylim((df['StraylightVoltage(V)'].min())*1000, (df['StraylightVoltage(V)'].max())*1000)
    ax2.xaxis.grid()
    # suavizado straylight
    lowes1 = sm.nonparametric.lowess(df.loc[:indice[-1], 'StraylightVoltage(V)']*1000,
                                     df.loc[:indice[-1], 'SensorTempertarure(K)'], frac=0.1)
    lowes2 = sm.nonparametric.lowess(df.loc[indice[-1] + 1:, 'StraylightVoltage(V)']*1000,
                                     df.loc[indice[-1] + 1:, 'SensorTempertarure(K)'], frac=0.1)
    ax2.plot(lowes1[:, 0], lowes1[:, 1], color='blue')
    ax2.plot(lowes2[:, 0], lowes2[:, 1], color='red')
    fig.subplots_adjust(hspace=0)


    plt.savefig(direccion+nombre[-1].replace('.txt', '.png'), dpi=300)
    plt.show()
    return fig