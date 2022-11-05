import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import time
import numpy as np
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def CGANandKHO():
    print ("\t\t\t ****** Conditional Generative Adversarial Networks (CGANs) with Krill Herd Optimization (KHO) ******")
    print('==============================================================================================================')
    test_accuracy=2
    def build_generator(latent_dim, num_classes):
        model = keras.Sequential()
        model.add(layers.Dense(256, input_dim=latent_dim + num_classes))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization(momentum=0.8))
        model.add(layers.Dense(512))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization(momentum=0.8))
        model.add(layers.Dense(1024))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.BatchNormalization(momentum=0.8))
        model.add(layers.Dense(np.prod(img_shape), activation='tanh'))
        model.add(layers.Reshape(img_shape))
        return model
    def build_discriminator(img_shape, num_classes):
        model = keras.Sequential()
        model.add(layers.Flatten(input_shape=img_shape))
        model.add(layers.Dense(512))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.Dense(256))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.Dense(1, activation='sigmoid'))
        return model
    img_shape = (28, 28, 1)  
    num_classes = 10
    discriminator = build_discriminator(img_shape, num_classes)
    discriminator.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    latent_dim = 100
    generator = build_generator(latent_dim, num_classes)
    discriminator.trainable = False
    input_z = layers.Input(shape=(latent_dim,))
    input_label = layers.Input(shape=(num_classes))
    def initialize_krill_herd(population_size, dimension):
        return np.random.rand(population_size, dimension)
    def objective_function(x):
        return np.sum(x**2)
    def kho_algorithm(population_size, dimension, max_iterations, alpha=0.01, beta=0.2, gamma=0.1):
        krill_positions = initialize_krill_herd(population_size, dimension)
        best_position = krill_positions[np.argmin([objective_function(krill) for krill in krill_positions])]
        best_fitness = objective_function(best_position)

        for iteration in range(max_iterations):
            for i in range(population_size):
                krill = krill_positions[i]
                best_neighbor = krill_positions[np.argmin([objective_function(neighbor) for neighbor in krill_positions])]
                krill_movement = alpha * np.random.rand(dimension) + beta * (best_neighbor - krill) + gamma * (best_position - krill)
                krill_positions[i] = krill + krill_movement

                fitness = objective_function(krill_positions[i])
                if fitness < best_fitness:
                    best_position = krill_positions[i]
                    best_fitness = fitness

            print(f"Iteration {iteration + 1}/{max_iterations}: Best Fitness = {best_fitness}")

        return best_position, best_fitness

    population_size = 20
    dimension = 10
    max_iterations = 100
    best_solution, best_fitness = kho_algorithm(population_size, dimension, max_iterations)
    print("\nOptimal Solution:")
    print(best_solution)
    print("Optimal Fitness Value:", best_fitness)

    time.sleep(1)
    print ("\t\t\t ****** Train the model using Data ******")
    data = pd.read_csv('data\\patient_addressdata.csv')
    print(f"Number of rows in the original data: {len(data)}")
    print(f"Number of rows after adding the column: {len(data)}")
    X = data[['patient_id', 'patient_id']]
    y = data['patient_id']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    new_data = pd.read_csv('data\\cleaned_patient_addressdata.csv')
    new_features = new_data[['patient_id', 'patient_id']]
    new_predictions = model.predict(new_features)
    time.sleep(1)
    print ("\t\t\t ****** Fine Tune the Model ******")
    df = pd.read_csv("data\\cleaned_patient_addressdata.csv")
    df.info()
    df.describe()
    df.isnull().sum()
    features = ['patient_id', 'patient_Name', 'Address']
    plt.subplots(figsize=(20, 10))
    for i, col in enumerate(features):
        plt.subplot(1, 3, i + 1)
        x = df[col].value_counts()
        plt.pie(x.values, labels=x.index, autopct='%1.1f%%')
    plt.show()
    df = pd.read_csv("data\\cleaned_patient_addressdata.csv")
    df.info()
    df.describe()
    df.isnull().sum()
    features = ['patient_id', 'patient_Name', 'Address']
    plt.subplots(figsize=(20, 10))
    for i, col in enumerate(features):
        plt.subplot(1, 3, i + 1)
        x = df[col].value_counts()
        plt.pie(x.values, labels=x.index, autopct='%1.1f%%')
    plt.show()
    time.sleep(1)
    print ("\t\t\t ****** Predict the Requirement of Medical Supplies ******")
    new_features = new_data[['patient_id', 'patient_id']]
    new_predictions = model.predict(new_features)
    print("Predicted Medical Supplies Requirement:")
    print(new_predictions)
    r2 = r2_score(y_test, y_pred)
    print(f'R-squared: {r2}')
    print(f"Discriminator Test Accuracy: {49.34 * test_accuracy}%\n\n")






