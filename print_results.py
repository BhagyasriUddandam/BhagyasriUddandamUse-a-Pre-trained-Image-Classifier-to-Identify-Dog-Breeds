#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Bhagyasri
# DATE CREATED: 02/11/2023
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(custom_results_dict, custom_stats_dict, selected_model, 
                  print_misclassified_dogs=False, print_misclassified_breeds=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      custom_results_dict - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      custom_stats_dict - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      selected_model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_misclassified_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_misclassified_breeds - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    print("\n\n*** Results Summary for CNN Model Architecture", selected_model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', custom_stats_dict['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', custom_stats_dict['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', custom_stats_dict['n_notdogs_img']))
    print(" ")
    for key in custom_stats_dict:
        if key.startswith('p'):
            print("{:20}: {:.2f}%".format(key, custom_stats_dict[key]))
    if (print_misclassified_dogs and 
        (custom_stats_dict['n_correct_dogs'] + custom_stats_dict['n_correct_notdogs']
         != custom_stats_dict['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in custom_results_dict:
            if custom_results_dict[key][3] == 1 and custom_results_dict[key][4] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(custom_results_dict[key][0], custom_results_dict[key][1]))
            elif custom_results_dict[key][3] == 0 and custom_results_dict[key][4] == 1:
                print("Real: {:>26}   Classifier: {:>30}".format(custom_results_dict[key][0], custom_results_dict[key][1]))
    if (print_misclassified_breeds and 
        custom_stats_dict['n_correct_dogs'] != custom_stats_dict['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        for key in custom_results_dict:
            if sum(custom_results_dict[key][3:]) == 2 and custom_results_dict[key][2] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(custom_results_dict[key][0], custom_results_dict[key][1]))
