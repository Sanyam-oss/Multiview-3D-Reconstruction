# Multiview-3D-Reconstruction

## Motivation
- 3D scene representation is a challenging and ongoing research area in computer vision, with numerous techniques proposed, from traditional image processing to advanced methods like deep neural networks and transformer models. This work employs traditional image processing techniques and Incremental Structure from Motion (SfM) algorithm for 3D reconstruction to create 3D point clouds of objects.

- 3D reconstruction from multiple photographs is crucial for applications like autonomous driving and augmented reality; however, specialized sensors like LIDAR can be expensive and complicated to use.

- Advances in digital cameras, improved resolution, and clarity have enabled new, more affordable 3D reconstruction techniques using only RGB cameras, without the need for expensive sensors.

- Structure from Motion (SfM) reconstructs 3D structures from multiple photographs taken from different viewpoints, with the main challenges being resilience, precision, completeness, and scalability; an incremental approach is used to address these issues.

## Objective

- Structure from Motion (SfM) reconstructs 3D structures from multiple photographs taken from different viewpoints. 

- This work employs traditional image processing techniques and Incremental Structure from Motion (SfM) algorithm for 3D reconstruction to create 3D point clouds of objects.

- The proposed method is evaluated using specific 3D reconstruction datasets to assess its performance.

# Datasets and Original Tasks
The dataset comprises of images of different 3D structures along with intrinsic camera matrix of the camera used to capture these images. All images for the given structure are captured using the same camera such that the order of images showcase a 360 degree motion of the camera around the structure. For each structure the number of images and their resolution is variable.

- We searched the web to obtain some of the 3D structure images available on the internet provided their intrinsic camera matrix was also available.

- We utilised our own phone’s(OnePlus 7) camera to obtain photographs of structures and obtained the camera’s intrinsic matrix using camera calibration methods discussed in the course utilising a 12x9 checkerboard.

In the Dataset folder, there is a separate folder for each structure. In a given structure folder there are images for that structure and a K.txt file containing the intrinsic camera matrix.

# Methodology
 <p align="center">
<a>
    <img width="1080" alt="image" src="https://github.com/Sanyam-oss/Multiview-3D-Reconstruction/blob/main/3DRCSFM_Pipeline.png">
</a>
 </p>

 For more details :  [3DRCSFM](https://github.com/Sanyam-oss/Multiview-3D-Reconstruction/blob/main/3DRCSFM_Presentation.pdf)

# Results
We observe that the quality of reconstructed scenes depends on several factors :
- Resolution and quality of images (Two cameras used) 
- Number and distribution of keypoints (Different types of objects used : Speaker, Buddha, Statue)
- Number of image views
- With the number of the images and the quality of the distinct structure features visible in the images, the reprojection error decreases.
- However, we can observed certain spikes in the reprojection error graphs, which showcase the importance of images features and positioning for the 3D reconstruction 
- More results are available in the folder result folder for reference with different structures.

 <p align="center">
<img width="880" alt="image" src="https://github.com/Sanyam-oss/Multiview-3D-Reconstruction/blob/main/readme_util/Buddha1-Results.png">
 </p>

  <p align="center">
<img width="880" alt="image" src="https://github.com/Sanyam-oss/Multiview-3D-Reconstruction/blob/main/readme_util/Buddha2-Results.png">
 </p>

  <p align="center">
<img width="880" alt="image" src="https://github.com/Sanyam-oss/Multiview-3D-Reconstruction/blob/main/readme_util/statue-results.png">
 </p>
 
## Future works

- Sparse representation of structure from motion lacks definitive quantitative metrics for model comparison and requires images to be passed in a specific order with sufficient overlap.
- Altering the image order may break the model, making it less flexible and adaptable to different situations.
- Despite sparse representations importance, dense image reconstruction is necessary for practical usage, achievable through the Multi-View Stereo (MVS) algorithm.
- Explore the transformer based 2D encoder - 3D decoder kind of approaches to solve this problem.

## References
1. https://cmsc426.github.io/sfm/
2. https://www.cs.cmu.edu/~16385/s17/Slides/11.4_Triangulation.pdf
3. CVPR Lab at NUS (Youtube Channel)
