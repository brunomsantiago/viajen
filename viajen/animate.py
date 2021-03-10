# Standard library imports
from io import BytesIO as _BytesIO

# Thirdy party imports
from IPython.display import Image as _display_image
from PIL import Image as _Image

# Project imports
import utils as _utils

_default = {}
_default['max_height'] = 300
_default['max_frames'] = 200
_default['file_extensions'] = ['jpg', 'png']


def _base_animation(pillow_images, max_height):
    # Resize Images
    if max_height:
        width, height = pillow_images[0].width, pillow_images[0].height
        if max_height < height:
            for image in pillow_images:
                image.thumbnail((width, max_height))
    # Create gif in memory
    gif_file = _BytesIO()
    pillow_images[0].save(gif_file,
                          format='gif',
                          save_all=True,
                          append_images=pillow_images[1:],
                          loop=0)
    animation = gif_file.getvalue()
    return _display_image(animation)


def pillow_list(images,
                max_height=_default['max_height'],
                max_frames=_default['max_frames']):
    images = _utils.clip_list(images, max_frames)
    return _base_animation(images, max_height)


def file_list(files,
              max_height=_default['max_height'],
              max_frames=_default['max_frames'],
              file_extensions=_default['file_extensions']):
    files = _utils.clip_list(files, max_frames)
    files = _utils.verify_file_list(files, file_extensions)
    images = [_Image.open(file) for file in files]
    return _base_animation(images, max_height)


def folder(folder_path,
           max_height=_default['max_height'],
           max_frames=_default['max_frames'],
           file_extensions=_default['file_extensions']):
    files = _utils.folder_to_file_list(folder_path, file_extensions)
    files = _utils.clip_list(files, max_frames)
    images = [_Image.open(file) for file in files]
    return _base_animation(images, max_height)


def array_list(arrays,
               max_height=_default['max_height'],
               max_frames=_default['max_frames'],
               BGR=False,
               mode=None,
               ):
    arrays = _utils.clip_list(arrays, max_frames)
    if BGR:
        arrays = [array[:, :, ::-1] for array in arrays]
    images = [_Image.fromarray(array, mode=mode) for array in arrays]
    return _base_animation(images, max_height)


def array_4d(array4d,
             array4d_dims='THWC',
             max_height=_default['max_height'],
             max_frames=_default['max_frames'],
             BGR=False,
             mode=None):
    # 'THWC' = (Time, Height, Width, Channels)
    arrays = _utils.array4d_to_array_list(array4d, array4d_dims=array4d_dims)
    return array_list(arrays,
                      max_height=max_height,
                      max_frames=max_frames,
                      BGR=BGR,
                      mode=mode)
