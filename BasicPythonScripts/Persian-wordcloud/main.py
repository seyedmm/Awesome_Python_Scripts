from wordcloud_fa import WordCloudFa
from PIL import Image
from numpy import array

mask_image = Image.open('mask.png')
mask_image = array(mask_image)
Word_c = WordCloudFa(font_path='font.ttf',mask=mask_image,persian_normalize=True,include_numbers=False)
with open('text.txt', 'r') as file:
    text= file.read()


cloud = Word_c.generate(text)
image = cloud.to_image()
image.show()
