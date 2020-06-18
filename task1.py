import numpy as np
from PIL import Image, ImageStat

import os

def mouse_loc(img_path: str):
    """Calculate in which compartment the mouse is."""
    input_img = Image.open(img_path)
    c1, c2, c3 = (122, 104, 271, 480), (298, 100, 445, 480), (468, 102, 620, 480) # coordinates of rectangular boundaries of the three compartments 
    extra = np.array([585, 585, 585, 140, 140, 140, 760, 760, 760]) # precalculated variance values of empty compartments
    stats = np.array(ImageStat.Stat(input_img.crop(c1)).var + ImageStat.Stat(input_img.crop(c2)).var + ImageStat.Stat(input_img.crop(c3)).var)
    stats = stats - extra 
    result = stats[::3].tolist()   
    return result.index(max(result))

def main():
    locations = []
    for filename in os.listdir("images"):
        locations.append(mouse_loc("images/" + filename))

    time1, time2, time3 = locations.count(0), locations.count(1), locations.count(2)
    print(f"The mouse spent {time1}s, {time2}s and {time3}s in compartments 1, 2, and 3 respectively, counting from the left.")

if __name__ == "__main__":
    main()
