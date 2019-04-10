import os


def remove_non_existing_datafiles(dataset):
    dataset_to_remove = []
    for dataset_name in dataset:
        full_filename = '../data/cnn.csail.mit.edu/motif_occupancy/' + dataset_name
        if not os.path.isdir(full_filename):
            print("Warning: Directory {} not found.".format(full_filename))
            dataset_to_remove.append(dataset_name)

    for dataset_name in dataset_to_remove:
        dataset.remove(dataset_name)

    return dataset


def remove_non_existing_datafiles_buggy(dataset):
    for dataset_name in dataset:
        full_filename = '../data/cnn.csail.mit.edu/motif_occupancy/' + dataset_name
        if not os.path.isdir(full_filename):
            print("Warning: Directory {} not found.".format(full_filename))
            dataset.remove(dataset_name)
    return dataset


if __name__ == '__main__':
    print("This example shows how easy it is to write a buggy program")
    print("******")
    b = ['wgEncodeAwgTfbsHaibK562Bclaf101388Pcr1xUniPk']
    b = remove_non_existing_datafiles_buggy(b)
    print("*****")

    print("******")
    datasets2 = ["wgEncodeAwgTfbsHaibK562Bcl3Pcr1xUniPk",
                 "wgEncodeAwgTfbsHaibK562Bclaf101388Pcr1xUniPk",
                 "wgEncodeAwgTfbsSydhK562Bdp1UniPk"]
    datasets2 = remove_non_existing_datafiles_buggy(datasets2)
    print("*****")
    print("Lesson Learned: do not update the list which you are iterating though in your for loop")

