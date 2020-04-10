import pandas as pd


class CollectData:

    def __init__(self, moves_list):
        self.moves_list = moves_list
        self.save_data()

    def save_data(self):
        self.format_the_data()
        self.write_to_csv()

    def format_the_data(self):
        formatted_list = []
        for move in self.moves_list:
            for index, pos in enumerate(move):
                if pos is 2:
                    move[index] = 'x'
                elif pos is 1:
                    move[index] = 'o'
                elif pos is 0:
                    move[index] = 'b'
            formatted_list.append(move)

        self.moves_list = formatted_list

    def write_to_csv(self):
        with open('../dataset/collected-data.csv', 'a', newline='') as csv_file:
            df = pd.DataFrame(self.moves_list)
            df.to_csv(csv_file, header=False, index=False)
