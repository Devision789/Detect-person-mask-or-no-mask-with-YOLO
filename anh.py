import cv2
from ultralytics import YOLO
from tkinter import filedialog

class ImageInference:
    def __init__(self, model_path="best.pt"):
        self.model = YOLO(model_path)

    def run(self):
        # Open file dialog to select an image
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if image_path:
            source = cv2.imread(image_path)
            results = self.model.predict(source, classes=[1, 3], save=True)

            # Display the result
            annotated_image = results[0].plot()
            cv2.imshow("YOLOv8 Inference", annotated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
