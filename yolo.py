from ultralytics import YOLO

model = YOLO('yolov8m-pose.pt')
results = model(source='hostage_18.mkv',show=True,conf=0.3,save=True)

for r in results:
    print(r.keypoints)