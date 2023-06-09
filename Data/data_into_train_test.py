# -*- coding: utf-8 -*-
import json
import pandas as pd
from pprint import pprint

df = pd.read_excel('/Users/skylerchak/Work/UM/Final_Program/data/人物关系表_N1500.xlsx')
relations = list(df['rel'].unique())
# relations.remove('unknown')
relation_dict = {}
relation_dict.update(dict(zip(relations, range(0, len(relations)))))

with open('/Users/skylerchak/Work/UM/Final_Program/data/rel_dict.json', 'w', encoding='utf-8') as h:
    h.write(json.dumps(relation_dict, ensure_ascii=False, indent=2))

print('Amount: %s' % len(df))
pprint(df['rel'].value_counts())
df['rel'] = df['rel'].apply(lambda x: relation_dict[x])

texts = []
for per1, per2, text in zip(df['人物1'].tolist(), df['人物2'].tolist(), df['文本'].tolist()):
    text = '$'.join([per1, per2, text.replace(per1, len(per1)*'#').replace(per2, len(per2)*'#')])
    texts.append(text)

df['text'] = texts


train_df = df.sample(frac=0.8, random_state=1024)
test_df = df.drop(train_df.index)

with open('/Users/skylerchak/Work/UM/Final_Program/Code/people_relation_extract/data/train.txt', 'w', encoding='utf-8') as f:
    for text, rel in zip(train_df['text'].tolist(), train_df['rel'].tolist()):
        f.write(str(rel)+' '+text+'\n')

with open('/Users/skylerchak/Work/UM/Final_Program/Code/people_relation_extract/data/test.txt', 'w', encoding='utf-8') as g:
    for text, rel in zip(test_df['text'].tolist(), test_df['rel'].tolist()):
        g.write(str(rel)+' '+text+'\n')




