from PIL import Image
color_image = Image.open("India_gate.jpg")
gray_scale = color_image.convert("L")
gray_scale.save("gray_gate.jpg")