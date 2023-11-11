#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Bhagyasri
# DATE CREATED: 02/11/2023
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0: pet image label (string).

# Imports python modules
import os

# Define get_pet_labels function
def get_pet_labels(image_folder):
    """
    Creates a dictionary of pet labels (labels_dict) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lowercase letters
    and with leading and trailing whitespace characters stripped from them.
    Numbers are removed from the pet labels, and underscores are replaced with spaces.
    (ex. filename = 'German_shepherd_12345.jpg' Pet label = 'german shepherd'
    
    Parameters:
     image_folder - The (full) path to the folder of images that are to be
                    classified by the classifier function (string)
    
    Returns:
      labels_dict - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    labels_dict = {}
    image_files = os.listdir(image_folder)

    for image_file in image_files:
        # Exclude files starting with a "."
        if not image_file.startswith('.'):
            pet_label = image_file.split('.')[0]
            translation_table = str.maketrans('', '', '0123456789')
            pet_label = pet_label.translate(translation_table)
            pet_label = pet_label.replace('_', ' ')
            pet_label = pet_label.lower().strip()
            labels_dict[image_file] = [pet_label]

    # Replace None with the labels_dict dictionary that you created with this function
    return labels_dict
