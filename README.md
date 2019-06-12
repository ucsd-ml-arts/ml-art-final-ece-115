# Final Project

Justine Lee, jul199@ucsd.edu

Victor Miranda, vmiranda@ucsd.edu

## Abstract Proposal

We will be bringing back the project 4 for our final project where we generate a stylized image. Our goal is to create our own camera similar to a polaroid using a Raspberry Pi and a picamera and send the picture taken through a neural network. Our desired creative goal is to integrate the software from machine learning with hardware. This allows the users to visualize the world in another style. We will be presenting our work in the final project presentation through example photos we have taken with the actual camera as well as the interface of the camera.

## Project Report

Our final project report can be found here: [Final Project Report](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/blob/master/ECE%20188%20Final%20Project%20Report.pdf)

## Model/Data

- The model used to run the program is the pre-trained neural network, VGG-19 ([download link](https://github.com/alexjc/neural-doodle/releases/download/v0.0/vgg19_conv.pkl.bz2)).
- There is no training data in the traditional sense; the data used by the program includes content and style images and their respective segmentation masking images.
- Content images are images that are taken on the Raspberry Pi (RPi) camera module.
- Segmentation of an image such as `<image_name>.jpg` is saved as `<image_name>_sem.png`.
- Content images (and their segmentation images) can be found in the [`samples_content`](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/tree/master/samples_content) directory.
- Style images (and their segmentation images) can be found in the [`samples_style`](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/tree/master/samples_style) directory.
- Directories that start with `frames_` hold images that show progress of sematic style transfer examples through iterations.

## Code

You can use the [`segment.py`](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/blob/master/segment.py) script to generate segmentation maskings for desired images.
- In order to generate segmentation maskings for desired images, execute `python segment.py --content <content_image_name> ---style <style_image_name> --clusters <number_of_clusters>`. (note: do not include the `.jpg` extension for image names)
- The `--clusters` parameter specifies how many k-means clusters you would like to make, which corresponds to the number of unique colors in a segmentaion masking image.
- Open/Run the (`segment_visuals.ipynb`)[https://github.com/ucsd-ml-arts/ml-art-final-ece-115/blob/master/segment_visuals.ipynb] notebook to see how the k-means algorithm creates clusters to generate segmentation masking images.

You can use the [`doodle.py`](https://github.com/ucsd-ml-arts/generative-visual-group-ece-115/blob/master/doodle.py) script to generate visuals using a previously trained model (ex. VGG-19).
- In order to generate visuals, execute `python doodle.py --style samples_style/<style_image_name>.jpg --output samples_content/<output_image_name>_resized.png --device=cpu --iterations=40`.
- The `--iterations` parameter specifies how many iterations per phase you would like to make.

## Results

The final results are saved as image files in the [`results`](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/tree/master/results) directory. A collage of final results for this project can be found here: [Final Collage](https://docs.google.com/document/d/1jnNvAf6oiMX2bmNCnMKpvXF0K6zn5Qc-QuiKX2Uw_Ws/edit?usp=sharing). Collages of final results from project 4 can also be found in the [`collages`](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/tree/master/collages) directory.
- Some of our results came out clear while others were difficult to distinguish. You really have to compare images side by side to find any similarities within pictures and too see if Neural Doodle was doing its job.

## Technical Notes

As mentioned previously, content images are images that are taken on the RPi camera module. The technical implementation of the physical camera was inspired by the ["Cartoonify"](https://github.com/danmacnish/cartoonify) project. Instead of generating sketches from captured images, we generate sematic style transferring from captured images.
- In order to capture images on the RPi using a camera module, a button, and an LED, setup a raspberry pi with the following hardware files in the [`rpi`](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/tree/master/rpi) directory.
- After setting up your raspberry pi hardware, run the [`takePic.py`](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/blob/master/rpi/takePic.py) script in the [`rpi`](https://github.com/ucsd-ml-arts/ml-art-final-ece-115/tree/master/rpi) directory to capture and save images.
- In order to transfer captured images from your RPi camera to your PC or DataHub, use the `rsync -avr -e ssh --rsync-path=cluster-rsync <image_folder_path> <datahub_username>@ieng6.ucsd.edu:<save_folder_path>` command on your raspberry pi. (note: syncing folder into path `<save_folder_path>` means creating a folder into this path)
- Once you have the pictures transferred to your PC or DataHub in their proper folders (content images in `samples_content` and style images in `samples_style`), follow the steps under the `code` section to run the semantic style transfer algorithm with your desired images.

This code requires the use of the following dependencies (for processing on PC or DataHub):
- numpy
- matplotlib
- scikit-learn
- Pillow
- colorama
- pillow>=3.2.0
- Theano>=0.8.1
- git+https://github.com/Lasagne/Lasagne.git@0440814#egg=Lasagne==0.2-dev

To install the dependencies, run the `pip install -r requirements.txt` command on your PC or DataHub.

## References

- Project 4 GitHub Repo - [Generative Visual](https://github.com/ucsd-ml-arts/generative-visual-group-ece-115)
- GitHub user 'alexjc' - [Neural Doodle](https://github.com/alexjc/neural-doodle)
- GitHub user 'danmacnish' - [Cartoonify](https://github.com/danmacnish/cartoonify)
- Raspberry Pi Projects - [The All-Seeing Pi](https://projects.raspberrypi.org/en/projects/the-all-seeing-pi/8)
- Pulkit Sharma - [Introduction to Image Segmentation Techniques](https://www.analyticsvidhya.com/blog/2019/04/introduction-image-segmentation-techniques-python/)
- Karen Simonyan, Andrew Zisserman - [VGG-19 pre-trained model](https://arxiv.org/abs/1409.1556)