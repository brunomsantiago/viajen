# VIAJEN

**VIAJEN** (**V**iew **I**mages as **A**nimation in **J**upyter and **E**quivalent **N**otebooks) is small library with few dependencies designed to preview video data on Jupyter Notebooks, Google Colab and Kaggle Notebooks.
<p align="center">
  <br>
  <img src="https://github.com/brunomsantiago/viajen/raw/master/docs/animate_folder.gif">
  <br>
</p>
It is specially useful when working with small clips, processing them frame by frame.
I created it to help me test video inpainting techniques, but it may be useful for other applications.
Ultimately the animations are virtual (io.BytesIO) gif files  created by pillow (PIL.Image) and displayed by Ipython (IPython.display.Image). Some animations also need numpy (np.moveaxis, np.split, np.squeeze) to be created.

## How to use

It has just five public functions, which can be explored by jupyter auto-completion.

<p align="center">
  <br>
  <img src="www">
  <br>(TODO: animation showing how to find the content)
</p>

Check the demo notebook ([TODO nbviewer](), [TODO google colab]()) for examples of each one these functions.

<br>

**animate.folder()**
The first function is pretty straightfoward. Just give a folder (string or pathlib object) and it will search for image files, sort them and a display the animation.
By default it only looks for 'jpg' and 'png', but it can be changed with the **file_extensions** parameter, which is a list of strings. The search is based on glob, which is case sensitive, so by default it won't look for 'PNG' or 'jpeg'. Anything pillow opens will probably work.

<br>

**animate.file_list()**
**animate.pillow_list()**
The second and third function are almost the same as the first, but you give the list of image files or pillow image objects you want to display as animation.
The **file_extensions** parameter is also present for the list of image files and the function will ignore files with other extensions.

<br>

**animate.array_list()**
The forth function is little bit different, as it doesn't involve files. Instead the input is list of numpy arrays. It is useful to work with scikit-image and opencv.
As opencv use the BGR channel order instead of RGB, there the flag **BGR** which by default is false and need to be set display opencv frames colors correctly.
Each frame array conversion is done by PIL.Image.fromarray() function, which has the parameter **mode** to control the frame array format. This parameter is also present here and by default is set to None. If necessary see [pillow docs](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes) for more details.

<br>

**animate.array_4d()**
The last function is just a 4D array. It is useful when working some neural networks.
By default it assumes the first 4D arrays dimension order are Time, Height, Width and Color Channel, but if working with different order you can inform the function and it will interpret the data accordingly.
Both the **BGR** and **mode** parameters (see above) are also available here.

<br>

**NOTE:** By default all the five functions limits the number of frames and the animation resolution because the main goal of the library is for quick previews. However the limitations can be bypassed setting the respective parameters (**max_height** and **max_frames**) to None.
