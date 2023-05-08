import plotly.express as px
import csv
import pandas as pd
player = []
team = []
posicao = []
with open('CSVFiles/players.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        temp_player = row[0]
        temp_team = row[1]
        temp_posi = row[2]

        #print(row)
        team.append(temp_team)
        player.append(temp_player)
        posicao.append(temp_posi)

print(player)
print(team)
print(posicao)

df = pd.DataFrame(dict(team=team,posicao=posicao,player=player))
fig = px.treemap(df, path=['team','posicao','player'])
#fig.upd    ate_traces(root_color="lightgrey")
#fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
