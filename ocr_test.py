import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

# Загружаем предобученную модель TrOCR
print("Загружаем процессор и модель...")
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-printed")
print("Процессор и модель загружены.")


image_path = "C:\\Users\\Антон\\Desktop\\3.JPG"  # Укажи свой путь
print(f"Открываем изображение из пути: {image_path}")
image = Image.open(image_path).convert("RGB")  # TrOCR требует RGB
print(f"Размер изображения: {image.size}")


print("Преобразуем изображение для модели...")
pixel_values = processor(images=image, return_tensors="pt").pixel_values
print(f"Размер изображения после преобразования: {pixel_values.shape}")

#  в нейросеть
print("Передаем изображение в модель для распознавания текста...")
with torch.no_grad():
    generated_ids = model.generate(pixel_values)
print("Текст сгенерирован.")

# Декодируем
recognized_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(f"Распознанный текст: {recognized_text}")
