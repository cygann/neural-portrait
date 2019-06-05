 # neural-portrait
CS 231N project
---------------
Priscilla Lui and Natalie Cygan
CS 231N Spring 2019

### Dependencies
Our style transfer is developed on top of anishathalye's neural style transfer implementation (https://github.com/anishathalye/neural-style). To run ours, follow the same installation and run instructions as thiers. We do have addtional style parameters that can be modified inside neural_style.py.

To operate our masked neural style implementation, you also must specify a mask inside neural_style.py. This mask can be created with the crfasrnn image segemenation implementation in keras (https://github.com/sadeepj/crfasrnn_keras). Using this program, create a binary mask from the outputed segmented image and you're good to go.

For facial enhancement, please see https://github.com/1adrianb/face-alignment to install the face-alignment library. 
