from Services import ShowSegmentsService, SegmentService , ProcessSegmentService
def main():
    operation = input("Would you like to run the segmentation algorithm? 1-Yes ")
    if operation == "1":
        input_image = input("Enter the image to segment: ")
        output_image = input("Enter the output folder name: ")
        SegmentService.segmentate(input_image,output_image)
    data = ProcessSegmentService.process_segment("Results/aorta.nii.gz")
    ShowSegmentsService.show_segments(data)
if __name__ == '__main__':
    main()