# PPM_Seminar

Machine Learning Applications in Process Mining (SE) 💡 - winter semester 2023

<img src="images/RWTH_Logo.png" width="500">

This repository is an adapted copy of [FOX](https://github.com/vinspdb/FOX). This repository incorporates code of an explainable AI approach for Predicitive Process Monitoring. In comparison to other approaches that use model agnostics, FOX uses an ad-hoc model to approach explainability. Its performance on benchmarks can be compared to those of simple machine learning approaches with similar level of explainability.

In the process of the above stated seminar, I performed some changes and additions to the code. If you have questions about the code feel free to contact me under my mail: lukas.jaeschke@rwth-aachen.de.

## Content of the repository and description:

The code of the repository is not hidden in another folder. Every python-file that you need for training and testing the model is directly visible in the repository.

In anfis_Mandami.py, membership.py and experimental.py you can find the code that determines the structur, the individual layers and the training method of the model. In train_anfis.py you will find the combination of all methods. This file performs the training of the models in correspondence to a specific dataset. In load_model.py you will find the test and evaluation functions of the model. Moreover, I added another python file called further_analysis that incorporates my approach to further evaluate the quality and performance of the model. 

To train the model, I recommend you to use the datasets that were taken as benchmarks in the approach of FOX. You can download the needed csv-files in this link [https://drive.google.com/drive/folders/1k4Ylxm0Ee1AisCvy52M9zbrLMS4zrL-g?usp=sharing]

Furthermore I added two folders. The params folder incorporates the best hyperparameters of the model with respect to the specific datasets. The results folder includes the csv-files of the performance and further analysis files that I created during my assessment.

## Libraries for the code:
<ul>
    <li>python --version 3.6</li>
    <li>(py)torch --version 1.8.1</li>
    <li>tqdm --version (current_one)</li>
    <li>(json)pickle --version (current_one)</li>
</ul>
