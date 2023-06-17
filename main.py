import easyocr
from pathlib import Path


#основная функция, которая будет анализировать изображения
def text_recogniser():
    input_path = Path('C:/Users/lobod/PycharmProjects/Text Recognizer IMG/Input imgs/')
    image_ext = ['*.jpg', '*.png']    #укажем, с какими расширениями изображений будем работать
    reader = easyocr.Reader(["ru"], gpu=True)    #загрузим модель, указав язык перевода
    for exs in image_ext:
        for file in input_path.glob(exs):    #перебираем каждый файл с соотвествубщим расширением из заданного пути
            file_name = Path(file).stem
            result = reader.readtext(str(file), detail=0, paragraph=True)    #запустим модель для распознавания текста из изображения
            with open(f'C:/Users/lobod/PycharmProjects/Text Recognizer IMG/Output text/{file_name}.txt', 'w') as txt_file:   #запишем текст в новый файл и сохраним его в отдельную папку
                txt_file.write(str(result))

def main():
    text_recogniser()


if __name__ == '__main__':
    main()