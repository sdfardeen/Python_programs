import xlrd
import json
import pandas as pd



def xls_file_reader(file_path, sheet_name):
    """
    Library to read the test data from xlsheet
    and
    :param file_path:
    :param sheet_name:
    :return: {"tcid": {"userid":"value", "password":"value"}, "tcid1": {"userid":"value", "password":"value"}}
    """
    xl_sheet_data = xlrd.open_workbook(file_path)
    xl_test_data = xl_sheet_data.sheet_by_name(sheet_name)
    test_data = dict()
    tc_id, use_name_header, pas_header = xl_test_data.cell_value(0, 0), xl_test_data.cell_value(0, 1), xl_test_data.cell_value(0, 2)

    for j in range(1, xl_test_data.nrows):
        if xl_test_data.cell_value(j, 0):
            test_data[xl_test_data.cell_value(j, 0)] = {
                use_name_header: xl_test_data.cell_value(j, 1),
                pas_header: xl_test_data.cell_value(j, 2)
            }
    print(json.dumps(test_data))
    return test_data


def read_xls_pandas(file_path, sheetname="", coulmns_data=list()):
    # ['Audit Test Cases', 'Data Required', 'Data Received by Parrot (Yes/No)']
    df = pd.read_excel(file_path, sheetname, index_col=0)
    df = pd.DataFrame(df, columns=coulmns_data)
    df = df.fillna(0)
    res = dict()
    if len(coulmns_data) <= 1:
        return res
    for i, j in df.iterrows():
        if j[coulmns_data[1]]:
            temp_dict = dict()
            for m in coulmns_data[1:]:
                temp_dict[m] = j[m]
            res[i] = temp_dict

    print(json.dumps(res))
    return json.dumps(res)

