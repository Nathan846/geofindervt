# UserInterface_ComputerVision_GoPro
This is collaboration with Dr. Junghwan Kim (Department of Geography@Virginia Tech) to create a user friendly desktop application that uses pre-trained Computer Vision models on geographical video files (captured by GoPro). The extracted metadata is saved in a CSV file. The tool consists of two main components: VideoConverter and ImageExtractor.

## Installation
To install this tool from PyPI, use the following command:
```
pip install geofinder-vt
```

## Usage
### VideoConverter Class
The VideoConverter class is used to extract images from video files in a specified folder.

```
from geofinder_vt import VideoConverter

video_folder = "campus_video_test"  # Specify the folder where your video files are stored
converter = VideoConverter(video_folder)
converter.video_extract_folder()
```
Methods
`__init__(self, video_folder_prefix)`: Initializes the VideoConverter with the specified folder prefix.
video_extract(self, video_file): Extracts images from a single video file using the extract_video function.
video_extract_folder(self): Extracts images from all video files in the specified folder.


Example Usage
# Application Title: Geospatial Image on Map Viewer

[√] Extract image frames from video files

[] Run pre-trained computer vision models on image frames

[] Display the results on a map

[] User Interface

[] User Manual

[] Demo Video

[] Presentation Slides

[] Final Report
