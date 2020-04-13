import pandas as pd


class CSVactions:

    @staticmethod
    def clear_a_csv(file_dis):
        f = open(file_dis, "w")
        f.truncate()
        f.close()

    @staticmethod
    def read_a_csv(file_dis, column_names):
        df = pd.read_csv(file_dis, names=column_names)
        return df

    @staticmethod
    def write_to_csv(file_path, data_frame):
        with open(file_path, 'a', newline='') as csv_file:
            data_frame.to_csv(csv_file, header=False, index=False)
