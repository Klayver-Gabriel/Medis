import Services

def main():
    operation = input("Would you like to run the segmentation algorithm? 1-Yes ")
    if operation == "1":
        input_image = input("Enter the image to segment: ")
        output_image = input("Enter the output folder name: ")
        Services.segmentate(input_image,output_image)
    data = Services.process_segment("adrenal_gland_left.nii.gz")
    Services.show_segments(data)
if __name__ == '__main__':
    main()