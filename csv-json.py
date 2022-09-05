import pandas as pd


class WineData:
    def __init__(self, file_path, in_json=False, save_path=''):
        self.file_data = pd.read_csv(file_path)  # Reading csv file
        self.in_json = in_json  # Check if we want to load data to json
        self.save_path = save_path  # Path to file if we want to save data to json

    def find_wine_type(self, wine_type: str):
        data = self.file_data[self.file_data['variety'].values == wine_type]  # Filter data by wine type

        if self.in_json:  # Saving data
            data.to_json(self.save_path)
            print('Loaded into json')
        return data

    def find_wine_rating(self, rating: tuple):
        data = self.file_data[self.file_data['rating'].isin(range(rating[0], rating[1] + 1))]  # Filter data by rating range

        if self.in_json:
            data.to_json(self.save_path)
            print('Loaded into json')
        return data

    def find_wine_region(self, region: str):
        data = self.file_data[self.file_data['region'].values == region]  # Filter data by region

        if self.in_json:
            data.to_json(self.save_path)
            print('Loaded into json')
        return data


# Filer and save files to json
california_wine = WineData('wine-data.csv', in_json=True, save_path='cal_wine.json').find_wine_region('California')
top_wine = WineData('wine-data.csv', in_json=True, save_path='top_wine.json').find_wine_rating((89, 92))
white_wine = WineData('wine-data.csv', in_json=True, save_path='white_wine.json').find_wine_type('Red Wine')

# Check if we did everything properly
print(pd.read_json('cal_wine.json'))
print(pd.read_json('top_wine.json'))
print(pd.read_json('white_wine.json'))
