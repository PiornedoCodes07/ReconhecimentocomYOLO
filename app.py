#Importando Yolo da biblioteca Ultralytics
from ultralytics import YOLO
#Criando a variavel que armazena o Yolo, com sua versão
modelo = YOLO("yolov8n.pt")
#Definindo o modelo 
modelo.predict(source='0', show=True)