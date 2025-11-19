import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple command-line tool to help solve math problems.")

    parser.add_argument("prob", help="Please provide a math problem for Gemini to solve.")

    args = parser.parse_args()
    print(f"{args.prob}")

if __name__ == "__main__":
    main()