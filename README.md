# PPM_Seminar

## How I understood the code provided by the repository of the research team:

The repository is constructed with 5 python-files:
<ul>
	<li> <i>anfis_Mandami.py</i> </li>
    <ul>
        <li>determines the structure and the operations of the ANFIS architecture</li>
        <li>in general: ANFIS is constructed using 5 layers!</li> 
        <li><b>Fuzzify, Rules, Normalization, Consequence/PlainConsequence and WeightedSum</b></li>
    </ul>
    <li> <i>experimental.py</i> </li>
    <ul>
        <li>functions for training the ANFIS-NN. This includes One-hot representation (?), Multi-accuracy via softmax and the actual training method</li>
        <li>the training method is structured as follows: initialization, Loop around Epochs(Loop around training batch(optimize/backprop), compute loss and acc, determination of best epoch)</li>
    </ul>
    <li> <i>load_model.py</i> </li>
    <ul>
        <li>definition of metric method that tests datasets and determines their performance</li>
        <li>also includes visualizations</li>
    </ul>
    <li> <i>membership.py</i> </li>
    <ul>
        <li>these are possible membership-functions for the ANFIS architecture</li>
        <li>It is imported from the library of James Power</li>
        <li>For us, only GaussMembFunc is interesting
    </ul>
    <li> <i>train_anfis.py</i> </li>
    <ul>
        <li>combination of all files</li>
        <li>could be understood as 'main.py'</li>
    </ul>
</ul>
and 4 folders:
<ul>
	<li> <i>dataset</i> </li>
    <ul>
        <li>premature dataset since it only includes sepsis_cases_1 as train, test and id_len (interesting for prefix traces) files.</li>
        <li>Files are in .csv-format</li>
    </ul>
    <li> <i>models</i> </li>
    <ul>
        <li>This folder includes .h5-files that are named according to datasets. It seems that these files specify the trained model.</li>
        <li>However, since the training of the NNs are part of the reconstruction, I should delete those files or create new ones.</li>
	<li>Here, I created a new folder called: <i>models_lj</i>. </li>
    </ul>
    <li> <i>params</i> </li>
    <ul>
        <li>This folder includes .p-files that are named according to datasets. It seems that these files specify the optimal hyperparameters of the datasets.</li>
        <li>I might change these hyperparameters for my upcoming analysis</li>
    </ul>
    <li> <i>streamlit_fox</i> </li>
    <ul>
        <li>This folder seems to be a premature copy of the original file</li>
        <li>Given the name of the folder, it seems that this folder is meant to simplify the application in streamline.</li>
        <li><b>deleted!</b></li> 
    </ul>
</ul>

## Libraries that I need:
<ul>
    <li>python --version 3.6</li>
    <li>(py)torch --version 1.8.1</li>
    <li>tqdm --version (current_one)</li>
    <li>(json)pickle --version (current_one)</li>
</ul>

## Changes I did:

<ul>
    <li>changed some file-creation methods to other directories.</li>
    <li>changed the training computation efforts to 'cpu'</li>	    
</ul>
