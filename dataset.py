import os
import numpy as np
from PIL import Image

import matplotlib.pyplot as plt

import torch
import torchvision


class ImageDataset(torch.utils.data.Dataset):
    def __init__(self, dir, transform=None):
        self.data_dir = dir
        self.images = os.listdir(dir)
        self.transform = transform

    # Defining the length of the dataset
    def __len__(self):
        return len(self.images)

    # Defining the method to get an item from the dataset
    def __getitem__(self, index):
        image_path = os.path.join(self.data_dir, self.images[index])
        image = np.array(Image.open(image_path))

        # Applying the transform
        if self.transform:
            image = self.transform(image)
        
        return image

    # Replace the path with the path to your dataset
data_path1 = './rover/switch'
data_path2 = './rover/knob'
data_path3 = './rover/socket'

# Creating a dataset object with the path to the dataset
dataset1 = ImageDataset(data_path1)
dataset2 =ImageDataset(data_path2)
dataset3 =ImageDataset(data_path3)

# Generating a random index within the dataset length
random_index = random.randint(0, dataset_length - 1)


def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE,DESTINATION):
    files = []
    for filename in os.listdir(SOURCE):
        file = SOURCE + filename
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + " has not enough pixels to represent it as an image, seems corrupted so ignoring.")

    training_length = int(len(files) * SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[-testing_length:]

    for filename in training_set:
        this_file = SOURCE + filename
        destination = TRAINING + filename
        copyfile(this_file, destination)

    for filename in testing_set:
        this_file = SOURCE + filename
        destination = TESTING + filename
        copyfile(this_file, destination)
# Plotting the randomly selected image
plt.imshow(dataset[random_index])
plt.show()