from PIL import Image

img = Image.new('RGB', (300, 100), color='white')
img.save('image.png')