# GResNet
Source code of GResNet

Some reminders:

1. Do an early stop. 

When running the code, the score reported at the end of the experiment will be the one achieved at the 1000th/500th epoch, which can be lower than the scores reported in the paper. We choose the best scores in running the code with different epochs. Please do an early stop when necessary, and choose a better epoch number, which will help you get better scores.

2. Change a random seed.

Change a random seed will help change another parameter initialization, which can also help you get higher scores for some of the models.
