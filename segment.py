#import necessary libraries
import argparse
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

#argument parser
parser = argparse.ArgumentParser(
    description='Apply k-means clustering to content and style images to create segmentation maskings.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--content', default=None, type=str, help='Content image name.')
parser.add_argument('--style', default=None, type=str, help='Style image name.')
parser.add_argument('--clusters', default=None, type=int, help='Number of k-means clusters.')
args = parser.parse_args()

#k-means segmentation function
def kmeans_segment(content,style,clusters=5):
    #read normalized images
    print('Reading images...')
    pic1 = plt.imread('./samples_content/'+content+'.jpg')/255  # dividing by 255 to bring the pixel values between 0 and 1
    pic2 = plt.imread('./samples_style/'+style+'.jpg')/255  # dividing by 255 to bring the pixel values between 0 and 1
    #vectorize images
    print('Vectorizing images...')
    pic1_n = pic1.reshape(pic1.shape[0]*pic1.shape[1], pic1.shape[2])
    pic2_n = pic2.reshape(pic2.shape[0]*pic2.shape[1], pic2.shape[2])
    #apply k-means
    print('Applying k-means...')
    kmeans1 = KMeans(n_clusters=clusters, random_state=0).fit(pic1_n)
    pic2show1 = kmeans1.cluster_centers_[kmeans1.labels_]
    kmeans2 = KMeans(n_clusters=clusters, random_state=0).fit(pic2_n)
    pic2show2 = kmeans1.cluster_centers_[kmeans2.labels_]
    #save clustered pictures (consistent masking)
    print('Saving clustered images...')
    cluster_pic1 = pic2show1.reshape(pic1.shape[0], pic1.shape[1], pic1.shape[2])
    plt.imsave('./samples_content/'+content+'_sem.png',cluster_pic1)
    cluster_pic2 = pic2show2.reshape(pic2.shape[0], pic2.shape[1], pic2.shape[2])
    plt.imsave('./samples_style/'+style+'_sem.png',cluster_pic2)
    print('Done')

#valid argument checker
if (args.content is None) or (args.style is None) or (args.clusters is None):
    print('Please provide valid arguments and try again!')

#run k-means segmentation function
else:
    print('Starting...')
    image1 = args.content
    image2 = args.style
    num_clusters = args.clusters
    kmeans_segment(image1,image2,clusters=num_clusters)