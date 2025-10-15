from totalsegmentator.python_api import totalsegmentator
def segmentate(image:str,output_name:str):
    totalsegmentator(image,output_name,ml=True)

def segment_map(segments_indeces):
   #TODO: CRIAR UMA LISTA DE OBJETOS QUE POSSUEM CARACTERISTICA COR e TRANSPARÊNCIA
   for index in segments_indeces:
       map = {
       }