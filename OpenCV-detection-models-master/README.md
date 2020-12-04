# OpenCV-detection-models
OpenCV public trained detection models: Haar, HOG and other.

There are public XML-files of trained models to detection of different objects: cars, planes, people, animals, plants and other most popular objects.

**This is branch for OpenCV 2.4.12**

Available branches:

* [OpenCV 2.4.12](https://github.com/AlexeyAB/OpenCV-detection-models/tree/master)
* [OpenCV 3.0](https://github.com/AlexeyAB/OpenCV-detection-models/tree/3.0)


Used detection methods:

* HaarCascades [cv::CascadeClassifier (C++ class)](http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html#CascadeClassifier)
* HaarCascades CUDA [gpu::CascadeClassifier_GPU (C++ class)](http://docs.opencv.org/modules/gpu/doc/object_detection.html#gpu::CascadeClassifier_GPU)
* [cv::LatentSvmDetector (C++ class)](http://docs.opencv.org/modules/objdetect/doc/latent_svm.html#LatentSvmDetector)
* [CvSVM](http://docs.opencv.org/modules/ml/doc/support_vector_machines.html#cv2.SVM)
* [gpu::HOGDescriptor (C++ structure)](http://docs.opencv.org/modules/gpu/doc/object_detection.html#gpu::HOGDescriptor)


Sources of models:

* [Itseez/opencv_extra - LatentSVMdetector](https://github.com/Itseez/opencv_extra/tree/2.4.12.x-prep/testdata/cv/latentsvmdetector)
* [Itseez/opencv - cascades: Haar, HOG and LBP](https://github.com/Itseez/opencv/tree/2.4.12.x-prep/data)


Soft for training:

* HaarCascades: https://github.com/mrnugget/opencv-haar-classifier-training
* HOG: https://github.com/DaHoC/trainHOG


OpenCV documentation: http://docs.opencv.org/genindex.html