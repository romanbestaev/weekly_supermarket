import os


class ExtractData:
    def __init__(self, purchase_data_dir=None):
        self.purchase_data_dir = purchase_data_dir or os.getcwd()
        self.purchase_files_list = []


    def get_file_names_from_dir(self):
        self.purchase_files_list = [f for f in os.listdir(self.purchase_data_dir) if
                                    os.path.isfile(os.path.join(self.purchase_data_dir, f))]
        # print (self.purchase_data_dir)
        # self.purchase_files_list = os.listdir(self.purchase_data_dir)
        # return


# Пример использования
extractor = ExtractData()
extractor.get_file_names_from_dir()
print(extractor.purchase_files_list)