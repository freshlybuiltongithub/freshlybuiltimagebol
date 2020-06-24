from requests import get
from os import mkdir,path
from sys import stdout
from tqdm import tqdm


model_url= "https://raw.githubusercontent.com/FreshlyBuilt/freshlybuiltimagebol/master/freshlybuiltimagebol/models/"

def download_model(model_name):
    if path.isfile("models/"+model_name+".pb")==False:
        try:
            mkdir("models")
        except:
            try:
                print('starting model download for the first time')
                print('download can take time depending upon your internet conection')
                with open("models/"+model_name +".pb", "wb") as f:
                    print ("Downloading %s" % model_name)
                    response = get(model_url+model_name+".pb", stream=True)
                    total_length = int(response.headers.get('content-length'))
                    

                    if total_length is None:
                        f.write(response.content)
                    else:
                        chunk_size=1024
                        for data in tqdm(iterable = response.iter_content(chunk_size),total=total_length/chunk_size, unit = 'KB'):
                            f.write(data)
                        tqdm.close()
                if total_length != 0 and tqdm.n != total_length:
                    print("ERROR, something went wrong")
                print('model download successful')
                return 1
            except:
                print('download interrupted')
                return 0
    else: print('model found')
    return 1


""" testing area"""
#model_name=input("model name: ")
#download_model(model_name)           

    
