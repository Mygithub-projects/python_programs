'''
import re
ph1="91-9962512345"
ph2="919962512345"
result=re.search('r\d\d\s-\d{9}',ph1)
'''
m_lst=["The Holy Grail", "The Life of Brain", "The Meaning of Life"]
years=[1975, 1979, 1983]
result=(map(lambda a,b:(a,b),m_lst,years))
print(list(result))
