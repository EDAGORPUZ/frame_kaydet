import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Varsayılan kamerayı açtık
frame_sayacı = 0  # Framelerin frame1, frame2 şeklinde ayrı ayrı kaydedilmesi için sayaç oluşturuldu.

while True:
    ret, frame = cap.read()
    cv2.imshow('webcam', frame)

    key = cv2.waitKey(1) & 0xFF  # Komutu key'in içine atamadan direkt yazdığımda hata aldım dikkat!!

    if key == ord('s'):  # Eğitimdeki 'q' tuşu ile ekran kapama şablonu ile aynı mantık.
        frame_sayacı += 1
        
        # file = f'../output/frame_{frame_sayacı}.jpg'  #direkt bir önceki klasöre çıktığı için çalışmadı
        file = f'./output/frame_{frame_sayacı}.jpg'  #mevcut dizindeki bir üst klasöre çıkıyor. 

        cv2.imwrite(file, frame)  # file değişkenine frameleri kaydet
        print(f"Frame kaydedildi: {file}")  # Kaydedilen frame'in adını yazdır
    elif key == ord('q'):  # 'q' tuşuna basıldığında çıkış yapılır
        break

cap.release()
cv2.destroyAllWindows()
