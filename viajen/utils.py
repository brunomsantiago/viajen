# Standard library imports
from pathlib import Path

# Thirdy party imports
import numpy as np


def clip_list(my_list, max_len):
    if max_len:
        if max_len < len(my_list):
            my_list = my_list[0:max_len]
    return my_list


def verify_file_list(files, file_extensions):
    error_message = f"list don't have image files ({file_extensions})"
    valid_files = []
    for file in files:
        file = Path(file)
        if file.exists() and file.suffix.strip('.') in file_extensions:
            valid_files.append(file)
    assert valid_files, error_message
    return valid_files


def verify_folder(folder):
    error_message = 'folder is not valid'
    assert isinstance(folder, str) or isinstance(folder, Path), error_message
    folder_path = Path(folder)
    assert folder_path.is_dir(), error_message
    return folder_path


def folder_to_file_list(folder, file_extensions):
    error_message = f"folder don't have image files ({file_extensions})"
    folder_path = verify_folder(folder)
    files = []
    for ext in file_extensions:
        ext_files = list(folder_path.glob(f'*.{ext}'))
        files.extend(ext_files)
    assert files, error_message
    return sorted(files)


def move_dimensions(array, current_dimensions, new_dimensions):
    new_dimensions = new_dimensions.upper()
    current_dimensions = current_dimensions.upper()
    current_indexes = [current_dimensions.find(dimension)
                       for dimension in current_dimensions]
    new_indexes = [current_dimensions.find(dimension)
                   for dimension in new_dimensions]
    return np.moveaxis(array, current_indexes, new_indexes)


def array4d_to_array_list(array4d, array4d_dims):
    # 'THWC' = (Time, Height, Width, Channels)
    standard_dims = 'THWC'
    array4d_dims = array4d_dims.upper()
    if array4d_dims != standard_dims:
        array4d = move_dimensions(array4d, array4d_dims, standard_dims)
    n_frames = array4d.shape[0]
    list_of_4d_arrays = np.split(array4d, n_frames, axis=0)
    array_list = [np.squeeze(x, axis=0) for x in list_of_4d_arrays]
    return array_list
