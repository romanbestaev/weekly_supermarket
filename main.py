from supermarket import ExtractData
#
# extract_data = supermarket.ExtractData()
# purchase_files = extract_data.get_file_names_from_dir()



# Пример использования
extractor = ExtractData()
extractor.get_file_names_from_dir()
print(extractor.purchase_files_list)
