import gspread

gc = gspread.service_account('service_account_credentials.json')

spreadsheet = gc.open_by_key('1bqccoz6XTmQGKMfwvHggPzmnyT9Hi2Emwjx2yFqDLKs')

products = ['UltraZoom Camera', 'HydroClean Vacuum', 'TasteBud Blender', 'VeloSwift Bicycle', 'SonicBeat Headphones', 'MobiMax Smartphone', 'LumaBright Lamp', 'HomeEase Air Conditioner', 'MegaFit Treadmill', 'AquaPure Water Filter']

for product in products:
    spreadsheet.add_worksheet(title=product, rows=100, cols=100)