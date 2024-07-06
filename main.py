import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from camera import WebcamInference
from anh import ImageInference
from vid import VideoInference

class MainApplication:
    def __init__(self, master):
        self.master = master
        master.title("Nhận Diện Người Đeo Khẩu Trang")
        
        # Set window size and center it
        window_width = 800
        window_height = 600
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        master.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        
        master.configure(bg="#f0f8ff")

        # Title Label
        self.title_label = tk.Label(
            master, text="Nhận Diện Người Đeo Khẩu Trang",
            font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#333"
        )
        self.title_label.pack(pady=20)

        # Subtitle Label
        self.subtitle_label = tk.Label(
            master, text="Trường Đại học Bách Khoa TP HCM",
            font=("Helvetica", 18), bg="#f0f8ff", fg="#666"
        )
        self.subtitle_label.pack(pady=10)

        self.advisor_label = tk.Label(
            master, text="Giáo viên hướng dẫn: Nguyễn Văn A",
            font=("Helvetica", 14), bg="#f0f8ff", fg="#666"
        )
        self.advisor_label.pack(pady=5)

        self.student_label = tk.Label(
            master, text="Sinh viên thực hiện: Nguyễn Văn B",
            font=("Helvetica", 14), bg="#f0f8ff", fg="#666"
        )
        self.student_label.pack(pady=5)

        # Buttons
        self.webcam_button = tk.Button(
            master, text="Webcam", command=self.run_webcam, font=("Helvetica", 16),
            bg="#4CAF50", fg="white", activebackground="#45a049", padx=20, pady=10
        )
        self.webcam_button.pack(pady=20)

        self.image_button = tk.Button(
            master, text="Image", command=self.run_image, font=("Helvetica", 16),
            bg="#2196F3", fg="white", activebackground="#1e88e5", padx=20, pady=10
        )
        self.image_button.pack(pady=20)

        self.video_button = tk.Button(
            master, text="Video", command=self.run_video, font=("Helvetica", 16),
            bg="#FF5722", fg="white", activebackground="#f4511e", padx=20, pady=10
        )
        self.video_button.pack(pady=20)

    def run_webcam(self):
        webcam_inference = WebcamInference()
        webcam_inference.run()

    def run_image(self):
        image_inference = ImageInference()
        image_inference.run()

    def run_video(self):
        video_inference = VideoInference()
        video_inference.run()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
