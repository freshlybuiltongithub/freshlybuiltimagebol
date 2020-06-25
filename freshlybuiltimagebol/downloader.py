from requests import get
from os import mkdir,path,remove
from sys import stdout
from tqdm import tqdm
from time import sleep


class imagebol_model_downloader:
    
    status_code=0000
    
    def __init__(self,model_name,status_code=0):
        self.download_model(model_name,status_code)

    def download_model(self,model_name,status_code=0):
        available_models={"F_est":["frozen_east_text_detection","94.4MB"]}
        model_url= "https://raw.githubusercontent.com/FreshlyBuilt/freshlybuiltimagebol/master/freshlybuiltimagebol/models/"
        if model_name in available_models:
            model_name=available_models[model_name]
            if path.isfile("models/"+model_name[0]+".pb")==False:
                try:
                    mkdir("models")
                except:
                    try:
                        print('starting model download for the first time')
                        sleep(1)
                        print('download can take time depending upon your internet conection')
                        with open("models/"+model_name[0] +".pb", "wb") as f:
                            print(model_name[0]+" is of "+model_name[1])
                            choice=input("do you wish to download/ntype 'y':")
                            if (choice=='y'):
                                response = get(model_url+model_name[0]+".pb", stream=True)
                                    
                            else:
                                print('download canceled')
                            
                            try:
                                response.raise_for_status()   
                                    
                            except response.exceptions.HTTPError as errh:
                                print ("Http Error:",errh)
                                self.status_code=1004
                                return status_code
                            except response.exceptions.ConnectionError as errc:
                                print ("Error Connecting:",errc)
                                self.status_code=1005
                                return status_code
                            except response.exceptions.Timeout as errt:
                                print ("Timeout Error:",errt)
                                self.status_code=1006
                                return status_code
                            except response.exceptions.RequestException as err:
                                print ("OOps: Something Else",err)
                                self.status_code=1007
                                return status_code
                            
                            total_length = int(response.headers.get('content-length'))
                            if total_length is None:
                                f.write(response.content)
                            else:
                                chunk_size=1024
                                for data in tqdm(iterable = response.iter_content(chunk_size),total=total_length/chunk_size, unit = 'KB'):
                                    f.write(data)
                                tqdm.close()
                                f.close()
                        if total_length != 0 and tqdm.n != total_length:
                            print("ERROR, something went wrong")
                        print('model download successful')
                        self.status_code=1003
                        return status_code
                    except:
                        print('\ndownload interrupted')
                        try:
                            remove("models/"+model_name[0] +".pb")
                            self.status_code=1002
                            return status_code
                        except:
                            self.status_code=1002
                            return status_code
                            
            else:
                print('model already exist')
                self.status_code=1000
                return status_code
            
            
        else: 
            print("no reference found for "+model_name)
            self.status_code=1001
            return status_code

"""status_code_meanings"""
# 1000 - model already exist
# 1001 - model name incorrect
# 1002 - download interupted
# 1003 - successful download
# 1004 - http error
# 1005 - connection error
# 1006 - timeout error
# 1007 - miscellanious error
      

""" testing area"""
#model_name=input("model name: ")
#print(imagebol_model_downloader(model_name).status_code)           

    