
#Importing Modules-------------------------------------------------------------------------------------------------------------
import tensorflow.keras
import pygad.kerasga

#Defining the number of input Classes
num_inputs = 2
num_classes = 2

#Training the data-------------------------------------------------------------------------------------------------------------
input_layer  = tensorflow.keras.layers.Input(num_inputs)
dense_layer = tensorflow.keras.layers.Dense(4, activation="relu")(input_layer)
output_layer = tensorflow.keras.layers.Dense(num_classes, activation="softmax")(dense_layer)

model = tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)

num_solutions = 10
keras_ga = pygad.kerasga.KerasGA(model=model,
                                 num_solutions=num_solutions)
keras_ga.population_weights
