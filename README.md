## face_detection using Viola-Jones Algorithm
Viola Jones algorithm is named after two computer vision researchers who proposed the method in 2001, Paul Viola and Michael Jones in their paper, “Rapid Object Detection 
using a Boosted Cascade of Simple Features”. Despite being an outdated framework, Viola=Jones is quite powerful, and its application has proven to be exceptionally notable in real-time face detection. This algorithm is painfully slow to train but can detect faces in real-time with impressive speed. Given an image (this algorithm works on grayscale image), the algorithm looks at many smaller subregions and tries to find a face by looking for specific features in each subregion. It needs to check many different positions and scales because an image can contain many faces of various sizes. Viola and Jones used Haar-like features to detect faces in this algorithm.

It works on four stages,

•	**Selecting Haar-like features**: A Haar-like feature consists of dark regions and light regions. It produces a single value by taking the difference of the sum of the intensities of the dark regions and the sum of the intensities of light regions. It is done to extract useful elements necessary for identifying an object. The features proposed by Viola-Jones are,

![image](https://user-images.githubusercontent.com/84698110/161754460-0fa907f8-7552-41bb-9c00-7ec5601940a8.png)

•	**Creation of Integral Images**: A given pixel in the integral image is the sum of all the pixels on the left and all the pixels above it. Since the process of extracting Haar-like features involves calculating the difference of dark and light rectangular regions, the introduction of Integral Images reduces the time needed to complete this task significantly.

•	**AdaBoost Training**: This algorithm selects the best features from all features. It combines multiple “weak classifiers” (best features) into one “strong classifier”. The generated “strong classifier” is basically the linear combination of all “weak classifiers”.

•	**Cascade Classifier**: It is a method for combining increasingly more complex classifiers like AdaBoost in a cascade which allows negative input (non-face) to be quickly discarded while spending more computation on promising or positive face-like regions. It significantly reduces the computation time and makes the process more efficient.

OpenCV already contains many pre-trained classifiers for face, eyes, smile etc. Input the image in grayscale mode then load the required XML classifiers. Then we find faces in the image. If faces are found, it returns the positions of detected faces as rectangle (column, row, width, height).
