#Best Track times F123 Graph

import matplotlib.pyplot as plt
import pandas as pd

best_times_per_track = pd.read_csv('F1_23_Lap_times.csv')

plt.plot(best_times_per_track['Track'],
         best_times_per_track['Lap_in_seconds']) #TypeError: 'Value' must be an instance of str or bytes, not a float.

plt.xlabel('Tracks')
plt.ylabel('Fastest Time in seconds')

plt.show()
