 # neural-portrait
CS 231N project
---------------
Priscilla Lui and Natalie Cygan
CS 231N Spring 2019

### Dependencies

Gatys and Gatys+:
Our style transfer is developed on top of anishathalye's neural style transfer implementation (https://github.com/anishathalye/neural-style). To run Gatys, follow the same installation and run instructions as thiers. We do have addtional style parameters that can be modified inside neural_style.py. Specifically, multiply the default style weight by 20 to do Gatys+.

Foreground mask:
To operate our masked neural style implementation, you also must specify a foreground mask inside neural_style.py. This mask can be created with the crfasrnn image segemenation implementation in keras (https://github.com/sadeepj/crfasrnn_keras). Using this program, create a binary mask from the outputed segmented image and you're good to go.

Naive algorithm:
Finish the step above for creating the foreground masks. Finish the first step to run Gatys, then run Gatys+. Run naive_image_formation.ipynb until all the final naive image compositions are saved.

Final algorithm:
Finish the step above for creating the foreground masks. For creating the facial feature mask, please see https://github.com/1adrianb/face-alignment to install the face-alignment library. Run the cells in segment_test.ipynb until all face masks are saved. Run facial_features_test.ipynb to apply the face masks until the final pastiches are saved.




