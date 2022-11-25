import pandas as pd

class FundingRaised:
  """
  Returns company's information
  """
  global df
  df = pd.read_csv('startup_funding.csv')
  
  @staticmethod
  def where(options = {}):
    """
    Filters the dataframe based on the parameters provided, and returns the filtered dataframe
    """
    result = df
    for key in options.keys():
      result = result.loc[result[key] == options.get(key)]

    return result
    

  @staticmethod
  def find_by(options):
    """
    This function returs the first instance that is found based on the parameter sent
    """
    for key in options.keys():
      result = df.loc[df[key] == options.get(key)].head(1)
    return result

if __name__ == "__main__":
    
    print(FundingRaised.where({'company_name': 'Facebook'}))
    print("___________________________________________________")
    print(FundingRaised.find_by({'company_name': 'Facebook'}))
    