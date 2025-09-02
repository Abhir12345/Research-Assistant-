import argparse
from src.graph_builder import app

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="Research topic to search")
    args = parser.parse_args()

    output = app.invoke({"query": args.query})
    print("\n📑 Literature Review Draft:\n")
    print(output["literature_review"])
