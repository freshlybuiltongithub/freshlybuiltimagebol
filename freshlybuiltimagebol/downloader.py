from requests import get
from os import mkdir
from os.path import isfile,isdir

class Model_File():
	"""
	Download the model if not already exists.
	Pass the model name and the model will be downloaded if not already exisis.
	"""
	def __init__(self,model_name):
		url="https://github.com/ZER-0-NE/EAST-Detector-for-text-detection-using-OpenCV/blob/master/"+model_name+".pb?raw=true"
		output_dir="freshlybuiltimagebol/models/"+model_name+".pb"
		if isfile(output_dir):
			print("Model already exists")
		else:
			ch=int(input("Do you want to download it.\n Type 1 for yes"))
			if ch==1:
				print("Downloading...")
				response = get(url)
				if response.status_code==200:
					if isdir("freshlybuiltimagebol/models"):
						pass
					else:
						mkdir("freshlybuiltimagebol/models")
					with open(output_dir, 'wb') as file:
						file.write(response.content)
					print("Download Successful")
				elif response.status_code==404:
					print("Model not found")
				else:
					print("Not able to download")
