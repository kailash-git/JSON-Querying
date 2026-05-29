from engine.loader import load_json
from engine.parser import parse_query
from engine.qury import run_query

# Load dataset
data = load_json("data/netflix_titles.json")

print("JSON Query Engine")

while True:

    query = input("\nEnter Query: ")

    if query.lower() == "exit":
        break

    try:
        parsed_query = parse_query(query)

        results = run_query(data, parsed_query)

        print("\nResults:\n")

        for result in results[:10]:
            print(result)

        print(f"\nTotal Results: {len(results)}")

    except Exception as e:
        print("Error:", e)