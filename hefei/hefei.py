import torch, os
from torch.utils.data import Dataset
import numpy as np


class ECDDataset(Dataset):
    def __init__(self, sig_dir, label_path, arrythmia_path):
        super(ECDDataset, self).__init__()

        with open(arrythmia_path, 'r', encoding='utf8') as f:
            arrythmia = [line.split()[0] for line in f.readlines()]
            # {'完全性左束支传导阻滞': 53, '融合波': 54}
            self.arrythmia_dict = dict(zip(arrythmia, range(len(arrythmia))))
            self.arrythmia = arrythmia

        with open(label_path, 'r', encoding='utf8') as f:
            label = [line.replace('\t\t', '\tNone\t').replace('\t\t', '\tNone\t').split() for line in f]
            # {'1221.txt': ['57', 'MALE', '窦性心律', '一度房室传导阻滞', 'QRS低电压', '临界ECG'],}
            self.label_file_dir = dict(zip([item[0] for item in label],
                                           [self.to_array(item[1:]) for item in label]))
        self.sig_dir = sig_dir
        self.sig_names = os.listdir(sig_dir)
        self.sig_names = list(filter(lambda x: x.split('.')[-1] == 'txt', self.sig_names))

    @property
    def label_info(self):
        return self.self.arrythmia_dict

    def to_array(self, data_list: list):
        # input like this: ['57', 'MALE', '窦性心律', '一度房室传导阻滞', 'QRS低电压', '临界ECG']
        #                  ['None', 'None', '窦性心律', 'QRS低电压', '临界ECG']
        result = np.zeros(len(self.arrythmia))
        if len(data_list) >= 2:
            for item in data_list[2:]:
                result[self.arrythmia_dict[item]] = 1
        else:
            data_list.append('None')  # in test set it can be "[None,]"
        age = float(data_list[0]) if data_list[0] != 'None' else -1  # age
        if data_list[1] == 'MALE':
            m_or_f = 0
        elif data_list[1] == 'FEMALE':
            m_or_f = 1
        else:
            m_or_f = 0.5

        return result, age, m_or_f

    def __getitem__(self, index):
        with open(os.path.join(self.sig_dir, self.sig_names[index]), 'r') as f:
            f.readline()
            sig_data = np.zeros([5000, 8])
            for i, line in enumerate(f):
                sig_data[i] = [float(i) for i in line.split()]

        y, age, m_or_f = self.label_file_dir[self.sig_names[index]]
        other_data = [age, m_or_f]

        return {'sig': sig_data, 'other': other_data, 'label': y}

    def __len__(self):
        return len(self.sig_names)


base_data_dir = './data/'
train_set = ECDDataset(os.path.join(base_data_dir, 'train'),
                       os.path.join(base_data_dir, 'hf_round1_label.txt'),
                       os.path.join(base_data_dir, 'hf_round1_arrythmia.txt'))

test_set = ECDDataset(os.path.join(base_data_dir, 'testA'),
                      os.path.join(base_data_dir, 'hf_round1_subA.txt'),
                      os.path.join(base_data_dir, 'hf_round1_arrythmia.txt'))
