"""
script to demo functions with keyword arguments
"""
def company_info(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

company_info(ticker = "APPL", company_name = "APPLE INC", pe_ratio = "3.0")