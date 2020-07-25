import pandas as pd


def get_gdp_data():
    """
    GDP data
    :return:
    """
    gdp_dict = {'Country': ['United States', 'China', 'Japan', 'Germany', 'India'],
                'GDP': ['$21.44 trillion', '$14.14 trillion', '$5.15 trillion', '$3.86 trillion', '$2.94 trillion']}
    data = pd.DataFrame(gdp_dict)
    return data
