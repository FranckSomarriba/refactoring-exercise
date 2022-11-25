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
    list_keys = options.keys()
    result = df
    for key in list_keys:
      result = result.loc[result[key] == options.get(key)]

    return result
    

#   @staticmethod
#   def find_by(options):
#     with open("../startup_funding.csv", "rt") as csvfile:
#       data = csv.reader(csvfile, delimiter=',', quotechar='"')
#       # skip header
#       next(data)
#       csv_data = []
#       for row in data:
#         csv_data.append(row)

#     if 'company_name' in options:
#       for row in csv_data:
#         if row[1] == options['company_name']:
#           mapped = {}
#           mapped['permalink'] = row[0]
#           mapped['company_name'] = row[1]
#           mapped['number_employees'] = row[2]
#           mapped['category'] = row[3]
#           mapped['city'] = row[4]
#           mapped['state'] = row[5]
#           mapped['funded_date'] = row[6]
#           mapped['raised_amount'] = row[7]
#           mapped['raised_currency'] = row[8]
#           mapped['round'] = row[9]
#           return mapped

#     if 'city' in options:
#       for row in csv_data:
#         if row[4] == options['city']:
#           mapped = {}
#           mapped['permalink'] = row[0]
#           mapped['company_name'] = row[1]
#           mapped['number_employees'] = row[2]
#           mapped['category'] = row[3]
#           mapped['city'] = row[4]
#           mapped['state'] = row[5]
#           mapped['funded_date'] = row[6]
#           mapped['raised_amount'] = row[7]
#           mapped['raised_currency'] = row[8]
#           mapped['round'] = row[9]
#           return mapped

#     if 'state' in options:
#       for row in csv_data:
#         if row[5] == options['state']:
#           mapped = {}
#           mapped['permalink'] = row[0]
#           mapped['company_name'] = row[1]
#           mapped['number_employees'] = row[2]
#           mapped['category'] = row[3]
#           mapped['city'] = row[4]
#           mapped['state'] = row[5]
#           mapped['funded_date'] = row[6]
#           mapped['raised_amount'] = row[7]
#           mapped['raised_currency'] = row[8]
#           mapped['round'] = row[9]
#           return mapped

#     if 'round' in options:
#       for row in csv_data:
#         if row[9] == options['round']:
#           mapped = {}
#           mapped['permalink'] = row[0]
#           mapped['company_name'] = row[1]
#           mapped['number_employees'] = row[2]
#           mapped['category'] = row[3]
#           mapped['city'] = row[4]
#           mapped['state'] = row[5]
#           mapped['funded_date'] = row[6]
#           mapped['raised_amount'] = row[7]
#           mapped['raised_currency'] = row[8]
#           mapped['round'] = row[9]
#           return mapped

#     raise RecordNotFound

# class RecordNotFound(Exception):
#   pass

if __name__ == "__main__":
    
    print(FundingRaised.where({'company_name': 'Facebook'}))
    # print("___________________________________________________")
    # print(FundingRaised.find_by({'company_name': 'Facebook'}))
    