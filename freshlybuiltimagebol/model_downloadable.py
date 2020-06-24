import requests
import urllib
import os
import sys

model_url= "https://raw.githubusercontent.com/ravi5175/freshlybuiltimagebol/master/freshlybuiltimagebol/models/"
def download_model(model_name):
    if os.path.isfile("models/"+model_name+".pb")==False:
        try:
            os.mkdir("models")
        except:
            print('directory exist')
            try:
                print('starting model download for the first time')
                print('download can take time depending upon your internet conection')
                #model=requests.get(model_url+model_name+".pb")
                with open("models/"+model_name +".pb", "wb") as f:
                        print ("Downloading %s" % model_name)
                        response = requests.get(model_url+model_name+".pb", stream=True)
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
                                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                                sys.stdout.flush()
                print('download complete')
                print('writing model ')
                #open('models/'+model_name+'.pb','wb').write(model.content)
                print('model_download_successful')
            except:
                 print('oops something went wrong')
        

    else: print('model found')

model_name=input()
download_model(model_name)    

    