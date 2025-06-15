# Importa as funções necessárias do setuptools para configurar o pacote.
from setuptools import setup, find_packages

# Abre o arquivo README.md para ler a descrição longa do seu pacote.
# O conteúdo será usado no campo 'long_description'.
with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

# Abre o arquivo requirements.txt para ler as dependências do seu pacote.
# Cada linha no requirements.txt se torna um item na lista 'requirements'.
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

# Chama a função setup para configurar e descrever o seu pacote Python.
setup(
    name="image_processing",  # O nome do seu pacote. Será usado para instalação (ex: pip install image_processing).
    version="0.0.1",          # A versão atual do seu pacote. Recomenda-se usar versionamento semântico (MAJOR.MINOR.PATCH).
    author="Karina",          # O nome do autor do pacote.
    # author_email="seu.email@example.com", # Opcional: E-mail do autor.
    description="Image Processing Package using skimage",  # Uma breve descrição do seu pacote.
    long_description=page_description, # A descrição longa do pacote, lida do README.md.
    long_description_content_type="text/markdown", # O formato da sua descrição longa (aqui, Markdown).
    url="https://github.com/tiemi/image-processing-package", # Opcional: URL para o repositório do seu projeto.
    packages=find_packages(), # Automaticamente encontra todos os pacotes (diretórios com __init__.py) no seu projeto.
    install_requires=requirements, # Lista de dependências que serão instaladas com o seu pacote.
    python_requires='>=3.5',  # A versão mínima do Python exigida para o seu pacote.
    # Opcional: Classificadores para ajudar os usuários a encontrar seu pacote no PyPI.
    # Veja a lista completa em: https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # Ou a licença que você estiver usando
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
)