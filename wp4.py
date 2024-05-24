'''
This module contains main function and main block that serve as
'''
from visualize_data import get_data, plot_data
from alpha_vantage import fetch_GDP_data


def main():
    '''
    Main module for generating graph from extracted data
    about real GDP of the US
    '''
    api_key = "WU1623RP57Z11QC6"
    data = fetch_GDP_data(api_key)
    list_xy = get_data(data)
    plot_data(list_xy)


if __name__ == "__main__":
    main()
