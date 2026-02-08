---
layout: post
title: Formal Verification and the Path to Machine Discovery
date: 2026-02-07 16:15:00
description: When machines prove theorems and why exams matter more than ever in an age of increasingly capable AI systems.
tags: teaching llm
categories: teaching llm
---

*This is Part 2 of a series on AI, education, and expertise. See also: [Part 1: The Rise of Autonomous Systems]({% link _posts/2026-02-07-extrapolation-interpolation_p1.md %})*
In the previous article, we saw how autonomous systems are decoupling correctness from code quality, producing functional but often "ugly" software through massive iteration. This raises a natural question: are machines fundamentally limited to recombining existing patterns (interpolation), or can they genuinely discover new knowledge (extrapolation)?

# Neural Networks as Interpolators

Neural networks, as commonly trained today, are extraordinarily good interpolators. Given enough data, they approximate complex functions with impressive accuracy within the region covered by that data. But they are notoriously brittle when asked to extrapolate.

I have seen this many times in my research. A simple illustration: the classic PenDigits dataset [1]. The task is handwritten digit recognition, but the test set comes from different writers than the training set. Humans barely notice the shift, we effortlessly generalize across writing styles, strokes, and personal quirks. Neural networks often suffer a significant performance drop. The distribution shift is small in human terms (extrapolation task) but large in statistical ones (interpolation task).

The network has learned *what digits look like in the training distribution*, not what a digit *is*.

This gap between interpolation and extrapolation appears everywhere: reinforcement learning, control, language, reasoning. Models excel when test data is "more of the same" and struggle when structure changes meaningfully. Humans extrapolate constantly. We reason with sparse data, build mental models, apply them in novel situations. When faced with a new problem, we don't merely search for a nearby example, we ask what should happen, based on principles, abstractions, and causal understanding.

Seen through this lens, many current debates become clearer. Exams benchmark interpolation, which is extremely useful on its own. Benchmarks test generalization within a dataset family. Research requires extrapolation beyond it. Conflating the two leads to confusion, inflated expectations, and misplaced fears.

None of this diminishes the value of neural networks or large language models (LLMs). Interpolation at scale is powerful. It changes how we access information, explore ideas, and prototype solutions. But extrapolation, the ability to genuinely extend knowledge, remains a different problem.

## Why LLMs Remain Interpolators

LLMs are remarkable interpolators over an enormous and diverse corpus of human text. The interpolation space is vast, which makes their outputs appear surprisingly general. But vast interpolation is still interpolation. The fact that the space is high-dimensional and richly structured doesn't automatically grant extrapolative ability in the sense research demands.

The agent-based coding systems from [Part 1]({% link _posts/2026-02-07-extrapolation-interpolation_p1.md %}), despite their impressive capabilities, remain fundamentally constrained to the realm of their training distribution.

Of course, for some problems, even if humans don't have the answer yet, having a big corpus of data allows LLMs to get pretty far in what could be considered extrapolation. But in practice, from the model's perspective, it's still interpolation.

This explains why LLMs can feel simultaneously impressive and fragile. They answer questions, generate code, and explain concepts fluently, until the problem subtly steps outside the patterns they've internalized. Then the cracks show: confident but incorrect answers, brittle reasoning chains, shallow analogies that collapse under scrutiny.

I've seen this firsthand when I code. When I ask an LLM for generic code, it produces several versions with different strategies, in many languages. When I ask for scientific code, it's usually full of mistakes, offers only one approach, and the number of languages is restricted. This suggests to me they can't really extrapolate, at least not yet.

If we want machines to participate in research rather than merely assist with it, we need to understand this gap clearly, not blur it with impressive demos. And if we want to educate students for research, we should be honest about what our exams actually measure. Because passing an exam means you can interpolate. Doing research means you can go where the map ends.

# Extrapolative Neural Networks

Recent events complicate that story, and I find them fascinating.

Earlier this month (02.2026), the startup Axiom published four original mathematical papers [2-6], each containing a complete and mechanically verified proof of a previously unsolved or partially solved problem. In one striking case, a problem in algebraic geometry that had resisted human effort for five years was solved overnight after being presented to Axiom's system. The key step wasn't brute-force computation but a reformulation of the problem, a change of perspective that reduced it to a known identity no one had noticed was relevant.

