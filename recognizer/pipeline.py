
from recognizer.detector import PlateDetector
from recognizer.recognizer import PlateOCR
from recognizer.utils import clean_and_validate
import cv2

def run_pipeline():
    image_path = "samples/sample1.jpg"
    model_path = "model/yolov8n_license.pt"

    detector = PlateDetector(model_path)
    ocr = PlateOCR()

    detections = detector.detect(image_path)

    for det in detections:
        crop = det["crop"]
        text = ocr.recognize_text(crop)
        validated = clean_and_validate(text)

        print(f"[DETECTED] raw: {text} → cleaned: {validated}")
        cv2.imshow("plate", crop)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()
