import os

def remove_non_existing_datafiles(data_sets):
    for dataset_name in data_sets:
        full_filename = '../data/cnn.csail.mit.edu/motif_occupancy/' + dataset_name
        if os.path.isdir(full_filename):
            pass
        else:
            print("Warning: Directory {} not found.".format(full_filename))
            data_sets.remove(dataset_name)

    return data_sets

