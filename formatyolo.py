from ultralytics import YOLO
import supervision as sv
import cv2
import numpy as np

class VideoProcessor:
    def __init__(self, frame_width=1280, frame_height=720):
        self.frame_width = frame_width
        self.frame_height = frame_height     
        self.cap = None
        self.model = None
        self.polygons = None
        self.box_annotator = sv.BoundingBoxAnnotator()
        self.labels_annotator = sv.LabelAnnotator()
        self.zone = None
        self.zone_annotator = None
        

    def configure_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
        
                         
    def zones(self):
        self.polygons =np.array([
            [10,400], 
            [300, 400], 
            [300, 20], 
            [10, 20]
        ])
        
        self.zone = sv.PolygonZone(polygon=self.polygons)
        self.zone_annotator = sv.PolygonZoneAnnotator(
        zone=self.zone, 
        color=sv.Color.RED,
        thickness=2,
        text_thickness=4,
        text_scale=2
    )
        
        
    
    def configure_model(self):
        self.model =YOLO('yolov8n.pt')
            
    
    def process_frame(self, frame):
        result = self.model.predict(frame)[0]
        detections = sv.Detections.from_ultralytics(result)
        
        labels = [
            f"{class_name} {confidence:.2f}"
            for class_name, confidence
            in zip(detections['class_name'], detections.confidence)
        ]
        
        frame = self.box_annotator.annotate(
            scene=frame,
            detections=detections,
        )
        frame = self.labels_annotator.annotate(
            scene=frame,
            detections=detections,
            labels=labels
        )
        self.zone.trigger(detections=detections)
        frame = self.zone_annotator.annotate(scene=frame)
        
        return frame
    
    def run(self):
        self.configure_camera()
        self.configure_model()
        self.zones()
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            frame = self.process_frame(frame)
            
            cv2.imshow("ketquanhandien", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    processor = VideoProcessor()
    processor.run()
