import requests

# url = 'http://127.0.0.1:5000/im_size'
# my_img = {'image': open('/home/neelesh/Downloads/download.jpeg', 'rb')}
# r = requests.post(url, files=my_img)

# convert server response into JSON format.
# print(r.json())

get_image_url = 'http://127.0.0.1:5000/get_image'
r = requests.get(get_image_url)
file = open("return.png", "wb")
file.write(r.content)
file.close()