import re
import sys
import csv
maxInt = sys.maxsize
import json
while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

with open('code_comments_URL.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
            name= re.sub('[\W_ ]+', ' ', row[1]).replace('ipynb','')
            text= re.sub('[\W_ ]+', ' ', row[6])
            title= re.sub('[\W_ ]+', ' ', row[7])
            comments= re.sub('[\W_ ]+', ' ', row[8])
            url=row[9]

            temp_data = {}
            temp_data["name"] = name
            temp_data["full_name"] = title
            temp_data["stargazers_count"] = 0
            temp_data["forks_count"] = 0
            temp_data["description"] = text + comments
            temp_data["id"] = row[0]
            temp_data["size"] = row[5]
            temp_data["language"] = row[2]
            temp_data["html_url"] = url
            temp_data["git_url"] = url
            filename= re.sub(r'[^A-Za-z0-9 ]+', '',name)+"_"+"_"+str( row[5])

            f = open("index_files/"+filename+".json", 'w+')
            f.write(json.dumps(temp_data))
            f.close()
            print(url)







