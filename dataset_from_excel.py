import pandas as pd
from dspy.datasets.dataset import Dataset


class ExcelDataset(Dataset):
    def __init__(self, file_path, *args,**kwargs) -> None:
        super().__init__(*args, **kwargs)

        df = pd.read_excel(file_path)
        self._train = df.iloc[0:10].to_dict(orient='records')
        self._val = df.iloc[10:20].to_dict(orient='records')
        self._test = df.iloc[20:].to_dict(orient='records')

excel_data = ExcelDataset("dialogue-data-small.xlsx")
train, val, test = excel_data._train, excel_data._val, excel_data._test
