# NeuralNetworkDataPrep
Prepares data for neural network analysis using the NeuroMat software, which is a collection of scripts written by Thomas Sourmail and Sree Harsha, based on the Bayesian optimization algorithm written by David McKay.

All data used in this repository was obtained from Glyn Evans.

This repository contains code to:

1. Fit a tanh curve to real data (Charpy toughness data) and based on that determine the inflection point (aka transition point in materials science) and the upper shelf start point (USSP) of the curve. 
2. Automatically create profiles for predictions based on a reference file (otherwise manual for NeuroMat).
3. Condense the predictions of several neural network models into a single multi-index DataFrame.
4. Plot the predictions of different models, but the same compositional profiles onto the same plot.
5. Find the significance values for each submodel of the committee used to predict the results and condense them into a single multi-index DataFrame.
6. Plot the average significances of each input variable for every specified model.

For more detailed information, visit the GitHub Pages for this repository:

https://ennuk3.github.io/NeuralNetworkDataPrep/
