
import os
import time
import cv2
import pathlib
from PIL import Image
from datetime import datetime

from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def get_durantion_video(path_video):
    video = cv2.VideoCapture(path_video)
    frame_rate = video.get(cv2.CAP_PROP_FPS)
    total_num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = total_num_frames / frame_rate
    return duration

def break_video_to_story(path_dir,name_file):

    path_video = path_dir + '/' + name_file
    duration_video = get_durantion_video(path_video)

    print(' |   Comprimento Video')
    print(' |   ', str(duration_video))

    # Criar Dir
    print(' |   Criar Dir to Story')
    cmd = 'mkdir ' + path_dir + '/story_video'
    os.system(cmd)
    time. sleep(2)

    if duration_video < 60:
        print(' |   Ate 1 min')
        cmd = 'cp ' + path_video + ' ' + path_dir + '/story_video/' + 'clip_1.mp4'
        os.system(cmd)

    elif duration_video < 120:
        print(' |   Ate 2 min')
        '''
        path_clip_2 = path_dir + '/story_video/' + 'clip_2.mp4' 
        ffmpeg_extract_subclip(path_video, 0, 59, targetname=path_clip_2)

        path_clip_1 = path_dir + '/story_video/' + 'clip_1.mp4' 
        ffmpeg_extract_subclip(path_video, 60, duration_video, targetname=path_clip_1)
        '''
    elif duration_video < 180:            
        print(' |   Ate 3 min')
        '''
        path_clip_3 = path_dir + '/story_video/' + 'clip_3.mp4' 
        ffmpeg_extract_subclip(path_video, 0, 59, targetname=path_clip_3)

        path_clip_2 = path_dir + '/story_video/' + 'clip_2.mp4' 
        ffmpeg_extract_subclip(path_video, 60, 119, targetname=path_clip_2)

        path_clip_1 = path_dir + '/story_video/' + 'clip_1.mp4' 
        ffmpeg_extract_subclip(path_video, 120, duration_video, targetname=path_clip_1)
        '''
    elif duration_video < 240:            
        print(' |   Ate 3 min')
        '''
        path_clip_4 = path_dir + '/story_video/' + 'clip_4.mp4' 
        ffmpeg_extract_subclip(path_video, 0, 59, targetname=path_clip_4)

        path_clip_3 = path_dir + '/story_video/' + 'clip_3.mp4' 
        ffmpeg_extract_subclip(path_video, 60, 119, targetname=path_clip_3)

        path_clip_2 = path_dir + '/story_video/' + 'clip_2.mp4' 
        ffmpeg_extract_subclip(path_video, 120, 179, targetname=path_clip_2)

        path_clip_1 = path_dir + '/story_video/' + 'clip_1.mp4' 
        ffmpeg_extract_subclip(path_video, 180, duration_video, targetname=path_clip_1)
        '''
    else:
        print('Nao Publica, maior que 4 minutos')
            #Nao publica


    print('   [ Falta Implementar: Publica no Story ]\n')




    # Obter Duracao do Video

    # Quebrar Video

    # Mover Video para Dir


        

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

