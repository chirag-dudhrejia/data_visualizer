import pandas as pd


class Process_data:

    def __init__(self, data):
        self.data = pd.read_csv(data)

    def get_df(self):
        return self.data

    def get_columns(self):
        return self.data.columns.to_list()

    def get_bar_data(self):
        return self.data