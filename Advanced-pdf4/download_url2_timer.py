import requests
import json
import time


def calculate_time(func):

    def inner_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken: {end - start} seconds")
        return result
    return inner_func

@calculate_time
def download_imgs():
   with open("Advanced-pdf4/urls.json", "r") as json_file:
    data = json.load(json_file)
    image_urls = data["image_urls"]  
    i=1
    for item in image_urls:
        url = item["url"] 
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"{i}.png", "wb") as file:
                    file.write(response.content)
                print(f"Content downloaded successfully from {url}!")
                i +=1
            else:
                print(f"Failed to download content from {url}.")
        except:
            print(f"An error occurred for {url}.")


download_imgs()

