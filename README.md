# MPC-Inspired Threat Intelligence Collaboration

**Author:** Diego Pfeiffer
**Focus Areas:** Cyber Threat Intelligence (CTI), Privacy-Preserving Analytics, MPC Concepts, OSINT Automation

---

## 1. Project Objective

The objective of this project is to demonstrate how **Multi-Party Computation (MPC) principles** can be applied to real-world **cyber threat intelligence collaboration** challenges.

Specifically, this project models how multiple organizations can:

* Collaboratively analyze indicators of compromise (IOCs)
* Identify shared or overlapping malicious infrastructure
* Generate actionable intelligence insights

**without directly sharing raw, sensitive data** such as IP addresses, domains, or hashes.

This mirrors real constraints faced by government, defense, and private-sector CTI teams, where legal, ethical, and operational concerns limit direct data sharing.

---

## 2. Problem Context

Threat intelligence collaboration is often limited by:

* Sensitivity of sources and methods
* Classification or contractual data-sharing restrictions
* Risk of exposing proprietary or investigative information

Despite these constraints, organizations still need ways to:

* Compare indicators
* Detect coordinated campaigns
* Identify shared infrastructure or adversary behavior

This project explores how **privacy-preserving computation techniques** can support those goals.

---

## 3. Scope of the Project

This project is intentionally scoped to be:

* **Educational and demonstrative**
* **Technically honest and defensible**
* **Directly relevant to CTI workflows**

### Included in Scope

* Deterministic masking of IOCs using cryptographic hashing
* XOR-based secret sharing to split sensitive values
* Secure aggregation over partial data inputs
* Generation of non-sensitive analytical outputs
* Clear separation between local processing and shared computation

### Explicitly Out of Scope

* Formal cryptographic MPC protocols (e.g., SPDZ, Yao circuits)
* Claims of production-grade cryptographic security
* Fully decentralized trustless computation
* Encrypted network transport or authentication layers

The design emphasizes **conceptual correctness and practical relevance**, not cryptographic novelty.

---

## 4. Design Principles

The project follows several guiding principles relevant to CTI and security engineering:

1. **Data Minimization**
   Only the minimum information required for analysis is shared.

2. **Input Privacy**
   Raw IOCs never leave the originating party’s environment.

3. **Separation of Trust**
   No single entity has access to both raw data and reconstructed secrets.

4. **Actionable Output Only**
   Outputs are high-level analytical conclusions rather than sensitive indicators.

---

## 5. High-Level Architecture

Each participating organization runs the same local processing logic:

1. Load locally held IOCs
2. Apply deterministic hashing to mask indicator values
3. Split masked indicators into secret shares
4. Retain one share locally
5. Share only a partial, non-reversible share externally

A central aggregation process:

* Receives partial shares from multiple parties
* Performs aggregation and pattern analysis
* Produces safe, non-sensitive intelligence outputs

At no point does the aggregator have access to raw or fully reconstructed IOCs.

---

## 6. Repository Structure

```text
src/
├── party.py        # Local processing per organization
├── aggregator.py   # Secure aggregation logic
├── mpc_utils.py    # MPC-inspired primitives

data/
├── party_a_iocs.json
├── party_b_iocs.json

README.md
requirements.txt
```

---

## 7. How This Demonstrates MPC Concepts

While not a formal MPC implementation, this project demonstrates key MPC ideas:

* **Private inputs**: Each party retains control of sensitive data
* **Secret sharing**: Sensitive values are split into multiple components
* **Joint computation**: Analysis occurs across partial inputs
* **Restricted outputs**: Only safe results are revealed

These concepts map directly to real-world privacy-preserving analytics use cases in security and intelligence environments.

---

## 8. Relevance to Cyber Threat Intelligence

This project reflects challenges faced by:

* Government CTI fusion centers
* Defense contractors and FFRDCs
* Private-sector intelligence sharing groups

It demonstrates:

* Secure design thinking
* Understanding of CTI operational constraints
* Ability to translate abstract security concepts into practical tooling

---

## 9. Limitations and Disclaimer

This project is **educational** and **demonstrative**.

* It does not claim cryptographic security guarantees
* It should not be used in production environments
* It is intended to show design reasoning, not deployable security

All MPC concepts are presented in a simplified, transparent manner for learning and discussion.

---

## 10. Future Extensions

Potential future improvements include:

* Integration with public threat-intelligence APIs
* AI-assisted analysis of aggregated outputs
* Threshold-based secret sharing
* Time-series correlation of indicators
* Exploration of formal MPC frameworks for research purposes

---

## 11. Key Skills Demonstrated

* Python scripting for security use cases
* Threat intelligence workflows
* Privacy-preserving system design
* MPC conceptual fluency
* Secure collaboration models
* Clear technical documentation

---

This repository is designed to clearly communicate **how and why** MPC-inspired approaches matter in cyber threat intelligence, particularly in environments where trust, privacy, and mission impact are critical.