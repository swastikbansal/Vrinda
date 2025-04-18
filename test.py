from ultralytics import YOLO

model = YOLO('yolov8n.pt')  

model.train(
    data='data.yaml',  
    epochs=10,
    imgsz=640,
    batch=16,
    name='pest_roboflow',        
    project='runs/train'              
)
