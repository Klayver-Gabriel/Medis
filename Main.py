from Services import ShowSegmentsService, SegmentService , ProcessSegmentService
from Services.ShowSegmentsService import show_multiple_segments


def main():

    output_image = ""
    operation = input("Would you like to run the segmentation algorithm? 1-Yes ")
    if operation == "1":
        input_image = input("Enter the image to segment: ")
        output_image = input("Enter the output folder name: ")
        SegmentService.segmentate(input_image,output_image)
    ShowSegmentsService.show_multiple_segments("Masks.nii",segment_map)
if __name__ == '__main__':
    main()