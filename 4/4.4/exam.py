import csv
import json
from datetime import *
def order(dic):
    new_dic = {}
    new_dic['name']=dic['name']
    new_dic['surname']=dic['surname']
    new_dic['best_score']=int(dic['best_score'])
    new_dic['date_and_time']=dic['date_and_time']
    new_dic['email']=dic['email']
    return new_dic
with open('C:/VS code pets/edu/pygen_prof/4/4.4/exam_results.csv', 'r', encoding='UTF-8') as exam_results:
    new_res=[]
    emails_list=[]
    res = csv.DictReader(exam_results)
    sorted_res = sorted(res, key=lambda x: (x['email'], int(x['score']), datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S')), reverse=True)
    for row in sorted_res:
        if row['email'] not in emails_list:
            emails_list.append(row['email'])
            row['best_score']=row['score']
            del row['score']
            new_row = order(row) 
            new_res.append(new_row)
    new_sorted = sorted(new_res, key=lambda x: x['email'])


    with open('C:/VS code pets/edu/pygen_prof/4/4.4/best_scores.json', 'w', encoding='utf-8', newline='') as best_json:
        json.dump(new_sorted, best_json, indent=3, ensure_ascii=False)