This is precisely the kind of move we associate with extrapolation.

What makes this particularly interesting to me is not just that the proofs exist, but how they were produced. The system doesn't merely generate informal arguments, it translates the entire reasoning process into Lean, a formal proof language in which every logical step is mechanically checked. The result is not a persuasive explanation but an object that can be verified, rerun, and audited by anyone.

This matters because it sharply constrains the space in which the system operates.

A large language model trained purely on natural language is free to generate fluent text, but it's also free to hallucinate, gloss over gaps, and smuggle in unjustified steps. Lean removes that freedom.

Lean [7,8] is a proof assistant, software that requires every step of a mathematical proof to be formally verified by a computer. Think of it as a compiler for mathematical reasoning: either your proof type-checks, or it doesn't. There's no such thing as "almost correct". The dependency either exists or it fails.

This is why, in my view, training models with formal systems like Lean is the right direction of progress beyond purely interpolative networks. Lean acts as a forcing function toward extrapolation.

What makes Axiom interesting as a case study isn't that we understand  its training methodology, we don't, and the papers are too recent for proper scrutiny. Rather, it's that Lean provides something the C compiler example lacked: **a mechanistic test for extrapolation**.

The C compiler could be evaluated on correctness (does it compile Linux?) but not on novelty (are the solutions new?). Axiom's proofs can be evaluated on both: Lean verifies correctness automatically, and the mathematical community can verify novelty by checking whether the theorems were previously proven.

This is why formal systems like Lean matter for understanding the interpolation/extrapolation boundary: they don't just constrain hallucination, they make the distinction between recombination and discovery *mechanically checkable*.

To succeed, the model must construct chains of reasoning that survive outside the statistical comfort zone of plausible text. It must discover structures that actually hold, not just ones that sound right. Reformulation becomes a necessity, not a stylistic flourish. The system is pushed away from surface-level interpolation toward something closer to genuine conceptual navigation.

I find myself wondering: if we stretch this idea further, by retraining with novel discoveries, and if continual learning [9] one day succeeds, we could directly incorporate theorems that were previously unknown into the training set. This wouldn't be cheating with train/validation splits because they can be formally verified. Incorporating formal verification as part of the loss function means we can generate many new verifiable examples automatically. So, step by step, training by training, we might enable genuine extrapolation.

In mathematics, Lean doesn't discover proofs in a vacuum. It provides a formal environment where correctness is non-negotiable, where every step must type-check, where ambiguity is eliminated. When LLMs are trained and evaluated inside such environments, something important happens: they stop optimizing for plausibility and start optimizing for truth.

For programming, I think we're converging toward the same idea. Strong test suites, formal specifications, verified compilers, property-based testing, model checking, these aren't just "engineering best practices" anymore. They're becoming the interface between human intent and machine interpolation. A "Lean for programming", or rather, a family of formal, executable specifications, may be the most realistic path forward for reliable autonomous software development.

### The Structure of Extrapolation

This changes how we think about machine learning. Perhaps the issue isn't that machines can't extrapolate, but that extrapolation requires a space where correctness is rigid, feedback is immediate, and structure can't be faked. Mathematics, when formalized, provides exactly that environment.

Interestingly, this mirrors how humans learn to extrapolate in mathematics. We don't acquire that skill by reading polished proofs alone, but by struggling with definitions, failing attempts, reformulating problems, and checking every step until something finally clicks. Lean externalizes this discipline. It turns extrapolation into a navigable space rather than an act of intuition alone.

From this perspective, systems like Axiom show us something important. What they demonstrate is that genuine discovery becomes accessible to machines when the task is embedded in a formal structure that enforces meaning.

Large language models trained only on text remain extraordinary interpolators. Large language models trained to reason inside formal systems may become something else entirely.

Whether that path leads to AGI is an open question. But if it does, I don't think it will come from ever-larger benchmarks that reward familiarity. It will come from environments where the map is incomplete, the rules are strict, and the only way forward is to genuinely discover new structure.

That, after all, is what research has always been.

# Conclusion

