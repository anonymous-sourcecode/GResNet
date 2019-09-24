'''
Concrete ResultModule class for a specific experiment ResultModule output
'''

# Copyright (c) 2017 Jiawei Zhang <jwzhanggy@gmail.com>
# License: TBD

from result import result
import pickle


class ResultSaving(result):
    data = None
    fold_count = None
    result_destination_folder_path = None
    result_destination_file_name = None

    def load(self):
        f = open(self.result_destination_folder_path + self.result_destination_file_name, 'rb')
        result = pickle.load(f)
        f.close()
        return result

    def save(self):
        f = open(self.result_destination_folder_path + self.result_destination_file_name, 'wb')
        pickle.dump(self.data, f)
        f.close()