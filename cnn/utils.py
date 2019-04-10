import os

def remove_non_existing_datafiles(dataset):
    for dataset_name in dataset:
        full_filename = '../data/cnn.csail.mit.edu/motif_occupancy/' + dataset_name
        if os.path.isdir(full_filename):
            pass
        else:
            print("Warning: Directory {} not found.".format(full_filename))
            dataset.remove(dataset_name)

    return dataset

