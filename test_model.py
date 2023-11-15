import torch
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from torch.autograd import Variable
plt.rcParams['figure.figsize'] = (20, 8)




def histplot_model_certainty(dataset_name, columns_sel):
    # create model from train_anfis.py
    model = torch.load('models_lj/model_' + dataset_name + '.h5')

    # read in data from the test-set and separate into features and classification
    df_test = pd.read_csv("dataset/" + dataset_name + "/" + dataset_name + '_test.csv', header=0, sep=',')
    df_features = df_test[columns_sel]
    df_targets = df_test[['Classification']]

    # create torch array from features
    conv_test = torch.tensor(df_features.values, dtype=torch.float)

    # predict outcome of each feature vector and split into prediction and certainty
    pred = model(torch.Tensor(conv_test))
    pred = torch.max(pred, 1)

    df_targets['model_classification'] = pred.indices.detach().numpy()
    df_targets['model_certainty'] = pred.values.detach().numpy()

    # check if classification of model is similar to the true classification of the feature vector
    false_class_df = df_features.loc[df_targets['Classification'] != df_targets['model_classification']]
    false_class_df['model_certainty'] = df_targets['model_certainty'].iloc[false_class_df.index]

    # create histogram for analysis purposes
    histplot_binning = np.linspace(0, df_targets['model_certainty'].max(), 50)

    fig, axs = plt.subplots(1,1)
    sn.histplot(data=df_targets, x='model_certainty', bins=histplot_binning, color='b', label='all')
    sn.histplot(data=false_class_df, x='model_certainty', bins=histplot_binning, color='r', label='false')
    axs.set_title('Model certainty comparison of all and false classifications of the test-set', fontsize=20)
    axs.legend(fontsize=15)
    axs.set_xlabel('model_certainty', fontsize=15)
    axs.set_ylabel('Count', fontsize=15)
    axs.tick_params(labelsize=12)
    #plt.savefig('results/images_further-analysis/'+dataset_name+'_hist-certainty.png')
    plt.show()



dataset_name = 'production'

if dataset_name == 'sepsis_cases_1':
        columns_sel = ['Diagnose', 'mean_open_cases', 'Age', 'std_Leucocytes', 'std_CRP']#sepsis_cases_1
elif dataset_name == 'sepsis_cases_2':
        columns_sel = ['Diagnose', 'mean_open_cases', 'mean_hour', 'DisfuncOrg']#sepsis_cases_2
elif dataset_name == 'sepsis_cases_4':
        columns_sel = ['Diagnose', 'mean_open_cases', 'Age', 'org:group_E', 'std_CRP', 'DiagnosticECG']#sepsis_cases_4
elif dataset_name == 'bpic2011_f1':
        columns_sel = ['Diagnosis Treatment Combination ID', 'mean_open_cases', 'Diagnosis', 'Activity code_376400.0']#bpic2011_f1
elif dataset_name == 'bpic2011_f2':
        columns_sel = ['Diagnosis Treatment Combination ID', 'Diagnosis', 'Diagnosis code', 'mean_open_cases', 'Activity code_376400.0', 'Age', 'Producer code_CHE1']#bpic2011_f2
elif dataset_name == 'bpic2011_f3':
        columns_sel = ['Diagnosis Treatment Combination ID', 'Diagnosis', 'mean_open_cases', 'Diagnosis code', 'std_event_nr', 'mean_event_nr']#bpic2011_f3
elif dataset_name == 'bpic2011_f4':
        columns_sel = ['Diagnosis Treatment Combination ID', 'Treatment code']#bpic2011_f4
elif dataset_name == 'bpic2012_accepted':
        columns_sel = ['AMOUNT_REQ', 'Activity_O_SENT_BACK-COMPLETE', 'Activity_W_Valideren aanvraag-SCHEDULE', 'Activity_W_Valideren aanvraag-START']#bpic2012_accepted
elif dataset_name == 'bpic2012_declined':
        columns_sel = ['AMOUNT_REQ', 'Activity_A_PARTLYSUBMITTED-COMPLETE', 'Activity_A_PREACCEPTED-COMPLETE', 'Activity_A_DECLINED-COMPLETE', 'Activity_W_Completeren aanvraag-SCHEDULE', 'mean_open_cases'] #bpic2012_declined
elif dataset_name == 'bpic2012_cancelled':
        columns_sel = ['Activity_O_SENT_BACK-COMPLETE', 'Activity_W_Valideren aanvraag-SCHEDULE', 'Activity_W_Valideren aanvraag-START', 'AMOUNT_REQ', 'Activity_W_Valideren aanvraag-COMPLETE', 'Activity_A_CANCELLED-COMPLETE']#bpic2012_cancelled
elif dataset_name == 'production':
        columns_sel = ['Work_Order_Qty', 'Activity_Turning & Milling - Machine 4', 'Resource_ID0998', 'Resource_ID4794', 'Resource.1_Machine 4 - Turning & Milling']#production


histplot_model_certainty(dataset_name, columns_sel)