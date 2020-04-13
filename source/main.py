
import tensorflow as tf
import sklearn
import numpy as np


# create the model
# cm.CreateModel().main()

# saved_model = tf.keras.models.load_model('saved_model')
# print(saved_model.summary())

# rec_data_frame = cm.CreateModel().process_data("../dataset/tic-tac-toe.csv")

# remove results column from the data frame and convert it to a data frame
# target = rec_data_frame.pop('target')
# results = target.to_frame()

# get the remaining data as feeds to the model
# feeds = rec_data_frame
#
# train_df, test_df, train_target_df, test_target_df = sklearn.model_selection.train_test_split(feeds, results,
#                                                                                               test_size=0)

# cm.CreateModel().evaluate_the_model(saved_model, test_df, test_target_df)

# class_names = ["FALSE", "TRUE"]
#
# tempered_test = [[2, 2, 2, 2, 1, 1, 1, 2, 1], [2, 2, 2, 2, 1, 1, 2, 1, 1], [1, 0, 1, 2, 2, 1, 2, 2, 1], [0, 2, 0, 2, 0, 2, 1, 1, 1],
#                  [0, 1, 0, 2, 2, 2, 0, 0, 1]]
#
# # received a numpy array
# predictions = saved_model.predict(tempered_test)
#
# print(predictions)

# print(len(predictions))

# for n in range(len(predictions)):
#     print("predicted : ", class_names[np.argmax(predictions[n])])
#
# for n in range(10):
#     print("\nprediction : ", class_names[np.argmax(single_prediction[n])], " real : ", class_names[test_target_df[n]])

# dataprocessor.DataProcessor.update_the_main_csv()

