import urllib.request
import cv2
import os
#img_link='https://i.ytimg.com/vi/HBxn56l9WcU/maxresdefault.jpg'
#road_id="0"
def get_query():
    im_name="img.jpg"
    img_link='http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5a823bd55058170011f6eaa0&t=1540214970801'
    urllib.request.urlretrieve(img_link,im_name)
    return img_link
