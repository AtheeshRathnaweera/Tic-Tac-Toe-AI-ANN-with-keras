import pandas as pd
import csvactions


class DataProcessor:

    def __init__(self, moves_list):
        self.moves_list = moves_list
        self.save_data()

    def save_data(self):
        self.format_the_data()
        df = pd.DataFrame(self.moves_list)
        csvactions.CSVactions.write_to_csv("../dataset/collected-data.csv", df)

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

    @staticmethod
    def update_the_main_csv():
        columns = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR', 'target']

        main_df = csvactions.CSVactions.read_a_csv('../dataset/tic-tac-toe.csv', columns)
        collected_df = csvactions.CSVactions.read_a_csv('../dataset/collected-data.csv', columns)

        print("collected amount : ", len(collected_df))

        # hold the newest rows
        new_rows_list = []

        # remove duplicated from the collected values
        collected_df.drop_duplicates(keep='first', inplace=True, ignore_index=True)

        for i, col_row in collected_df.iterrows():
            new_row = True
            for main_i, main_row in main_df.iterrows():
                if main_row['TL'] == col_row['TL'] and main_row['TM'] == col_row['TM'] and main_row['TR'] == col_row['TR'] \
                        and main_row['ML'] == col_row['ML'] and main_row['MM'] == col_row['MM'] and main_row['MR'] == col_row['MR']\
                        and main_row['BL'] == col_row['BL'] and main_row['BM'] == col_row['BM'] and main_row['BR'] == col_row['BR']:
                    # print('main row : ', main_i, i)
                    # save the new row and remove the main file row
                    print("found")
                    # main_row['target'] = col_row['target']
                    # print('found updated')
                    new_row = False
                    break
                else:
                    # save the main file row as it is
                    print("not found ", col_row.values.tolist())
                    new_row = True

            if new_row:
                new_rows_list.append(col_row.values.tolist())

        new_rows_df = pd.DataFrame(new_rows_list, columns=columns)

        print("new rows df size : ", len(new_rows_df))
        print('main df size : ', len(main_df))

        main_df = main_df.append(new_rows_df, ignore_index=True)
        print('updated main_df size : ', len(main_df))

        csvactions.CSVactions.clear_a_csv("../dataset/tic-tac-toe.csv")
        csvactions.CSVactions.clear_a_csv("../dataset/collected-data.csv")

        csvactions.CSVactions.write_to_csv("../dataset/tic-tac-toe.csv", main_df)


# DataProcessor.update_the_main_csv()




