# Lembra de dar pip install pelo terminal do pycharm no JinaAI, gTTS e openai se estiver usando
from jinaai import JinaAI
from gtts import gTTS
import openai
import os
import base64
# Se for testar mude esse caminho para o seu vvv
img_caminho = 'C:/Users/Richard/Documents/Richard/imagem1.jpg'
cont = 0

def image_to_data_uri(file_path):
    with open(file_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:image/jpeg;base64,{encoded_image}"

def transformar_imagem(lingua, abv):
    jinaai = JinaAI(
        secrets={
            # Se a chave expirar cria uma nova conta no scenexplain, gera uma nova chave e coloca no lugar dessa
            'scenex-secret': 'XVOQd1bL38HEoHPRl034:f513c618c7ea968414f7a35abdb92b1002bf0452b65e43f9479b453732ef8d18'

        }
    )

    descriptions = jinaai.describe(
        image_to_data_uri(img_caminho)
    )

    openai.api_key = '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'
    model_engine = "text-davinci-003"
    max_tokens = 1024

    linguagem = abv

#Mude o tamanho da descrição aqui
    prompt = 'Resuma em 30 palavras em' + lingua + 'o seguinte texto:' + str(descriptions)
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    texto = str(completion.choices[0].text)
    converter_mp3 = gTTS(text=texto, lang=linguagem, slow=False)
    # Use seu própio caminho se for testar vvv
    converter_mp3.save('C:/Users/Richard/Documents/Richard/audio.mp3')

def tocar_audio():
    # Use seu própio caminho se for testar vvv
    os.system('C:/Users/Richard/Documents/Richard/audio.mp3')



while True:
    menu = input('''
    =========================================
    | Bem vindo ao descritor de imagens! ⬤  |   
    | 1 - Descrever imagem                  | 
    | 2 - Tocar audio mais recente          | 
    | 3 - Sair                              |
    =========================================
    Digite: ''')

    if menu == '1':
        foi = False
        while foi == False:
            escolha = input('Digite a linguagem que deseja escolher(Inglês, Espanhol, Português): ')

            if escolha == 'Inglês' or escolha == 'inglês' or escolha == 'ingles':
                abv = 'en'
                print('Analizando imagem...')
                transformar_imagem(escolha, abv)
                tocar_audio()
                cont+= 1
                foi = True

            elif escolha == 'Espanhol' or escolha == 'espanhol':
                abv = 'es'
                print('Analizando imagem...')
                transformar_imagem(escolha, abv)
                tocar_audio()
                cont += 1
                foi = True

            elif escolha == 'Português' or escolha == 'português' or escolha == 'portugues':
                abv = 'pt'
                print('Analizando imagem...')
                transformar_imagem(escolha, abv)
                tocar_audio()
                cont += 1
                foi = True

            else:
                print('Valor inválido, tente novamente!')

    elif menu == '2':
        if cont == 0:
            print('Nenhum áudio foi tocado recentemente...')
            print('Retornando...')
        else:
            print('Tocando áudio...')
            tocar_audio()

    elif menu == '3':
        print('Até mais!')
        break

    else:
        print('Você digitou um valor inválido, tente novamente!')



