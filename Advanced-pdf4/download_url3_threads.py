import threading
import requests
import json
import time

with open("Advanced-pdf4/urls.json", "r") as json_file:
    data = json.load(json_file)
    image_urls = data["image_urls"]  

def calculate_time(func):

    def inner_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken: {end - start} seconds")
        return result
    return inner_func


@calculate_time
def download_imgs(url,num):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"{num}.png", "wb") as file:
                    file.write(response.content)
                print(f"Content downloaded successfully from {url}!")
            else:
                print(f"Failed to download content from {url}.")
        except:
            print(f"An error occurred for {url}.")

t1 = threading.Thread(target=download_imgs, args=(image_urls[0]["url"],1))
t2 = threading.Thread(target=download_imgs, args=(image_urls[1]["url"],2))
t3 = threading.Thread(target=download_imgs, args=(image_urls[2]["url"],3))
t4 = threading.Thread(target=download_imgs, args=(image_urls[3]["url"],4))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()


