from ultralytics import YOLO
import cv2

class PlateDetector:
    def __init__(self, model_path='plate-detector.pt'):
        self.model = YOLO(model_path)

    def detect_plates(self, image_path:str):
        img = cv2.imread(image_path)
        results = self.model.predict(source=img)
        detections = []
        
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                crop = img[y1:y2, x1:x2]
                detections.append({
                    "bbox": (x1, y1, x2, y2),
                    "conf": float(box.conf.item()),
                    "crop": crop
                })
         
            
        return detections    