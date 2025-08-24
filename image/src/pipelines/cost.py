import pandas as pd

from src.aws import cost_explorer

res = cost_explorer.get_cost()
data = []
for service in res['ResultsByTime'][0]['Groups']:
    data.append({
        'SERVIÇO': service['Keys'][0],
        'VALOR': float(service['Metrics']['UnblendedCost']['Amount']),
        'MOEDA': service['Metrics']['UnblendedCost']['Unit']
    })

df_cost = pd.DataFrame(data)

df_cost = df_cost.sort_values(by='VALOR', ascending=False)

df_cost = pd.concat([
    df_cost,
    pd.DataFrame([{
        'SERVIÇO': 'TOTAL',
        'VALOR': df_cost['VALOR'].sum(),
        'MOEDA': 'USD'
    }])
])