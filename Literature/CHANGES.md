# Here I want to describe which changes I made to the code

<p> As mentioned in the README.md file, this repo is cloned from the creators of FOX. However, since I am only interested in reconstructing the results and training the models, I performed some changes to the code and the repo. </p>
<p> Thus, my repository only incorporates files and folders that are relevant for my task. </p>
### Changes:
<ul>
	<li> I deleted the streamlit folder since I am not interested in a nice GUI. </li>
	<li> I did not incorporate the models folder since I am training the models myself. If you are interested in training the models, run 'train_anfis.py' with specifying which dataset you want to take. </li>
	<li> I created a results folder which saves the performance of the models (in csv-format). Strangely, this was not part of the original repository. </li>
	<li> For training the model I changed the training computation efforts to 'cpu' instead of 'cuda'. </li>
	<li> I performed some additional minor changes to the code. </li>
	<li> I added another file called 'further_analysis.py'. This code incorporates my approach to further investigate the performance of the model. The analysis results are saved in the folder results/further_analysis </li>
</ul>
