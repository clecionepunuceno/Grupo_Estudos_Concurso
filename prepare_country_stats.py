import pandas as pd

def prepare_country_stats(oecd_bli, gdp_per_capita):
    # 1. Filtra para pegar apenas o indicador de 'Satisfação de Vida'
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    
    # 2. Renomeia e organiza as colunas do PIB
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    
    # 3. Une (merge) os dois DataFrames baseando-se no índice (País)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    
    # 4. Ordena pelo PIB e remove alguns países (outliers) para o exemplo ficar didático
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35] # Países muito pobres ou muito ricos
    keep_indices = list(set(range(36)) - set(remove_indices))
    
    return full_country_stats.iloc[keep_indices][["GDP per capita", 'Life satisfaction']]