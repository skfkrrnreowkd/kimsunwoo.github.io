import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# 데이터 로드
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# 데이터 전처리
train_images, test_images = train_images / 255.0, test_images / 255.0

# 모델 구성
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# 모델 학습
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

# 새로운 이미지 분류 예측
import numpy as np
from tensorflow.keras.preprocessing import image

# 이미지 로드 및 전처리
img_path = "test_image.jpg"
img = image.load_img(img_path, target_size=(32, 32))
img_array = image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) / 255.0

# 모델 예측
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

# 결과 출력
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
               'dog', 'frog', 'horse', 'ship', 'truck']
print("This image most likely belongs to {} with a {:.2f} percent confidence."
      .format(class_names[np.argmax(score)], 100 * np.max(score)))
