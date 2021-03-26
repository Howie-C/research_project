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
    icd_code_list = []
    icd_version_list = []
    admittime_list = []
    dischtime_list = []
    deathtime_list = []
    admission_type_list = []
    ethnicity_list = []
    marital_status_list = []
    hospital_expire_flag_list = []

    '''
    Locate other info in Patients table
    '''
    for subject_id in sample_subject_list:
        #print(subject_id)

        # Find gender in patients.csv, convert to string and make a list
        gender = patients_df[patients_df['subject_id'] == subject_id]['gender'].to_string(index = False).replace(' ', '')

        gender_list.append(gender)

    print(gender_list)

    '''
    Locate other info in Diagnoses_icd table
    '''
    for (subject_id, hadm_id) in zip(sample_subject_list, sample_hadm_list):
        #print(subject_id, hadm_id)
        seq_num = diagnoses_df[(diagnoses_df['subject_id'] == subject_id) & (diagnoses_df['hadm_id'] == hadm_id)]['seq_num'].to_string(index = False).replace(' ', '').replace('\n', ' ')
        icd_code = diagnoses_df[(diagnoses_df['subject_id'] == subject_id) & (diagnoses_df['hadm_id'] == hadm_id)]['icd_code'].to_string(index = False).replace(' ', '')
        icd_version = diagnoses_df[(diagnoses_df['subject_id'] == subject_id) & (diagnoses_df['hadm_id'] == hadm_id)]['icd_version'].to_string(index = False).replace(' ', '')

        seq_num_list.append(seq_num)
        icd_code_list.append(icd_code)
        icd_version_list.append(icd_version)

    print(seq_num_list)
    print(icd_code_list)
    print(icd_version_list)

    '''
    Locate other info in Admissions table
    '''
    for (subject_id, hadm_id) in zip(sample_subject_list, sample_hadm_list):
        #print(subject_id, hadm_id)
        admittime = admissions_df[(admissions_df['subject_id'] == subject_id) & (admissions_df['hadm_id'] == hadm_id)]['admittime'].to_string(index = False)
        dischtime = admissions_df[(admissions_df['subject_id'] == subject_id) & (admissions_df['hadm_id'] == hadm_id)]['dischtime'].to_string(index = False)
        #deathtime = diagnoses_df[(admissions_df['subject_id'] == subject_id) & (admissions_df['hadm_id'] == hadm_id)]['deathtime'].to_string(index = False)
        admission_type = admissions_df[(admissions_df['subject_id'] == subject_id) & (admissions_df['hadm_id'] == hadm_id)]['admission_type'].to_string(index = False).replace(' ', '')
        ethnicity = admissions_df[(admissions_df['subject_id'] == subject_id) & (admissions_df['hadm_id'] == hadm_id)]['ethnicity'].to_string(index = False).replace(' ', '')
        marital_status = admissions_df[(admissions_df['subject_id'] == subject_id) & (admissions_df['hadm_id'] == hadm_id)]['marital_status'].to_string(index = False).replace(' ', '')
        hospital_expire_flag = admissions_df[(admissions_df['subject_id'] == subject_id) & (admissions_df['hadm_id'] == hadm_id)]['hospital_expire_flag'].to_string(index = False).replace(' ', '')

        admittime_list.append(admittime)
        dischtime_list.append(dischtime)
        #deathtime_list.append(deathtime)
        admission_type_list.append(admission_type)
        ethnicity_list.append(ethnicity)
        marital_status_list.append(marital_status)
        hospital_expire_flag_list.append(hospital_expire_flag)

    print(admittime_list)
    print(dischtime_list)
    #print(deathtime_list)
    print(admission_type_list)
    print(ethnicity_list)
    print(marital_status_list)
    print(hospital_expire_flag_list)

    # Create new dataframe
    main_df = pd.DataFrame()
    each_patient_num_list = []
    each_seq_num_list = []


    for each_patient in range(len(seq_num_list)):
        #print(seq_num_list[each])
        each_seq_num = seq_num_list[each_patient].split(' ')
        each_seq_num_list.append(each_seq_num)

        each_patient_num = len(each_seq_num_list)
        each_patient_num_list.append(each_patient_num)

    print(each_patient_num_list)

    total_patient_list = [sample_subject_list * i for i in each_patient_num_list]
    print(total_patient_list)




    main_df.to_csv('main.csv')

def task():

    data_pre_processing()




if __name__ == '__main__':
    task()