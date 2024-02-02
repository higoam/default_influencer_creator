
import os
import time
import cv2
import pathlib
from PIL import Image
from datetime import datetime

from moviepy.editor import *

class ProcessamentoVideo(object):

    def get_durantion_video(self, path_video):
        video = cv2.VideoCapture(path_video)
        frame_rate = video.get(cv2.CAP_PROP_FPS)
        total_num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        duration = total_num_frames / frame_rate
        return duration

        

    '''    
    # Video Generating function 
    def generate_video(): 
    image_folder = '.' # make sure to use your folder 
    video_name = 'mygeneratedvideo.avi'
    os.chdir("/home/higo/Dev/krossy/mundodospequeninos/aux_video/frames/") 
      
    images = [img for img in os.listdir(image_folder) 
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")] 
     
    # Array images should only consider 
    # the image files ignoring others if any 
    print(images)  
  
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape   
  
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))  
  
    # Appending the images to the video one by one 
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image)))  
      
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated 
    '''

