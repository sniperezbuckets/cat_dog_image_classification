import os
import random
import shutil

script_path = os.path.abspath(__file__)
parent_folder = os.path.dirname(script_path)

train_dir = os.path.join(parent_folder, 'train')
os.mkdir(train_dir)
val_dir = os.path.join(parent_folder, 'val')
os.mkdir(val_dir)
test_dir = os.path.join(parent_folder, 'test')
os.mkdir(test_dir)

images = os.listdir('images')

# train
os.mkdir(os.path.join(train_dir, 'cats'))
os.mkdir(os.path.join(train_dir, 'dogs'))
# val
os.mkdir(os.path.join(val_dir, 'cats'))
os.mkdir(os.path.join(val_dir, 'dogs'))
# test
os.mkdir(os.path.join(test_dir, 'cats'))
os.mkdir(os.path.join(test_dir, 'dogs'))


test_ratio = int(0.1 * len(images))
val_ratio = int(0.15 * len(images))


cats_image = [cat_image for cat_image in images if 'cat' in cat_image]
dogs_image = [dog_image for dog_image in images if dog_image not in cats_image]


def move_files(source_path, destination_path, files):
    for file in files:
        shutil.copy(f'{source_path}/{file}', destination_path)


def remove_files(files, files_to_remove):
    return [file for file in files if file not in files_to_remove]


val_dog_samples = random.sample(dogs_image, val_ratio)
val_cat_samples = random.sample(cats_image, val_ratio)

# val
move_files('images', os.path.join(val_dir, 'dogs'), val_dog_samples)
move_files('images', os.path.join(val_dir, 'cats'), val_cat_samples)

dogs_image = remove_files(dogs_image, val_dog_samples)
cats_image = remove_files(cats_image, val_cat_samples)


test_dog_samples = random.sample(dogs_image, test_ratio)
test_cat_samples = random.sample(cats_image, test_ratio)

# test
move_files('images', os.path.join(test_dir, 'dogs'), test_dog_samples)
move_files('images', os.path.join(test_dir, 'cats'), test_cat_samples)


dogs_image = remove_files(dogs_image, test_dog_samples)
cats_image = remove_files(cats_image, test_cat_samples)


# train
move_files('images', os.path.join(train_dir, 'dogs'), dogs_image)
move_files('images', os.path.join(train_dir, 'cats'), cats_image)


print('Train cats:', len(os.listdir(os.path.join(train_dir, 'cats'))))
print('Train dogs:', len(os.listdir(os.path.join(train_dir, 'dogs'))))

print('Val cats:', len(os.listdir(os.path.join(val_dir, 'cats'))))
print('Val dogs:', len(os.listdir(os.path.join(val_dir, 'dogs'))))

print('Test cats:', len(os.listdir(os.path.join(test_dir, 'cats'))))
print('Test dogs:', len(os.listdir(os.path.join(test_dir, 'dogs'))))

# print(val_dir)


# print(test_ratio, val_ratio)
# print(val_dog_samples)
