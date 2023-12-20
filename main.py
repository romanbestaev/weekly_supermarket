from supermarket import ExtractData
#
# extract_data = supermarket.ExtractData()
# purchase_files = extract_data.get_file_names_from_dir()

PATH_TO_INIT_DATA = r'D:\workshop\Python\weekly_supermarket\purchase_data'

# Пример использования
extractor = ExtractData(PATH_TO_INIT_DATA)
extractor.get_file_names_from_dir()
extractor.get_products_set()
df = extractor.get_dataframe_product_url()
print(extractor.purchase_files_list)
print(extractor.products_set)
