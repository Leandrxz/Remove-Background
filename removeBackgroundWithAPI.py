import requests
import os
from tkinter import Tk, filedialog
from PIL import Image

#definições
apiKey = os.getenv("apiKey")
inputFolder = filedialog.askopenfilename(
    title = "Input path:"
)
outputFolder = filedialog.askopenfilename(
    title="Output Path: "
)
size = (1200, 1200)

os.makedirs(outputFolder, exist_ok=True)

#fun~çao pra remover o fundo e salvar com o novo tamanhom
def remove(input_path, output_path, size=size):
    try:
        with open (input_path, "rb") as image_file:
            response = requests.post(
                "https://api.remove.bg/v1.0/removebg",
                files={"image_file": image_file},
                data={"size": "auto"},
                headers={"X-api-key": apiKey},
            )
#if pra salvar caso funcione
        if response.status_code == 200:

            with open(output_path, "wb") as out:
                out.write(response.content)

            img = Image.open(output_path)
            img = img.resize(size)
            img.save(output_path, "PNG")
            print(f"Success: {os.path.basename(output_path)} ({size[0]}x{size[1]})")

        else:
            print(f"Erro de API ({response.status_code}): {response.text}")

    except Exception as e:
        print(f"Erro no processamento {input_path}: {e}")


#for pra continuar processando as img
for file in os.listdir(inputFolder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(inputFolder, file)
        output_path = os.path.join(outputFolder, file.rsplit('.', 1)[0] + ".png")
        remove(input_path, output_path)
        