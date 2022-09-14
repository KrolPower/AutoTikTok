# Import everything needed to edit video clips
from moviepy.editor import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def split(movieName, clip, clipStart, totalClips, clipEnd):

    # getting only first 5 seconds
    clip = clip.subclip(clipStart, clipEnd)


    # add movie title and part

    # Generate a text clip. You can customize the font, color, etc.
    txt_clip = TextClip("Part_" + str(totalClips), fontsize=70, color='white')


    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_pos('top').set_duration(10)  # --------------------------------- make this be the duration of the clip


    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])


    # Make New Directory and write clips to it

    # importing os module  
    import os 
        
    # Directory 
    directory = str(movieName)
        
    # Parent Directory path 
    parent_dir = "D:/AutoTikTok/AutoTikTok/Output"
        
    # Path 
    path = os.path.join(parent_dir, directory) 

    # create directory
    try: 
        os.mkdir(path)
        print(bcolors.OKGREEN + "Directory '" + movieName + "' Created" + bcolors.ENDC)
    except OSError as error: 
        print(bcolors.WARNING + str(error) + bcolors.ENDC)  
    
    # change directory to output movie clips
    os.chdir(path)

    # Write the result to a file (many options available !)
    video.write_videofile(str(movieName) + "_" + str(totalClips) + ".mp4")
    print(bcolors.OKGREEN + "Clip " + str(movieName) + "_" + str(totalClips) + " Created in Directory " + str(path) + "\n" + bcolors.ENDC)




# Enter movie file path
file = "Source\Piper.mp4"

# Enter Movie Name
movieName = "Piper"


# loading video gfg
clip = VideoFileClip(file)





# getting duration of the video
duration = clip.duration
  
# printing duration
print("Duration : " + str(duration))



# split time into 60 second clips

totalClips = int(duration//60)


clipStart = 0
clipEnd = 60


for i in range(totalClips):
    print("Clip Start: " + str(clipStart))
    print("Clip End: " + str(clipEnd))

    split(movieName, clip, clipStart, i, clipEnd)

    if i < totalClips:
        clipStart += 60
        clipEnd += 60





