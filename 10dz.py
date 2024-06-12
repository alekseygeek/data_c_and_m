import torch
from torch import nn
from transformers import SegformerImageProcessor, SegformerForSemanticSegmentation
from PIL import Image
import matplotlib.pyplot as plt
import requests

#  определения устройства
device = (
    "cuda"
    # Устройство для NVIDIA или AMD GPUs
    if torch.cuda.is_available()
    else "mps"
    
    if torch.backends.mps.is_available()
    else "cpu"
)

# загрузка модели
image_processor = SegformerImageProcessor.from_pretrained("jonathandinu/face-parsing")
model = SegformerForSemanticSegmentation.from_pretrained("jonathandinu/face-parsing")
model.to(device)

# загрузка изображения 

url = "https://globalsib.com/wp-content/uploads/2017/09/2000x1333_0xc0a839a2_6963696981478781887.jpg"
image = Image.open(requests.get(url, stream=True).raw)

# вывод по изображению
inputs = image_processor(images=image, return_tensors="pt").to(device)
outputs = model(**inputs)
logits = outputs.logits  # shape (batch_size, num_labels, ~height/4, ~width/4)

# изменение размеров
upsampled_logits = nn.functional.interpolate(logits,
                size=image.size[::-1], # H x W
                mode='bilinear',
                align_corners=False)

# получение масок
labels = upsampled_logits.argmax(dim=1)[0]

# перейти к процессору для визуализации в matplotlib
labels_viz = labels.cpu().numpy()
plt.imshow(labels_viz)
plt.show()



