---
title: "AI/LLM Security Resources"
summary: "Curated standards, labs, tools, and guidance for defensive AI application security and prompt injection testing."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - ai-security
  - llm-security
  - prompt-injection
  - rag
  - tools
related:
  - ../bug-classes/ai-llm/README.md
  - ../bug-classes/ai-llm/prompt-injection.md
  - ../playbooks/ai-llm-application-review.md
references:
  - https://genai.owasp.org/
  - https://portswigger.net/web-security/llm-attacks
  - https://atlas.mitre.org/
---

# AI/LLM Security Resources

This page collects high-signal public resources for securing and testing AI-enabled applications.

## Standards And Taxonomies

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) - primary LLM application risk taxonomy.
- [OWASP GenAI Security Project](https://genai.owasp.org/) - OWASP hub for GenAI, LLM, agentic security, governance, and resources.
- [MITRE ATLAS](https://atlas.mitre.org/) - adversarial AI tactics, techniques, and case studies.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - governance framework for AI risk.
- [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) - GenAI-specific AI RMF profile.
- [Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) - joint international guidance for secure AI design, development, deployment, and operation.

## Prompt Injection And LLM App Testing

- [PortSwigger Web LLM Attacks](https://portswigger.net/web-security/llm-attacks) - lab-safe learning for prompt injection, indirect injection, tools, and insecure output handling.
- [Simon Willison prompt injection archive](https://simonwillison.net/tags/prompt-injection/) - clear writing on prompt injection, indirect injection, and the private-data/untrusted-content/exfiltration-channel risk pattern.
- [Microsoft Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter-prompt-shields) - user prompt and document attack taxonomy plus mitigation concepts.
- [NVIDIA: Securing LLM Systems Against Prompt Injection](https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/) - tool/plugin risk and mitigation discussion.
- [Anthropic: Reduce Prompt Leak](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak) - practical guidance for reducing hidden prompt leakage.
- [Lakera Gandalf](https://gandalf.lakera.ai/) - public lab for prompt-injection awareness training.

## AI Red Team And Methodology

- [Microsoft AI Red Team](https://learn.microsoft.com/en-us/security/ai-red-team/) - AI red-team guidance hub.
- [Microsoft PyRIT](https://github.com/microsoft/PyRIT) - open-source Python Risk Identification Tool for generative AI red teaming.
- [Google Secure AI Framework](https://blog.google/technology/safety-security/introducing-googles-secure-ai-framework/) - control framework for secure AI systems.
- [CISA AI](https://www.cisa.gov/ai) - U.S. government AI security resource hub.

## Tools And Evaluation

- [garak](https://github.com/NVIDIA/garak) and [garak docs](https://docs.garak.ai/) - LLM vulnerability scanner for repeatable probing.
- [promptfoo](https://www.promptfoo.dev/) - prompt, RAG, red-team, and CI evaluation framework.
- [Giskard](https://docs.giskard.ai/) - AI evaluation and red-teaming platform.
- [Guardrails AI](https://www.guardrailsai.com/docs) - input/output validation and guardrail framework.
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - programmable guardrails for conversational and RAG applications.

## Model And AI Supply Chain

- [Protect AI ModelScan](https://github.com/protectai/modelscan) - scans serialized model files for unsafe code patterns.
- [PickleScan](https://github.com/mmaitre314/picklescan) - scans Python pickle artifacts before loading.
- [Hugging Face malware scanning docs](https://huggingface.co/docs/hub/security-malware) - model hub malware scanning behavior.
- [CycloneDX ML-BOM](https://cyclonedx.org/capabilities/mlbom/) - machine-learning bill of materials capability.

## Use Guidance

- Use OWASP LLM Top 10 for risk categories.
- Use PortSwigger labs and Lakera Gandalf for safe practice.
- Use MITRE ATLAS for technique mapping.
- Use NIST AI RMF and secure AI development guidance for governance.
- Use PyRIT, garak, promptfoo, and Giskard only against systems you own or are authorized to test.
- Treat model files as executable supply-chain inputs; scan before loading.
