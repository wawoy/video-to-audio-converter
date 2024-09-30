import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    try:
        # Load the video file
        video = VideoFileClip(input_file)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to a file
        audio.write_audiofile(output_file)
        
        # Close the video file
        video.close()
        
        print(f"Conversion complete. Audio saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("MP4 to MP3 Converter")
    
    # Get input file path
    input_file = input("Enter the path to the MP4 file: ")
    
    # Check if file exists
    if not os.path.exists(input_file):
        print("Error: The specified file does not exist.")
        return
    
    # Get output file path
    output_file = input("Enter the path for the output MP3 file: ")
    
    # Perform conversion
    convert_mp4_to_mp3(input_file, output_file)

if __name__ == "__main__":
    main()
