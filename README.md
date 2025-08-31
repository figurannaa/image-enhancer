# Image Enhancer
Resizes and enhances images to the desired size
## Usage 
1. Install python3 
2. Clone the repository
3. Go into the repository's folder
4. Execute the script with the following command:
    - `python3 image-enhancer.py -e -w [desired width] -H [desired height] -p [path to image]`
    - OR
    - `python3 image-enhancer.py --enhance --width [desired width] --height [desired height] --path [path to image]`
## Guide
- You can keep the original ratio by only specifiying **one** dimension
- Using *-e* or *--enhance* flags will enhance the quality of the image by modifying sharpness, contrast and blurness
