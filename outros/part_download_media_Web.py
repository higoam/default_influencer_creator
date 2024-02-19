
import os
import time

from processamento_video import break_video_to_story


def provisoria():

    path_dir_main    = '/home/higo/Dev/medias_to_post/petts/outros'
    files_of_dir_videos = os.listdir(path_dir_main)

    for x in files_of_dir_videos:
        
     
#        break_video_to_story(path_dir,x)

        path = path_dir_main + '/' + x
        path_reel = 'mkdir ' + path + '/reel'
        cmd = 'mkdir ' + path + '/reel'

        print(' |  ',x)

    # Criar Dir
    print(' |   Criar Dir to Story')
    cmd = 'mkdir ' + path_dir + '/story_video'
    os.system(cmd)
    time. sleep(2)


def download_media_by_web():

    path_dir_main    = '/home/higo/Dev/medias_to_post/petts/outros'
    dir_videos = os.listdir(path_dir_main)


    for x in dir_videos:

        path = path_dir_main + '/' + x

        files = os.listdir(path)

        for y in files:
            if '.mp4' in y:
                print(y)
                cmd = 'mv ' + path + '/' + y + ' ' + path + '/reel'
                os.system(cmd)


    # -------------------------------------------------------
    '''
    for x in dir_videos:

        path = path_dir_main + '/' + x

        files = os.listdir(path)

        for y in files:
            if '.mp4' in y:
                print(y)
                cmd = 'mv ' + path + '/' + y + ' ' + path + '/reel'
                os.system(cmd)
    '''


download_media_by_web()