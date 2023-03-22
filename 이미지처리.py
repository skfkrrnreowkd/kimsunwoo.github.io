from PIL import Image

# 이미지 로드
image = Image.open('example.jpg')

# 이미지 크기 변경
image_resized = image.resize((800, 600))

# 이미지 회전
image_rotated = image.rotate(90)

# 이미지 저장
image_resized.save('resized.jpg')
image_rotated.save('rotated.jpg')
