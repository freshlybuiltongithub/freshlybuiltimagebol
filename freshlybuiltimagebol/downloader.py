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
                    total_length = response.headers.get('content-length')
                    total_length = int(total_length)
                    t=tqdm(total=total_length,unit='kB',unit_scale=True)

                    if total_length is None:
                        f.write(response.content)
                    else:
                        dl = 0
                        for data in response.iter_content(chunk_size=1024):
                            t.update(len(data))
                            f.write(data)
                t.close()
                if total_length != 0 and t.n != total_length:
                    print("ERROR, something went wrong")
                print('model download successful')
                return 1
            except:
                print('oops something went wrong')
                return 0
    else: print('model found')
    return 1

            

    