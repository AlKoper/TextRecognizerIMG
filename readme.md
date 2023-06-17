# Text Recognizer IMG
____

Скрипт распознает текст из изображений и сохраняет его в отдельном файле соответствующей папки. Для этого использую библиотеку "easyocr". 
Эта модель имеет множество настроек и пригодится для разного пула задач. Документация модели:
- https://www.jaided.ai/easyocr/documentation/
- https://github.com/jaidedai/easyocr

ВАЖНО:
По умолчанию easyocr использует GPU (можно использовать и CPU, на Windpws возникают проблемы). Поэтому важно правльно установить важнеы зависимости (не только сам модуль). Система должна иметь CUDA, которую можно найти по ссылкам:
- Linux: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
- Windows: https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html

Перед использованием также необходимо установить pyTorch:
- https://pytorch.org/get-started/locally/

Выполнив эти шаги, скрипт будет работать!


P.S.
Скрипт основан на модели easyocr. На момент написания это наиболее эффективная и простая модель для распознавания текста из изображений. Однако есть и другая интерсная модлье, которая имеет хороший функционал. Это Tesseract. Подробную информацию с примеро кода по этой библиотеки вы найдет по ссылке:
- https://www.youtube.com/watch?v=UPjTYorn59g
