import face_alignment
from skimage import io
import matplotlib.pyplot as plt;
import cv2
import numpy as np

def get_features_mask(img, doEnlarge=True, scale=15):
    """ 
    Returns a binary image mask for the input image's facial features. 
    
    Params:
    img - input image of face to segment facial features from
    doEnlarge - determines if feature masks should be larger than true values
    scale - pixels to enlarge feature by in all directions
    
    Out:
    mask - numpy array of image mask
    """
    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, flip_input=False)
    preds = fa.get_landmarks(img) 
    
    # extract out the points for specific features from the landmarks
    # only use preds[0] to get features on the first face
    eye_left = preds[0][36:42,:]
    eye_right = preds[0][42:48,:]
    mouth = preds[0][48:61,:]
    nose = np.concatenate((preds[0][27:28,:], preds[0][31:36,:]))
    brow_left = preds[0][22:27,:]
    brow_right = preds[0][17:22,:]
    
    # enlarge features (optional)
    if doEnlarge:
        eye_left = enlarge(eye_left, scale=scale)
        eye_right = enlarge(eye_right, scale=scale)
        brow_left = enlarge(brow_left, scale=scale)
        brow_right = enlarge(brow_right, scale=scale)
        mouth = enlarge(mouth, scale=scale)
        nose = enlarge(nose, scale=scale)
    
   
    # create segmented mask with the features present
    mask = np.full_like(img, 0)
    cv2.fillConvexPoly(mask, np.int32(eye_left), (255, 255, 255))
    cv2.fillConvexPoly(mask, np.int32(eye_right), (255, 255, 255))
    cv2.fillConvexPoly(mask, np.int32(mouth), (255, 255, 255))
    cv2.fillConvexPoly(mask, np.int32(nose), (255, 255, 255))
    cv2.fillConvexPoly(mask, np.int32(brow_left), (255, 255, 255))
    cv2.fillConvexPoly(mask, np.int32(brow_right), (255, 255, 255))
    
    return mask
    
    
def enlarge(feature, scale=15):
    """ given a specific feature, return an enlarged version of it"""
    
    # find average feature coordinate to enlarge around
    feature_avg = (np.mean(feature[:,0]), np.mean(feature[:,1])) 
    enlarged = feature.copy()
  
    # expand datapoints around the center coordinate
    enlarged[:,0] = np.where(feature[:,0] < feature_avg[0], feature[:,0], feature[:,0] + scale)
    enlarged[:,1] = np.where(feature[:,1] > feature_avg[1], feature[:,1], feature[:,1] - scale)
    enlarged[:,0] = np.where(feature[:,0] > feature_avg[0], feature[:,0], feature[:,0] - scale)
    enlarged[:,1] = np.where(feature[:,1] < feature_avg[1], feature[:,1], feature[:,1] + scale)
    
    return enlarged