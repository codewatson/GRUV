from data_utils.parse_files import *

#TODO - Make these command line arguments
input_directory = 'datasets/YourMusicLibrary/'
output_filename = 'datasets/YourMusicLibraryNP'

freq = 44100 		#sample frequency in Hz
clip_len = 10 		#length of clips for training. Defined in seconds
block_size = 11025 	#block sizes used for training - this defines the size of our input state
max_seq_len = int(round((freq * clip_len) / block_size)) #Used later for zero-padding song sequences
#Step 1 - convert MP3s to WAVs
new_directory = convert_folder_to_wav(input_directory)
#Step 2 - convert WAVs to frequency domain with mean 0 and standard deviation of 1
convert_wav_files_to_nptensor(new_directory, block_size, max_seq_len, output_filename)