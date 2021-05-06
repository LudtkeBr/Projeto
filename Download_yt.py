
#Libs requisitadas para rodar o programa: 
#ffmpeg and youtube-dl -> Mais fácil baixar pelo controle de hambiente do anaconda

#OBS.: O programa baixa as musicas na pasta onde o programa está salvo.

#Importa as libs
import youtube_dl
import sys

#Define os parametros para fazer o download
params ={
    'format': 'bestaudio/best',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    
}

#Cria o objeto do tipo YoutubeDL com os parâmetros carregados
youtube= youtube_dl.YoutubeDL(params)

#Realiza o download chamando o método download do objeto youtube criado acima...
#Passa a url do video ou de uma playlist do yt pra fazer o download no formato mp3 conforme carregado nos params
youtube.download(['https://www.youtube.com/watch?v=BEm0AjTbsac&t=60s'])
