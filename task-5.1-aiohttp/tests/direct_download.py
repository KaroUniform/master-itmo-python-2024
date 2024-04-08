# Этот скрипт служит для сравнения асинхронного скачивания с обычным "прямым" скачиванием по порядку
import requests
import os
import time 

start_time = time.time()
os.makedirs('person_images', exist_ok=True)
num_images = 50
for i in range(num_images):
    response = requests.get('https://thispersondoesnotexist.com')
    if response.status_code == 200:
        image_path = f'person_images/person_{i}.jpg'
        
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f'Изображение {i+1} загружено и сохранено как {image_path}')
    else:
        print(f'Ошибка при загрузке изображения {i+1}: {response.status_code}')

end_time = time.time()
print(f"Downloads completed in {end_time - start_time:.2f} seconds")