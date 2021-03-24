import pandas as pd


# initiation
patients_df = pd.read_csv('patients.csv')

admissions_df = pd.read_csv('admissions.csv')

diagnoses_df = pd.read_csv('diagnoses_icd.csv')

print('Loading dataframes...\n')
print("{} rows of data are included in 'patients.csv'.".format(len(patients_df.index)))
print("{} rows of data are included in 'admissions.csv'.".format(len(admissions_df.index)))
print("{} rows of data are included in 'disgnoses_icd.csv'.".format(len(diagnoses_df.index)))


def data_pre_processing():

    print('\nData pre-processing...\n')

    # Take sample data size of 100, on admission.csv table.

    sample_df = admissions_df.head(3)
    #print(sample_df)

    # Make subject_id to list
    sample_subject_list = sample_df['subject_id'].tolist()
    sample_hadm_list = sample_df['hadm_id'].tolist()

    # Make empty lists of other info
    gender_list = []
    seq_num_list = []

    '''
    Locate other info in Patients table
    '''
    for subject_id in sample_subject_list:
        #print(subject_id)

        # Find gender in patients.csv, convert to string and make a list
        gender = patients_df[patients_df['subject_id'] == subject_id]['gender'].to_string(index = False)

        gender_list.append(gender)

    print(gender_list)

    '''
    Locate other info in Patients table
    '''
    for (subject_id, hadm_id) in zip(sample_subject_list, sample_hadm_list):
        #print(subject_id, hadm_id)
        seq_num = diagnoses_df[(diagnoses_df['subject_id'] == subject_id) & (diagnoses_df['hadm_id'] == hadm_id)]['seq_num'].to_string(index = False)

        seq_num_list.append(seq_num)

    print(seq_num_list)


def task():

    data_pre_processing()




if __name__ == '__main__':
    task()