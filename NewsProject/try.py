import Scrapers
import pandas as pd

new_data = pd.DataFrame(Scrapers.TOI('Gandhi'))
new_data.to_csv("GandhiTOI.csv",index = True)
new_data = pd.DataFrame(Scrapers.TheHindu('Gandhi'))
new_data.to_csv("GandhiTheHindu.csv",index = True)
new_data = pd.DataFrame(Scrapers.IndiaTV('Gandhi'))
new_data.to_csv("GandhiIndiaTV.csv",index = True)