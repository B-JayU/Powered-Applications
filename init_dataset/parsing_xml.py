# -*- coding:euc-kr -*-

import xml.etree.ElementTree as ELT
from bs4 import BeautifulSoup
import pandas as pd

data = pd.read_csv("./writers.csv")
df = pd.read_csv("./writers_with_features.csv")
print(df.info())

questions_with_accepted_answer = df[df["is_question"] & ~(df["AcceptedAnswerId"].isna())]
q_and_a = questions_with_accepted_answer.join(
    df[["body_text"]], on="AcceptedAnswerId", how="left", rsuffix="_answer"
)

pd.options.display.max_colwidth = 500
print(q_and_a[["body_text", "body_text_answer"]][:5])

received_answers = df[df['is_question'] & (df["AnswerCount"]!=0)]
has_accepted_answer = df[df["is_question"] & ~(df["AcceptedAnswerId"].isna())]

print("총 질문: %s개, 1개 이상의 답변을 가진 질문 : %s개, 답변이 채택된 질문: %s개" % (len(df['is_question']), len(received_answers),
                                                            len(has_accepted_answer)))
