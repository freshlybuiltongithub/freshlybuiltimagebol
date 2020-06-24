from requests import get
from os import mkdir,path
from sys import stdout

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
                        total_length = response.headers.get('content-length')

                        if total_length is None: # no content length header
                            f.write(response.content)
                        else:
                            dl = 0
                            total_length = int(total_length)
                            for data in response.iter_content(chunk_size=4096):
                                dl += len(data)
                                f.write(data)
                                done = int(50 * dl / total_length)
                                stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                                stdout.flush()
                print('model_download_successful')
                return 1
            except:
                 print('oops something went wrong')
                 return 0
    else: print('model found')
    return 1
        

    