The thread running through this discussion is simple: what a system can do depends critically on the environment it is placed in. Interpolation thrives in open-ended spaces where plausibility is enough. Extrapolation requires something stricter, a setting where correctness is rigid, feedback is immediate, and shortcuts are impossible.

Large language models demonstrate how powerful interpolation can be at scale. That power is real and valuable, but mistaking it for discovery creates confusion in research, education, and public debate. Benchmarks overwhelmingly measure competence within a known distribution. Research, by contrast, begins when that distribution no longer applies.

Formal systems like Lean change this dynamic. They collapse the distinction between "sounds right" and "is right". When machines are forced to operate inside such systems, extrapolation becomes a navigable process rather than an act of stylistic fluency.

This has implications beyond AI. If we care about extrapolation, in students or machines, we must build environments that demand it. Mathematics, formal verification, and executable specifications show one viable path: restrict freedom in the right way, and genuine structure emerges, for students, it is still to be determined what is the right path.

## Additional notes:

### Verification: The Case of Axiom
The recent breakthroughs from Axiom are promising, but we must remain cautious. While the proofs themselves are mechanically verified by Lean, eliminating the standard concern of LLM hallucination, the "how" remains a black box. These are incredibly recent papers, and we do not yet fully understand the implications of the training methodology used to produce them. We don't know if this approach scales, if it relies on subtle data contamination, or if it represents a sustainable path toward general reasoning.

Until these results are fully integrated into the broader mathematical canon and the underlying training paradigms are transparently stress-tested by the research community, they remain "promising artifacts" rather than settled law. But they prove one thing: when we give an interpolator a formal cage to play in, it can occasionally find the key to the door leading outside.

Ultimately, these notes reinforce the same conclusion: whether we are navigating an alien codebase or auditing a machine-generated proof, the burden of final judgment remains stubbornly human.


These observations about formal systems, machine capabilities, and the importance of theoretical skills raise a deeper question: what fundamental distinction separates pattern recognition from genuine discovery? In the final part of this series, we'll explore this conceptual framework and what it means for how we think about learning, research, and the future of human expertise.

*Continue reading: [Part 3: Interpolation, Extrapolation, and What Exams Really Measure]({% link _posts/2026-02-07-extrapolation-interpolation_p3.md %}) - the core conceptual framework underlying this series*

# References:

1. Alpaydin, E. & Alimoglu, F. (1996). Pen-Based Recognition of Handwritten Digits [Dataset]. UCI Machine Learning Repository. [10.24432](https://doi.org/10.24432/C5MG6K).
2. [Axiom theorem proving (french)](https://www.lesnumeriques.com/intelligence-artificielle/une-ia-vient-de-resoudre-quatre-enigmes-mathematiques-complexes-que-personne-n-avait-denouees-n251153.html), [Wayback](https://web.archive.org/web/20260206182303/https://www.lesnumeriques.com/intelligence-artificielle/une-ia-vient-de-resoudre-quatre-enigmes-mathematiques-complexes-que-personne-n-avait-denouees-n251153.html)
3. [Parity of k-differentials in genus zero and one, 2602.03722](https://arxiv.org/pdf/2602.03722)
4. [Fel's conjecture on syzygies of numerical semigroups, 2602.03716](https://arxiv.org/pdf/2602.03716)
5. [Dead ends in square-free digit walks ,2602.05095](https://arxiv.org/pdf/2602.05095)
6. [Almost all primes are partially regular ,2602.05090](https://arxiv.org/pdf/2602.05090)
7. Moura, L.d., Ullrich, S. (2021). The Lean 4 Theorem Prover and Programming Language. In: Platzer, A., Sutcliffe, G. (eds) Automated Deduction – CADE 28. CADE 2021. Lecture Notes in Computer Science, vol 12699. Springer, Cham. [10.1007/978-3-030-79876-5_37](https://doi.org/10.1007/978-3-030-79876-5_37)
8. [The Lean Theorem Prover](https://lean-lang.org/)
9. [Continual Learning with RL](https://cameronrwolfe.substack.com/p/rl-continual-learning), [Wayback](https://web.archive.org/web/20260127125419/https://cameronrwolfe.substack.com/p/rl-continual-learning)
