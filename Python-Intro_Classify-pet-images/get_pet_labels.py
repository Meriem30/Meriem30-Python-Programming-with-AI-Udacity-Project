#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# Meriem ARBAOUI:
# 27 Nov. 2024:
# 28 Nov. 2024:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    files = listdir(image_dir)
    pet_labels_dict = {}

    # for each filename do the necessary processing to generate the correct label
    for file_in in files:
        # First, skip hidden files that starts with '.'
        if file_in.startswith('.'):
            continue
        # only save the name without the extension
        # use split method to generate the list of separated str file parts
        # & only save the first element
        file_name = file_in.split('.')[0]

        # eliminate the underscores
        file_name_list = file_name.split('_')
        # Iterate over the created list to joint up only the alphabit elements, eliminating the numbers
        jointed_name = ''
        for file_name_word in file_name_list:
            if file_name_word.isalpha():
                jointed_name += file_name_word + ' '
            else:
                break
        # convert all letters to lowercase
        jointed_name = jointed_name.lower()
        # remove the whitespace at the end:
        jointed_name = jointed_name.strip()
        # add the created label with its file name (key)
        # as the first element of the list (value)
        # if it's not already in the dict
        if file_in not in pet_labels_dict:
            pet_labels_dict[file_in] = jointed_name
        # print a warning message if it's already exists
        else:
            print(f"Warning: Duplicate files exists ! check the already added element {file_in} to the dict.")
    # return the created dict
    return pet_labels_dict
