import argparse
from google import genai
import pandas as pd

def main():
    #Define parser and args
    parser = argparse.ArgumentParser(description="A simple command-line tool to help solve math problems.")
    parser.add_argument("prob_num", help="Please provide a number associated with a math problem for Gemini to solve.")
    args = parser.parse_args()
    print(f"{args.prob_num}")
    
    #Upload list of problems
    problem_list = pd.read_csv("math_data_summarized.csv")

    question_text = problem_list.iloc[0]
    
    

    #Call Gemini
    client = genai.Client()
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"Provide an answer to {args.prob}"
)
    print(response.text)
if __name__ == "__main__":
    main()