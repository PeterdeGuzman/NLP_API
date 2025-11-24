import argparse
from google import genai
import pandas as pd
import os
from dotenv import load_dotenv

def main():
    #Define parser and args
    parser = argparse.ArgumentParser(description="A simple command-line tool built by Chris and Peter to help solve math problems.")
    parser.add_argument("prob_num", type=int, help="Please provide a number associated with a math problem for Gemini to solve.")
    args = parser.parse_args()
    print(f"{args.prob_num}")
    
    #Upload list of problems
    problem_list = pd.read_csv("math_data_summarized.csv")

    question_text = problem_list.iloc[0]
    
    if args.prob_num < 0 or args.prob_num >= len(problem_list):
        print(f"Error: Problem number must be between 0 and {len(problem_list)-1}")
        return
    
    question_text = problem_list.iloc[args.prob_num]['question']

    
    print(f"Question: {question_text}\n")

    #Call Gemini
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"Provide an answer to {question_text}"
)
    print(response.text)
if __name__ == "__main__":
    main()