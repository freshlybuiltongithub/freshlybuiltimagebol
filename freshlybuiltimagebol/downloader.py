from hashlib import md5
from os import mkdir, path, remove

import colorama as col
from requests import get
from tqdm import tqdm

"""
freshlybuiltimagebol library model downloader
status_code for checking the execution status
code   meaning
1000 - model already exist
1001 - model name incorrect
1002 - download interupted
1003 - successful download
1004 - http error
1005 - connection error
1006 - timeout error
1007 - miscellanious error
1008 - building models directory
1009 - signature mismatch 
"""


class imagebol_model_downloader:
    status_code = 0000

    def __init__(self, model_name, status_code=0000):
        self.download_model(model_name, status_code)

    def download_model(self, model_name, status_code):
        dir_path = path.dirname(path.realpath(__file__))

        available_models = {
            "F_est": [
                "frozen_east_text_detection",
                "94.4MB",
                "8a9b7f2ebd9bcf8212bfa856b065e6f0",
            ]
        }

        if path.isdir(dir_path + "models/") == False:
            try:
                mkdir(dir_path + "/models")
            except:
                print("models directory found")

        if model_name in available_models:
            model_name = available_models[model_name]
            if path.isfile(dir_path + "/models/" + model_name[0] + ".pb") == False:
                try:
                    print('starting model download')
                    print("don't quit until downlaoding completes")
                    print(
                        'download can take time depending upon your internet conection'
                    )
                    print(Fore.BLUE + model_name[0] + " is of " + model_name[1])
                    choice = input(Fore.YELLOW + "do you wish to download type 'y':")
                    if choice == 'y':
                        return self.start_downloading(model_name, dir_path, status_code)
                    else:
                        print('download canceled')
                        status_code = 0000
                        return status_code
                    print('model download successful')
                    self.status_code = 1003
                    return status_code
                except:
                    print('download interrupted')
                    try:
                        remove(dir_path + "/models/" + model_name[0] + ".pb")
                        self.status_code = 1002
                        return status_code
                    except:
                        self.status_code = 1002
                        return status_code
            else:
                print('model found')
                print('checking encryption signature')
                self.hash_signature_match(
                    model_name, available_models, dir_path, status_code
                )
                if self.status_code == 1000:
                    return self.status_code
                else:
                    print(self.status_code)
                    print(Fore.CYAN + model_name[0] + " is of " + model_name[1])
                    re_choice = input(
                        Fore.YELLOW + "press 'y' to start re-downloading: "
                    )
                    if re_choice == 'y':
                        remove(dir_path + "/models/" + model_name[0] + ".pb")
                        self.start_downloading(model_name, dir_path, status_code)
                        self.hash_signature_match(
                            model_name, available_models, dir_path, status_code
                        )
                        return self.status_code

        else:
            print("no reference found for " + model_name)
            self.status_code = 1001
            return status_code

    def start_downloading(self, model_name, dir_path, status_code):
        model_url = "https://raw.githubusercontent.com/FreshlyBuilt/freshlybuiltimagebol/master/freshlybuiltimagebol/models/"
        response = get(model_url + model_name[0] + ".pb", stream=True)
        try:
            response.raise_for_status()
        except response.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            self.status_code = 1004
            return self.status_code
        except response.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            self.status_code = 1005
            return self.status_code
        except response.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            self.status_code = 1006
            return self.status_code
        except response.exceptions.RequestException as err:
            print("OOps: Something Else", err)
            self.status_code = 1007
            return self.status_code
        with open(dir_path + "/models/" + model_name[0] + ".pb", "wb") as f:
            total_length = int(response.headers.get('content-length'))
            if total_length is None:
                f.write(response.content)
            else:
                chunk_size = 1024
                for data in tqdm(
                    iterable=response.iter_content(chunk_size),
                    total=total_length / chunk_size,
                    unit='KB',
                ):
                    try:
                        f.write(data)
                    except:
                        pass

    def hash_signature_match(self, model_name, available_models, dir_path, status_code):
        model_checksum = dir_path + "/models/" + model_name[0] + ".pb"
        md5_hash = md5()
        model_handler = open(model_checksum, "rb").read()
        md5_hash.update(model_handler)
        hash_code = md5_hash.hexdigest()
        if hash_code == model_name[2]:
            col.init(autoreset=True)
            print(col.Fore.GREEN + "signature matched")
            col.deinit()
            self.status_code = 1000
            return status_code
        else:
            col.init(autoreset=True)
            print(
                Fore.RED + "warning signature mismatched, model may not work properly "
            )
            col.deinit()
            self.status_code = 1009
            return status_code


"""downloader_debugger"""
# model_name=input("model name: ")
# print(imagebol_model_downloader(model_name).status_code)
