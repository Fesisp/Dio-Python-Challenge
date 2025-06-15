from skimage.io import imread, imsave

def read_image(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image

def save_image(image, path):
    imsave(path, image)

imagem_colorida = read_image('imagem_original.png') # Lê a imagem em cores
imagem_cinza = read_image('imagem_original.png', is_gray=True) # Lê a imagem em escala de cinza

save_image(imagem_colorida, 'imagem_lida_colorida.png')
save_image(imagem_cinza, 'imagem_lida_cinza.png')

print("Imagens lidas e salvas com sucesso!")