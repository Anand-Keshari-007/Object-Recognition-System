#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import keras
import numpy as np
from keras.applications import imagenet_utils
from django.conf import settings


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# create a function to prepare image
def prepare_image(file):
    file = settings.BASE_DIR.__str__() + file
    mobile = keras.applications.mobilenet.MobileNet()
    img_path = ''
    img = keras.preprocessing.image.load_img(img_path + file, target_size=(224, 224))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    image = keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)
    predictions = mobile.predict(image)
    return imagenet_utils.decode_predictions(predictions)


if __name__ == '__main__':
    main()
