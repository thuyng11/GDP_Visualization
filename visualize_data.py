'''
Data Visualization Module
'''
import matplotlib.pyplot as plt

def get_data(data):
    '''
    Extracts the data from a given dictionary and returns it in
    an array format

    :param data: a list of dictionary
    '''
    date_list = []
    value_list = []
    for item in data[:11]:
        date_list.insert(0, item['date'])
        value_list.insert(0, item['value'])

    return [date_list, value_list]


def plot_data(data):
    '''
    Generate line graph from given data

    :param data: a list of date and value
    '''
    assert isinstance(data, list)
    x = data[0]  # Time
    y = data[1]  # Values
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(10, 5))  # Setting figure size
    fig.autofmt_xdate()
    ax.plot(x, y)  # Create a line chart
    ax.set_xlabel('Date')  # Add a label to X axis
    ax.set_ylabel('Value (in billion dollars)')  # Add a label to  Y axis
    plt.title('Annual Real Gross Domestic Product')  # Add a title
    # Save plot to a figure in a file
    plt.savefig('WorkoutProject4-thuyn18', dpi=300, bbox_inches='tight')
