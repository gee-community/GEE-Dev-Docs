# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 08:59:56 2019

@author: braatenj
"""



import os

outFile = r'C:\Users\braatenj\Documents\GitHub\GEE-Dev-Docs\docs\API\date-ranges-home.md'
lookHere = r'C:\Users\braatenj\Documents\GitHub\example-scripts\DateRanges'

info = [
    {'title':'Creating DateRanges','pages':[
        'ee.DateRange.md',
        'ee.DateRange.unbounded.md',
    ]},
    {'title':'Transforming DateRanges','pages':[
        'dateRange.union.md',
        'dateRange.intersection.md',
    ]},
    {'title':'Querying DateRanges','pages':[
        'dateRange.start.md',
        'dateRange.end.md',
    ]},    
    {'title':'Describing DateRanges','pages':[
        'dateRange.intersects.md',
        'dateRange.contains.md',
        'dateRange.isEmpty.md',
        'dateRange.isUnbounded.md'
    ]}   
]


divider = ['\n\n<!------------------------------------------------------------------------------------------------------------------------------>\n',
               '<!---replace---------------------------------------------------------------------------------------------->\n',
               '<!------------------------------------------------------------------------------------------------------------------------------>\n\n\n']
divider = ''.join(divider)


with open(outFile, 'w') as outfile:
  for i in range(len(info)):
    newSection = 1
    for j in range(len(info[i]['pages'])):
      if newSection == 1:
        addThis = divider.replace('replace', info[i]['title'])+'## '+info[i]['title']+'\n\n\n'
      else:
        addThis = '\n\n<!------------------------------------------------------------------------------------------------------------------------------>\n\n\n'
      
      with open(os.path.join(lookHere,info[i]['pages'][j])) as infile:
        out = infile.read()
        out = addThis+out
        out = out.replace('## Syntax', '**Syntax**')
        out = out.replace('## Example', '**Example**')
        out = out.replace('#### Javascript', '*Javascript*')
        out = out.replace('\n# ', '\n### ')
        outfile.write(out)
        
      newSection = 0