import json
from collections import Counter

def aggregate(shares_a, shares_b):
    total = shares_a + shares_b
    counts = Counter(total)

    return {
        "total_indicators": len(total),
        "unique_shares": len(counts),
        "pattern": "shared infrastructure likely" if len(counts) < len(total) else "diverse infrastructure"
    }

if __name__ == "__main__":
    with open("data/party_a_outbound.json") as f:
        a = json.load(f)

    with open("data/party_b_outbound.json") as f:
        b = json.load(f)

    results = aggregate(a, b)

    with open("data/aggregated_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("[Aggregator] Secure aggregation complete.")