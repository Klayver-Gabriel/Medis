import random

from totalsegmentator.python_api import totalsegmentator
def segmentate(image:str,output_name:str):
    totalsegmentator(image,output_name,ml=True,fastest=True)

def segment_map(segments_indeces):
    segments_properties = {}
    for i,index in enumerate(segments_indeces):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        transparency = random.uniform(0.5,0.8)
        segments_properties[index] = {
           'color':color,
           'alpha':transparency,
        }
        print(f"Indice: {index} cor: {color} transparência: {transparency}")
    return segments_properties