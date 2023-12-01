#Best Track times F123 Graph
python3 -mpip matplotlib as plt
import pandas as pd

best_times_per_track = pd.read_csv('F1_23_Lap_times.csv')

plt.plot(best_times_per_track['Track'],
         best_times_per_track['Fastest_lap'])

plt.show()