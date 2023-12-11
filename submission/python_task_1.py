import pandas as pds


def generate_car_matrix()
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    def generate_car_matrix():
    df=pds.read_csv("dataset-1.csv")
  
    generated_matrix = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)
    generated_matrix.values[[range(len(generated_matrix))]*2] = 0

    return generated_matrix

result = generate_car_matrix()
print(result)
  




def get_type_count()
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    df=pds.read_csv("dataset-1.csv")
    bins = [-float('inf'), 15, 25, float('inf')]
    categories = ['low', 'medium', 'high']
    
    df['car_type'] = pds.cut(df['car'], bins=bins, labels=categories, right=False, include_lowest=True)
    
    occurance_counts = df['car_type'].value_counts().to_dict()
    
    dict= sorted(occurance_counts.items())

    return    dict
result = get_type_count()
print(result)



def get_bus_indexes(df):
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
  
      
    df=pd.read_csv("dataset-1.csv")

    mean_value = df['bus'].mean()
    list = df[df['bus'] > 2 * mean_value].index.tolist()
    list.sort()

    return list



list = get_bus_indexes()
print(list)

   


def filter_routes()
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    df=pd.read_csv("dataset-1.csv")
   
    route_avg_truck = df.groupby('route')['truck'].mean()
    list = route_avg_truck[route_avg_truck > 7].index.tolist()
    list.sort()

    return list
result=filter_routes()
print(result)


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
