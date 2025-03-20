import glob
import pandas as pd

files = glob.glob("../files/*.csv")
save_files = '../saved_files/'

# Llegir tots els arxius i guardar-los en una llista
dfs = [pd.read_csv(fitxer) for fitxer in files]
