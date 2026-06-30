# On the Emergence of Thinking in LLMs II: Thinking Big on Small Budgets

This repository contains the official codebase and implementation details for our project, **"On the Emergence of Thinking in LLMs II: Thinking Big on Small Budgets"**. 

This work was conducted as part of the **Natural Language Processing** course at the National Technical University of Athens (NTUA). Our project focuses on the replication and subsequent expansion of the research presented in the original _"On the Emergence of Thinking in LLMs Ι: Searching for the Right Intuition"_ paper.

---

## Technical Stack & Infrastructure
To conduct our experiments, we leveraged a hybrid compute approach:
* **Environments:** Development and training were performed across **Kaggle** kernels, **Lightning AI** nodes, and **local hardware resources**.
* **Model Constraints:** Due to hardware limitations, we utilized smaller, efficient models: **Qwen/Qwen2.5-1.5B-Instruct** and **meta-llama/Llama-3.2-1B-Instruct**.
* **Optimization Strategies:** To bypass resource constraints, our pipeline incorporates **GRPO** (Group Relative Policy Optimization) instead of standard PPO for Llama-3.2-1B-Instruct model, alongside **LoRA** (Low-Rank Adaptation) and **quantization** techniques.

---

## Project Structure
The project is organized into two primary pillars:

1.  **Recreation:** A faithful reproduction of the methodologies and experiments outlined in the original research to establish a robust baseline.
2.  **Expansions:** Our original contributions, where we test **dynamic hyperparameters** and implement **different exploration reward functions** to analyze their impact on reasoning emergence.

---

## Participants (Alphabetical Order)
- [Γιωτίτσας Αναστάσιος]
- [Ηλιάδης Ηλίας-Στυλιανός]
- [Λιβανάς Δημήτριος]
- [Μανιατογιάννης Σταύρος]

---

## Documentation
For a comprehensive breakdown of our methodology, experiment configurations, and results, please refer to the `report.pdf` located in the root directory of this repository.