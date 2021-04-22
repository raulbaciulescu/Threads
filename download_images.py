import requests
import time
import os.path
import concurrent.futures


start = time.perf_counter()
images = [
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    'https://imgd.aeplcdn.com/476x268/n/cw/ec/38904/mt-15-front-view.jpeg?q=80',
    ]
i = 0
for image_url in images:
    i += 1
    img_bytes = requests.get(image_url).content
    img_name = f'image.jpg'


    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{i} - {img_name} was downloaded!')

finish = time.perf_counter()
print(f'1 ------ Finished in {round(finish - start, 2)} seconds(s)')

start = time.perf_counter()

def download_image(image_url):
    img_bytes = requests.get(image_url).content
    img_name = f'image.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded!')


with concurrent.futures.ThreadPoolExecutor() as executor:
    f = executor.map(download_image, images)


finish = time.perf_counter()
print(f'2 ------ Finished in {round(finish - start, 2)} seconds(s)')