import cv2

# Открываем камеру (0 - это индекс по умолчанию для первой камеры)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Ошибка при открытии камеры!")
    exit()

while True:
    # Чтение кадра с камеры
    ret, frame = cap.read()
    
    if not ret:
        print("Не удалось захватить кадр!")
        break
    
    # Отображаем кадр в окне
    cv2.imshow('Webcam', frame)
    
    # Выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
