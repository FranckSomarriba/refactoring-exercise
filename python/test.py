from funding_raised import FundingRaised
import os

def test_where_returns_events():
  assert len(FundingRaised.where({'company_name': 'Facebook'})) == 7

def test_where_returns_correct_keys():
  row = FundingRaised.where({'company_name': 'Facebook'}).head(1)
  keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
  values = ['facebook', 'Facebook', '450.0', 'web', 'Palo Alto', 'CA', '1-Sep-04', '500000', 'USD', 'angel']
  for i in range(0, len(keys)):
    assert str(row[keys[i]].values[0]) == values[i]

def test_where_returns_events_by_city():
  assert len(FundingRaised.where({'city': 'Tempe'})) == 3

def test_where_returns_events_by_state():
  assert len(FundingRaised.where({'state': 'CA'})) == 873

def test_where_returns_events_by_company():
  assert len(FundingRaised.where({'company_name': 'Facebook', 'round': 'a'})) == 1

def test_where_returns_events_by_type():
  assert len(FundingRaised.where({'round': 'a'})) == 582

def test_where_returns_no_events():
  assert len(FundingRaised.where({'company_name': 'NotFacebook'})) == 0

def test_find_by_event_by_company_name():
  row = FundingRaised.find_by({'company_name': 'Facebook'})
  keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
  values = ['facebook', 'Facebook', '450.0', 'web', 'Palo Alto', 'CA', '1-Sep-04', '500000', 'USD', 'angel']
  for i in range(0, len(keys)):
    assert str(row[keys[i]].values[0]) == values[i]

def test_find_by_event_by_state():
  row = FundingRaised.find_by({'state': 'CA'})
  keys = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']
  values = ['digg', 'Digg', '60.0', 'web', 'San Francisco', 'CA', '1-Dec-06', '8500000', 'USD', 'b']
  for i in range(0, len(keys)):
    assert str(row[keys[i]].values[0]) == values[i]

test_where_returns_events()
test_where_returns_correct_keys()
test_where_returns_events_by_city()
test_where_returns_events_by_state()
test_where_returns_events_by_company()
test_where_returns_events_by_type()
test_where_returns_no_events()
test_find_by_event_by_company_name()
test_find_by_event_by_state()
