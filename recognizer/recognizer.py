import easyocr
import numpy as np

class PlateOCR:
    def __init__(self):
        self.reader = easyocr.Reader(['ru'], gpu=False)

    def recognize_text(self, image_np: np.ndarray) -> str:
        result = self.reader.readtext(image_np)
        if result:
            return result[0][-2]
        return ""
