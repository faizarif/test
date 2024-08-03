alpaca_prompt = """Below is an extraction from architecture diagram which shows the software used, Problem Statement , Probable Solutions Paths, Benefits, Cons, Risks , Dependencies, Systems Impacted your task is to classify based Class which is provided.

### Instruction:
{}

### Software Used:
{}

### Problem Statement:
{}

### Problem Solution Paths:
{}

### Benefits:
{}

### Cons:
{}

### Risks:
{}

### Dependencies:
{}

### System Impacted:
{}

### Class:
{}"""

# EOS_TOKEN = tokenizer.eos_token
def formatting_prompts_func(examples):
    instructions= "Below is the extraction from architecture diagram give class taking inputs like software_used,problem_statement,problem_solution_paths,benefits,cons,risks,dependencies,system_impacted"
    software_used= examples["software_used"]
    problem_statement=examples["problem_statement"]
    problem_solution_paths=examples["problem_solution_paths"]
    benefits=examples["benefits"]
    cons=examples["cons"]
    risks=examples['risks']
    dependencies=examples['dependencies']
    system_impacted=examples['systems_impacted']
    Class= examples["class"]
    texts = []
    for instructions,software_used,problem_statement,problem_solution_paths,benefits,cons,risks,dependencies,system_impacted,Class in zip(instructions,software_used,problem_statement,problem_solution_paths,benefits,cons,risks,dependencies,system_impacted,Class):
        # Must add EOS_TOKEN, otherwise your generation will go on forever!
        text = alpaca_prompt.format(instructions,software_used,problem_statement,problem_solution_paths,benefits,cons,risks,dependencies,system_impacted,Class)
        texts.append(text)
    return { "text" : texts, }
pass

from datasets import load_dataset
from datasets import Dataset
import pandas as pd
df = pd.read_excel("dummy_text_multiclass.xlsx")
dataset = Dataset.from_pandas(df)
print(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)
