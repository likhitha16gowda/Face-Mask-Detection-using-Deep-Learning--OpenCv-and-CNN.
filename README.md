# Face-Mask-Detection-using-Deep-Learning--OpenCv-and-CNN.
Face mask detection using MobileNetV2 and OpenCV for real-time deep learning-based image and video analysis.

This project presents an automated face mask detection system using Deep Learning and Computer Vision techniques. The model is built using a Convolutional Neural Network (CNN) with transfer learning based on the MobileNetV2 architecture and integrated with OpenCV for real-time detection.

### Features
- Detects faces with and without masks
- Real-time video stream detection using webcam
- High accuracy (~97%) on test data
- Lightweight and efficient model (MobileNetV2)
- Data augmentation for improved generalization

### Technologies Used
- Python
- TensorFlow / Keras
- OpenCV
- NumPy & Matplotlib

### Model Details
- Base Model: MobileNetV2 (pre-trained on ImageNet)
- Transfer Learning with fine-tuning
- Binary classification: Mask / No Mask

### Dataset
- 7,553 labeled images
- Classes: `with_mask`, `without_mask`
- Data augmentation applied to training set

### Applications
- Public safety monitoring
- Smart surveillance systems
- Real-time compliance detection

### Results
- Achieved ~97% accuracy
- Strong precision and recall for both classes

### Future Work
- Detect improperly worn masks
- Deploy on edge devices (Raspberry Pi, Jetson)
- Multi-person and multi-camera detection

### Author
Likhitha Mahadeva
