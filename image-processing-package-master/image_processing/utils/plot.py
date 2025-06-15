# Importa o módulo pyplot da biblioteca matplotlib
import matplotlib.pyplot as plt

def plot_image(image):
    """
    Exibe uma única imagem em escala de cinza.

    Args:
        image (numpy.ndarray): O array da imagem a ser plotada.
    """
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')  # Desliga os eixos
    plt.show()

def plot_result(args):
    """
    Plota múltiplas imagens lado a lado, com a última rotulada como 'Result'.

    Args:
        args (list or tuple): Uma lista ou tupla de objetos imagem a serem plotados.
    """
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))

    # Cria a lista de nomes para as imagens, a última é 'Result'
    names_list = ["Image {}".format(i) for i in range(1, number_images)]
    names_list.append('Result')

    # Itera sobre os subplots, nomes e imagens para plotar
    for ax, name, image in zip(axis, names_list, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off') # Desliga os eixos para cada subplot

    fig.tight_layout() # Ajusta o layout para evitar sobreposição
    plt.show()

def plot_histogram(image):
    """
    Plota os histogramas dos canais de cor (vermelho, verde, azul) de uma imagem.
    Ideal para imagens coloridas (3 canais).

    Args:
        image (numpy.ndarray): O array da imagem (espera-se ser 3D para RGB).
    """
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_list = ['red', 'green', 'blue']

    # Itera sobre os subplots e as cores para plotar cada canal
    for index, (ax, color) in enumerate(zip(axis, color_list)):
        ax.set_title('{} histogram'.format(color.title()))
        # Seleciona o canal específico, achata-o e plota o histograma
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)

    fig.tight_layout() # Ajusta o layout
    plt.show()