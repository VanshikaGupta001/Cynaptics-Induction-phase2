import pandas as pd
import tqdm
from trial import *

data= pd.read_csv("cases_preprocessed.csv")
df = pd.DataFrame(data)

case_verdicts = []  # Stores final results as [id, verdict]

def parse_verdict(text: str) -> int:
    
    return 1 if 'accept' in text.lower() else 0

for _, row in tqdm(df.iterrows(), total=len(df)/20):
    case_id = row['id']
    try:
        # Simulate judge response
        verdict_text = judge.respond(f"Case {case_id}: {row['description']}")
        verdict = parse_verdict(verdict_text)
    except Exception as e:
        print(f"Error processing Case {case_id}: {str(e)}")
        verdict = 0  # Default to rejection on failure
        print(case_verdicts)
        
    case_verdicts.append({
        "case_id": case_id,
        "verdict": verdict,
    })

