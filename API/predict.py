import cv2
import tensorflow as tf
import keras
from keras import backend as K
CATEGORIES = ["traffic", "road"]


def prepare(filepath):
    IMG_SIZE = 80  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    #print("i reached here")
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def predict(file_dir):
    print("12312412424234235235asfssdfjvndkfDEDUNCE")
    model = keras.models.load_model("traffic_detection.model")
    #model.summary()
    results=[]
    prediction = model.predict([prepare(file_dir)])
    #print('abraham')
    #print(prediction)
    if (prediction[0][0]>prediction[0][1]):
        results.append('traffic')
        print ('traffic')
    else:
        results.append('road')
        print('road')
    results.append(prediction[0][0])
    results.append(prediction[0][1])
    K.clear_session()
    return results

#5h30-5h55 Troi mua, buoi toi
#1.jpeg road --wrong/maybe?
#2.jpeg road
#3.jpeg NKKN-dien bien phu - traffic
#4.jpeg Nguyen van troi- huynh van banh - traffic
#5.jpeg nga 4- phu nhuan 2 - traffic
#6.jpeg Nguyen Kiem- Ho Van Hue 1 -road
#7.jpeg Nguyen Van Troi- tran Huy Lieu road --wrong
#8.jpeg duong ham- Ky con road --wrong
#9.jpeg Nguyen Trai- Nguyen Van Cu traffic
#10.jpeg Nguyen Van Cu- Tran Hung Dao traffic
#11.jpeg Hong Bang- Ngo Quyen traffic
#12.jpeg Hai Thuong Lan Ong- Cau Cha Va traffic
#13.jpeg Hong Bang - Chau Van Liem --road --wrong/ is it?
#14.jpeg Hong Bang - Chau Van Liem -traffic correct (see the difference)
# 15.jpeg Hai Thuong Lan Ong-cau cha va traffic
#16.jpeg pham van dong- le quang dinh road --wrong
#17.jpeg Hiep Binh-Quoc Lo 13 traffic
#Nguyen Van Cu - Tran Hung Dao 5h42 ket xe rat nhieu
#18.jpeg Hong Bang Ngo Quyen road --wrong
#19.jpeg Cong Hoa- Binh Gia traffic
#20.jpeg Cong Hoa-ut tich traffic
#21.jpeg Truong Chinh - Tan Ky Tan Quy traffic
#22.jpeg Phan Thuc Dien - Tran Quoc Hoan road --wrong
#23.jpeg Nga Sau- Nguyen Thai Son 2 road --wrong
#24.jpeg Nguyen Oanh - Phan Van Tri 2 traffic
#25.jpeg Nguyen Oanh - Phan Van Tri 1 traffic
#26.jpeg Hiep Binh - Quoc Lo 13 traffic
#27.jpeg Nam Ky Khoi Nghia - Ly Chinh Thang road --wrong ***************
#28.jpeg Hoang Van Thu- Nguyen Van Troi 2 road --wrong
#29.jpeg Hoang Van Thu- Ho Van Hue traffic
#30.jpeg Hoang Van Thu - Nguyen Van Troi 1 traffic
