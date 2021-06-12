from pytube import YouTube

link=input('please input the video URL:')

video=YouTube(link)

print(f'the video title is \n{video.title}  \n_________________')
print(f'the video description is \n{video.description} \n______________')
print(f'the video viwes are \n{video.viwes} \n ____________')
print(f'the video rating is \n{video.rating} \n_____________')
print(f'the video length is \n{video.length/60} miutes \n_____________')

"""
streams represent the vidoe quality => 720px is a video image stream..and there are streams 
for sounds also
"""

#for stream in video.streams:
    #print(stream) 


for stream in video.streams.filter(progressive=True):
    print(stream)    

  #progressive=True means videos include both image and sound , see print(video.streams) to understand
  # if you want to identify the image quality of the video , add res=720p to filter 


#print(video.streams.get_higher_resolution()) if i want to directly install the highest res video without using filter

# to download=>
video.streams.get_higher_resolution().download(output_path='C:\Users\STUDENT\Desktop\downloaded videos')

# to make sure that the video is downloaded successfully

def finish():
    print('downloaded successfully')

video.register_on_complete_callback(finish())   



# to download a whole playlist

from pytube import playlist

playlist_link=input('please enter the playlist link :')

playlist=playlist(playlist_link)


for video in playlist.videos:
    video.streams.get_higher_resolution().download(output_path='C:\Users\STUDENT\Desktop\downloaded videos')



  


                  


 