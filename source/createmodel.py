import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model, preprocessing
import dataset

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class CreateModel:

    def __init__(self):
        print("create model started.")

    def main(self):
        # data_frame = self.process_data("../dataset/tic-tac-toe.csv")
        data_frame = self.process_data("../dataset/test_data.csv")
        model = self.__create_the_model()
        self.__train_and_save(model, data_frame)

    def __train_and_save(self, model, data_frame):
        # remove results column from the data frame and convert it to a data frame
        target = data_frame.pop('target')
        results = target.to_frame()

        # get the remaining data as feeds to the model
        feeds = data_frame

        for n in range(5):
            # train_df, test_df, train_target_df, test_target_df = sklearn.model_selection.train_test_split(feeds,
            #                                                                                               results,
            #                                                                                               test_size=0.1)
            # model.fit(train_df, train_target_df, epochs=20)
            model.fit(feeds, target, epochs=20)

        model.save('saved_model/')
        print("new model saved")

    def __create_the_model(self):
        # creating the model
        model = keras.Sequential([
            keras.layers.Dense(9, activation='relu', input_shape=[9]),
            keras.layers.Dense(18, activation='relu'),
            keras.layers.Dense(2, activation='softmax')
        ])

        # compiling the model
        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        return model

    def process_data(self, file_path):
        # read the data file
        data_frame = pd.read_csv(file_path)

        data_frame['TL'] = pd.Categorical(data_frame['TL'])
        data_frame['TL'] = data_frame.TL.cat.codes
        data_frame['TM'] = pd.Categorical(data_frame['TM'])
        data_frame['TM'] = data_frame.TM.cat.codes
        data_frame['TR'] = pd.Categorical(data_frame['TR'])
        data_frame['TR'] = data_frame.TR.cat.codes

        data_frame['ML'] = pd.Categorical(data_frame['ML'])
        data_frame['ML'] = data_frame.ML.cat.codes
        data_frame['MM'] = pd.Categorical(data_frame['MM'])
        data_frame['MM'] = data_frame.MM.cat.codes
        data_frame['MR'] = pd.Categorical(data_frame['MR'])
        data_frame['MR'] = data_frame.MR.cat.codes

        data_frame['BL'] = pd.Categorical(data_frame['BL'])
        data_frame['BL'] = data_frame.BL.cat.codes
        data_frame['BM'] = pd.Categorical(data_frame['BM'])
        data_frame['BM'] = data_frame.BM.cat.codes
        data_frame['BR'] = pd.Categorical(data_frame['BR'])
        data_frame['BR'] = data_frame.BR.cat.codes

        data_frame['target'] = pd.Categorical(data_frame['target'])
        data_frame['target'] = data_frame.target.cat.codes

        return data_frame

    def evaluate_the_model(self, model, test_data, test_results):
        test_loss, test_acc = model.evaluate(test_data, test_results, verbose=2)
        print('\nTest accuracy:', test_acc)

