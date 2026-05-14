import os

FEATURES = ['Fp1', 'F3', 'C3', 'P3', 'F7', 'T3', 'T5', 'O1', 'Fz', 'Cz', 'Pz', 'Fp2', 'F4', 'C4', 'P4', 'F8', 'T4', 'T6', 'O2', 'EKG']

LL = ['Fp1', 'F7', 'T3', 'T5', 'O1']
LP = ['Fp1', 'F3', 'C3', 'P3', 'O1']
RP = ['Fp2', 'F4', 'C4', 'P4', 'O2']
RR = ['Fp2', 'F8', 'T4', 'T6', 'O2']
IMPT_ELECTRODES = ['Fp1', 'O1', 'Fp2', 'O2']


REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# Download HMS Data & store it in directory hms_data/ inside the repo root.
PATH_TO_FILES_TRAIN_EEG = f'{REPO_ROOT}/hms_data/train_eegs'
PATH_TO_FILES_TRAIN_SPECT = f'{REPO_ROOT}/hms_data/train_spectrograms'
PATH_TO_TRAIN_CSV = f'{REPO_ROOT}/hms_data/train.csv'
PATH_TO_MERGE_PARQUET = f'{REPO_ROOT}/hms_data/combined_parqs'
PATH_TO_PROCESSED_DATA = f'{REPO_ROOT}/processed_data'

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds