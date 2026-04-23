# import the packages
import os

# Mounting the google drive
from google.colab import drive
drive.mount('/content/gdrive')

# Google Drive Path
#gDrivePath = "gdrive/MyDrive/Colab Notebooks/COVID19_FaceMaskDetection/"
gDrivePath ="/content/gdrive/MyDrive/Collab_notebook/COVID19_FaceMaskDetection"

# original input directory of images
BASE_PATH = gDrivePath + "dataset"

# Output Path Directory
outputPath = gDrivePath + "output"

# defining the directories
TRAIN = "training"
VAL = "validation"
TEST = "evaluation"

CLASSES = ["withMask","withoutMask"]

# setting the parameters
BATCH_SIZE = 32
INIT_LR = 1e-4
EPOCHS = 20

# setting the path to save the serialized model after training
MODEL_PATH = os.path.sep.join([outputPath, "facemask.model"])

# setting the path for the output training history plots
PLOT_PATH = os.path.sep.join([outputPath, "plot.png"])
