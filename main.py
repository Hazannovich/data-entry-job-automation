from data_to_sheet import DataToSheet
from zillow_data import ZillowData

data = ZillowData()
form = DataToSheet()
print(len(data.get_links()),len(data.get_prices()), len(data.get_addresses()))
form.fill_forms(data.get_addresses(),data.get_prices(), data.get_links())
