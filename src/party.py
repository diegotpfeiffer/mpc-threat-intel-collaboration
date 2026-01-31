import json
import os
from mpc_utils import hash_ioc, split_secret

SALT = "shared_salt_for_demo_only"

def process_iocs(ioc_file):
    with open(ioc_file, "r") as f:
        iocs = json.load(f)

    masked = []
    shares = []

    for ioc in iocs:
        hashed = hash_ioc(ioc, SALT)
        share1, share2 = split_secret(hashed)

        masked.append(hashed)
        shares.append({
            "share_for_aggregator": share1,
            "local_share": share2
        })

    return masked, shares

if __name__ == "__main__":
    masked, shares = process_iocs("data/party_a_iocs.json")

    # Send ONLY share_for_aggregator outward
    outbound = [s["share_for_aggregator"] for s in shares]

    with open("data/party_a_outbound.json", "w") as f:
        json.dump(outbound, f)

    print("[Party] Masked IOCs processed and partial shares exported.")