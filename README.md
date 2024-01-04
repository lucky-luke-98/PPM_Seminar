# PPM_Seminar

Machine Learning Applications in Process Mining (SE) 💡 - winter semester 2023

<img src="images/RWTH_Logo.png" width="500">

This repository is an adapted copy of [FOX](https://github.com/vinspdb/FOX). This repository incorporates code of an explainable AI approach for Predictive Process Monitoring. In comparison to other approaches that use model agnostics, FOX uses an ad-hoc model to approach explainability. Its performance on benchmark datasets can be compared to those of other machine learning approaches with similar levels of explainability.

In the process of the above-stated seminar, I performed some changes and additions to the code. If you have questions about the code feel free to contact me under my mail: lukas.jaeschke@rwth-aachen.de.

![Python Version](https://img.shields.io/badge/Python-3.6%2B-brightgreen)

## Content of the repository and description:

Every Python file that you need for training and testing the model is directly visible in the repository.

In anfis_Mandami.py, membership.py, and experimental.py you can find the code that determines the structure, the individual layers, and the training method of the model. In train_anfis.py you will find the combination of all methods. This file performs the training of the models in correspondence to a specific dataset. In load_model.py you will find the test and evaluation functions of the model. Moreover, I added another Python file called further_analysis that incorporates my approach to further evaluate the quality and performance of the model. 

To train the model, I recommend you to use the datasets that were taken as benchmarks in the approach of FOX. You can download the needed csv-files at this link https://drive.google.com/drive/folders/1k4Ylxm0Ee1AisCvy52M9zbrLMS4zrL-g?usp=sharing

Furthermore, I included four folders. The [params](params/) folder incorporates the best hyperparameters of the model with respect to the specific benchmark datasets. The [results](results/) folder includes the csv-files of the performance and further analysis files that I created during my assessment. [Literature](Literature/) includes descriptions of my approach.

## Libraries for the code:
<ul>
    <li>python --version 3.6</li>
    <li>(py)torch --version 1.8.1</li>
    <li>tqdm --version (current_one)</li>
    <li>(json)pickle --version (current_one)</li>
</ul>

## How to install the repository in your workspace:
```bash
git clone https://github.com/lucky-luke-98/PPM_Seminar
```

## How to contribute to this project:
Thank you for your interest in contributing to this project! I welcome all kinds of contributions, no matter how small or big they are. Whether it's adding new features, fixing bugs, improving documentation, or suggesting new ideas.
In this regard, please follow our [Code of Conduct](Literature/CONTRIBUTION.md)
