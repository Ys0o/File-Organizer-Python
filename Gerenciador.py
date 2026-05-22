from pathlib import Path    #Path cria objetos (arquivos, diretórios, caminhos e etc...)
import shutil               #shutil usada para mover arquivos, copiar e etc...

pasta = Path("Path Teste")    #Criação de variável e transformação em objeto

tipos = {                     #Dicionário ( Chave -> Valor)
    ".png" : "Imagens P",
    ".mp3" : "Audios P",
    ".mp4" : "Videos P",
    ".txt" : "Texto P"
    }

for item in pasta.iterdir():              #Analisa/Percorre cada item da pasta. /  Item - arquivo atual do loop.
    categoria = tipos[item.suffix]        #Descobre a categorio do arquivo.     /  Suffix descobre a extensão do arquivo (png,mp3,mp4...)
    Path(categoria).mkdir(exist_ok=True)  #Cria a pasta da categoria automaticamente.
    print(item.suffix)
    print(categoria)
    shutil.move(item, categoria)          #Move o arquivo para a pasta correta.

