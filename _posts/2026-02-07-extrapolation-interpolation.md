---
layout: post
title: Interpolation, Extrapolation, and the Future of Thinking
date: 2026-02-07 15:58:10
description: Reflecting on the gap between pattern recognition and genuine discovery, and what it means for how we teach in an age of increasingly capable machines.
tags: teaching llm
categories: teaching llm
---

There's a distinction I keep returning to when I think about what exams measure and what research demands. The simplest way I've found to express it is this: most exams reward interpolation. Research, in contrast, is extrapolation.

I realize this sounds like a neat formula, the kind that fits well in a tweet but collapses under scrutiny. And yet, the more I think about it, especially now, as large language models reshape how we write code, organize knowledge, and approach problems, the more this distinction feels very accurate.

## What Exams Actually Measure

Consider how exam preparation works. Students train on a finite set of exercises, examples, and problem types. The exam samples from roughly the same distribution. Questions may be disguised, combined, or slightly perturbed, but they remain, in a statistical sense, within the convex hull of what has already been seen. Success requires recognizing patterns, mapping them to known solutions, and executing reliably.

This is not inherently bad. Interpolation is a real skill. It reflects domain mastery, technical fluency, and the ability to apply known ideas consistently. These matter. But we should be honest about what exams measure, and what they do not.

Research asks a different question. Not "have you seen something like this before?" but "what happens outside what we currently understand?" The goal is not to recombine known patterns, but to push beyond them: to ask questions that were not part of the training set, to explore regimes where existing tools break down, and to build new concepts when old ones no longer suffice.

And yet, something important happens during exam preparation that I think we often overlook. When students work through exercises, they're not just memorizing solutions, they're building an internal structure, a way of seeing patterns, a repertoire of moves. This repertoire becomes the foundation for extrapolation. You cannot extrapolate from nothing. The ability to venture beyond known territory requires first having stable ground to stand on, a rich enough internal model that you can recognize when something is genuinely new versus merely unfamiliar.

In this sense, the interpolation skills developed through exams are not opposed to extrapolation, they're prerequisite to it. The student who has deeply internalized enough examples, who has practiced recognizing structure across varied problems, is better equipped to notice when a problem falls outside the known space and requires something different. Mastery of interpolation, paradoxically, is what makes extrapolation possible.

## Neural Networks as Interpolators

Neural networks, as commonly trained today, are extraordinarily good interpolators. Given enough data, they approximate complex functions with impressive accuracy within the region covered by that data. But they are notoriously brittle when asked to extrapolate.

I have seen this many times in my research. A simple illustration: the classic PenDigits dataset [1]. The task is handwritten digit recognition, but the test set comes from different writers than the training set. Humans barely notice the shift, we effortlessly generalize across writing styles, strokes, and personal quirks. Neural networks often suffer a significant performance drop. The distribution shift is small in human terms but large in statistical ones.

The network has learned *what digits look like in the training distribution*, not what a digit *is*.

This gap between interpolation and extrapolation appears everywhere: reinforcement learning, control, language, reasoning. Models excel when test data is "more of the same" and struggle when structure changes meaningfully. Humans extrapolate constantly. We reason with sparse data, build mental models, apply them in novel situations. When faced with a new problem, we don't merely search for a nearby example, we ask what should happen, based on principles, abstractions, and causal understanding.

Seen through this lens, many current debates become clearer. Exams benchmark interpolation, which is extremely useful on its own. Benchmarks test generalization within a dataset family. Research requires extrapolation beyond it. Conflating the two leads to confusion, inflated expectations, and misplaced fears.

None of this diminishes the value of neural networks or large language models (LLMs). Interpolation at scale is powerful. It changes how we access information, explore ideas, and prototype solutions. But extrapolation, the ability to genuinely extend knowledge, remains a different problem.

## The Shift Toward Autonomous Systems

Something has changed in how companies approach software development [2,3]. The phrase "the art of programming" already hints at something important: programming has an artistic component. There's care in making code beautiful, readable, extensible, maintainable. That matters, especially to programmers themselves.

But historically, programming was never an end in itself. It's a means to an end. Companies build products for users, not for the intrinsic beauty of the codebase. If we view programming primarily as a tool, then it's natural to want something better at achieving the underlying goal.

If the resulting code is ugly underneath but produces correct answers, the goal is achieved; if a client is unhappy and we can ask a system to refine the pipeline without breaking it; if this refinement happens in hours without supervision, this is the grail many companies, and many researchers, have chased for decades.

For a long time, large language models simply weren't reliable enough to write or maintain code at scale. Around December 2025, something shifted. With the previous introduction of agents, skills, and now better performing models, notably Claude Code, coding capabilities changed qualitatively. Instead of producing code that degraded as complexity increased, agents began writing systems that could repair themselves, improve iteratively, and remain stable over time.

Much of this improvement addresses what I think of as the context problem. When a single model tries to reason about everything at once, its context becomes polluted and output quality drops sharply. Agent-based systems [4] mitigate this by decomposing work into smaller subtasks. A child agent focuses narrowly on a specific problem, then sends a concise summary back to its parent. This keeps the parent's context clean while preserving essential information for coordination.

Another key idea is what we call skills [5], particularly in the Model Context Protocol (MCP) [6] context. The goal: give language models access to the external world through tools. Naively, this would require exposing large APIs directly in the model's context. Imagine giving an LLM access to all of Chrome's functionality, the API alone would overwhelm the context window immediately. Skills solve this by acting as minimal specifications of desired interactions. A small team of agents builds the required tool on the fly, exposing only a narrow interface. The orchestrating agent operates with a minimal API in context, drastically improving reliability.

To demonstrate this works in practice, Anthropic recently built a complete C compiler using agents, a budget around $20,000, and only the C language specification. This compiler isn't yet on par with GCC, it's slower and less optimized, but it achieved something I find remarkable: it successfully compiled the full Linux kernel.

That's not a toy benchmark. It's a strong signal we're approaching a world where fully automatic systems are not just plausible but operational.

## When Correctness Decouples from Quality

This experiment makes one thing clear to me: goal-directed correctness is now decoupling from code quality.

Compiling the Linux kernel is one of the most demanding integration tests in systems programming: enormous codebase, decades of accumulated assumptions, undefined behaviors, edge cases, architecture-specific quirks, implicit contracts. That a compiler written autonomously by LLM agents can get that far already feels extraordinary to me.

Even with all the caveats, inefficient generated code, reliance on GCC for some phases, lack of elegance, partial shortcuts, the result surprised me. A 100,000-line clean-room compiler, capable of building Linux 6.9 on multiple architectures, would have been considered science fiction not long ago. The fact that it's "ugly" by expert standards doesn't really matter at this stage. What matters is that the system can navigate toward a precise goal, detect failures, adapt its behavior, and eventually satisfy a brutally strict external constraint.

This is where the interpolation versus extrapolation distinction becomes interesting again.

The agents aren't "inventing" compiler theory. They're not discovering new abstractions in the sense a human researcher might. Instead, they're performing massive, guided interpolation in the space of known ideas, implementations, and failure modes, but at a scale and persistence no human could sustain. Thousands of iterations, relentless testing, endless retries, zero fatigue. The result is not a beautiful solution but a working one.

And I think that's the key shift.

For many practical goals, ugly but correct is already sufficient. The traditional human advantage, writing clean, elegant, well-factored code, is no longer the decisive bottleneck for many tasks. What becomes decisive is the ability to define the right goal, design the right tests, and recognize when the system is fooling itself.

Notice how much success in the Anthropic experiment comes not from "better prompts" but from better harnesses: carefully designed tests, oracles (GCC as a reference), feedback loops, constraints that make it possible for agents to orient themselves. The intelligence is not just in the model; it's in the structure surrounding it.

## What This Means for Human Expertise

This reframes human contribution. If LLM agents can already produce large, functional systems, human expertise shifts upward: toward theory, toward specification, toward reasoning about correctness, complexity, invariants, failure modes. 

This is exactly why I believe theoretical knowledge, algorithmic thinking, and mathematical maturity matter more, not less, in the age of LLMs. These are the tools needed to design the harness, not just the code.

Which brings me back to education, exams, and skills.

The world doesn't need everyone to be a human GCC. But it desperately needs people who can tell whether a system is correct, understand why it works, see where it might break, and design constraints that prevent silent failure. That kind of judgment can't be outsourced to an interpolator. It's built through deep understanding, abstraction, and disciplined reasoning, precisely the skills developed through theory-heavy courses, exploratory problem solving, and yes, well-designed exams.

The Anthropic compiler is impressive to me not because it replaces human programmers outright, but because it exposes where human value now lies. We're moving from writing code to shaping computation. From producing artifacts to defining spaces in which artifacts can be safely generated.

In that world, learning to think formally, whether through mathematics, algorithms, or programming-as-experimentation, isn't an anachronism. It's preparation.

## Why LLMs Remain Interpolators (For Now)

LLMs are remarkable interpolators over an enormous and diverse corpus of human text. The interpolation space is vast, which makes their outputs appear surprisingly general. But vast interpolation is still interpolation. The fact that the space is high-dimensional and richly structured doesn't automatically grant extrapolative ability in the sense research demands.

Of course, for some problems, even if humans don't have the answer yet, having a big corpus of data allows LLMs to get pretty far in what could be considered extrapolation. But in practice, from the model's perspective, it's still interpolation.

This explains why LLMs can feel simultaneously impressive and fragile. They answer questions, generate code, and explain concepts fluently, until the problem subtly steps outside the patterns they've internalized. Then the cracks show: confident but incorrect answers, brittle reasoning chains, shallow analogies that collapse under scrutiny.

I've seen this firsthand when I code. When I ask an LLM for generic code, it produces several versions with different strategies, in many languages. When I ask for scientific code, it's usually full of mistakes, offers only one approach, and the number of languages is restricted. This suggests to me they can't really extrapolate, at least not yet.

If we want machines to participate in research rather than merely assist with it, we need to understand this gap clearly, not blur it with impressive demos. And if we want to educate students for research, we should be honest about what our exams actually measure. Because passing an exam means you can interpolate. Doing research means you can go where the map ends. Or so I thought, until recently.

## When Machines Do Extrapolate

At this point, it would be tempting to conclude that machines are condemned to interpolation, that extrapolation remains uniquely human. Recent events complicate that story, and I find them fascinating.

Earlier this month (02.2026), the startup Axiom published four original mathematical papers [7-11], each containing a complete and mechanically verified proof of a previously unsolved or partially solved problem. In one striking case, a problem in algebraic geometry that had resisted human effort for five years was solved overnight after being presented to Axiom's system. The key step wasn't brute-force computation but a reformulation of the problem, a change of perspective that reduced it to a known identity no one had noticed was relevant.

This is precisely the kind of move we associate with extrapolation.

What makes this particularly interesting to me is not just that the proofs exist, but how they were produced. The system doesn't merely generate informal arguments, it translates the entire reasoning process into Lean, a formal proof language in which every logical step is mechanically checked. The result is not a persuasive explanation but an object that can be verified, rerun, and audited by anyone.

This matters because it sharply constrains the space in which the system operates.

A large language model trained purely on natural language is free to interpolate fluently across human text, but it's also free to hallucinate, gloss over gaps, and smuggle in unjustified steps. Lean removes that freedom.

Lean [12,13] is a proof assistant, software that requires every step of a mathematical proof to be formally verified by a computer. Think of it as a compiler for mathematical reasoning: either your proof type-checks, or it doesn't. There's no such thing as "almost correct". The dependency either exists or it fails.

This is why, in my view, training models with formal systems like Lean is the right direction of progress beyond purely interpolative networks. Lean acts as a forcing function toward extrapolation.

To succeed, the model must construct chains of reasoning that survive outside the statistical comfort zone of plausible text. It must discover structures that actually hold, not just ones that sound right. Reformulation becomes a necessity, not a stylistic flourish. The system is pushed away from surface-level interpolation toward something closer to genuine conceptual navigation.

I find myself wondering: if we stretch this idea further, by retraining with novel discoveries, and if continual learning [14] one day succeeds, we could directly incorporate theorems that were previously unknown into the training set. This wouldn't be cheating with train/validation splits because they can be formally verified. Incorporating formal verification as part of the loss function means we can generate many new verifiable examples automatically. So, step by step, training by training, we might enable genuine extrapolation.

In mathematics, Lean doesn't discover proofs in a vacuum. It provides a formal environment where correctness is non-negotiable, where every step must type-check, where ambiguity is eliminated. When LLMs are trained and evaluated inside such environments, something important happens: they stop optimizing for plausibility and start optimizing for truth.

For programming, I think we're converging toward the same idea. Strong test suites, formal specifications, verified compilers, property-based testing, model checking, these aren't just "engineering best practices" anymore. They're becoming the interface between human intent and machine interpolation. A "Lean for programming", or rather, a family of formal, executable specifications, may be the most realistic path forward for reliable autonomous software development.

## The Structure of Extrapolation

This reframes the earlier distinction. Perhaps the issue isn't that machines can't extrapolate, but that extrapolation requires a space where correctness is rigid, feedback is immediate, and structure can't be faked. Mathematics, when formalized, provides exactly that environment.

Interestingly, this mirrors how humans learn to extrapolate in mathematics. We don't acquire that skill by reading polished proofs alone, but by struggling with definitions, failing attempts, reformulating problems, and checking every step until something finally clicks. Lean externalizes this discipline. It turns extrapolation into a navigable space rather than an act of intuition alone.

From this perspective, systems like Axiom don't contradict the claim that exams test interpolation and research demands extrapolation. They reinforce it. What they show is that extrapolation becomes accessible to machines when the task is embedded in a formal structure that enforces meaning.

Large language models trained only on text remain extraordinary interpolators. Large language models trained to reason inside formal systems may become something else entirely.

Whether that path leads to AGI is an open question. But if it does, I don't think it will come from ever-larger benchmarks that reward familiarity. It will come from environments where the map is incomplete, the rules are strict, and the only way forward is to genuinely discover new structure.

That, after all, is what research has always been.

## In Defense of Exams and Skill-Building

This perspective changes how I think about exams. They're often criticized as artificial, stressful, or disconnected from real-world practice. Some of that criticism is justified. But exams do something I find extremely valuable: they build skills.

A well-designed exam doesn't primarily test whether a student remembers a formula. It tests whether they can recognize structure, choose an approach, reason under constraints, and adapt known ideas to a new situation. In other words, it tests controlled extrapolation. Not full research-level discovery, but the ability to go beyond rote interpolation while remaining within a well-defined space.

This matters even more today than a decade ago, I think.

We're entering a world where writing code, in the narrow sense of producing syntactically correct programs, is no longer the bottleneck. LLM-based agents can already generate large amounts of usable code, refactor existing systems, and explore implementation variants far faster than a human. As this trend continues, the scarce skill won't be typing programs but deciding what should be built, why it should work, and how to tell whether it actually does.

Those are theoretical skills.

Algorithmic thinking, mathematical reasoning, abstraction, and the ability to hold multiple interacting constraints in mind are precisely the abilities that exams, at their best, are designed to cultivate. They train students to reason without scaffolding, to operate when the path is not spelled out, and to notice when something is missing or inconsistent. These are the same skills required to guide, question, and correct LLMs rather than blindly trust them.

This doesn't mean programming becomes irrelevant. Quite the opposite.

Programming remains a crucial epistemic tool. When studying a theoretical concept, the ability to simulate it, plot it, stress-test it, or explore edge cases computationally is invaluable. Writing small programs forces precision. It exposes hidden assumptions. It turns vague understanding into something concrete and falsifiable.

Even if future software production relies heavily on automated agents, programming will still play the same role that experiments play in physics or diagrams play in mathematics: a way to think, not just a way to deliver a product.

The skill shift isn't from programming to theory, but from programming-as-output to programming-as-understanding. Exams, theory-heavy courses, and exploratory coding all point in the same direction: training minds that can reason, validate, and guide intelligent tools rather than compete with them.

If LLMs are becoming powerful extrapolators in constrained formal environments like Lean, then education must focus even more on something different but complementary: producing humans who can extrapolate in messy, undefined spaces where formal systems don’t yet exist.

That includes recognizing which problems need formalization, crafting the right constraints, and building the harnesses that make machine extrapolation possible. These are not mechanical tasks. They require judgment, taste, and deep theoretical understanding, qualities that cannot be outsourced to automation without first being supplied by humans.

There's a pattern here worth noting. Every time we automate a skill, we don't make that skill obsolete, we make the meta-skill of understanding and judging it more valuable. Calculators didn't make arithmetic irrelevant; they made numerical reasoning more important. Compilers didn't make understanding code irrelevant; they made understanding abstractions essential.

But there's a crucial difference with LLMs that changes the nature of this pattern. Calculators and compilers are deterministic machines. We trust them precisely because they produce the same output every time, because their behavior is predictable and verifiable. LLMs, even those enhanced with formal systems, remain fundamentally stochastic at their core. The same prompt can yield different answers, some correct, some plausible, some subtly wrong. This introduces a qualitatively different kind of problem: the output can shift between runs, and there's no guarantee of consistency even when formal verification catches logical errors.

So the pattern still holds, but the meta-skill has evolved. With deterministic tools, we learned to trust the tool and focus on formulating the right question. With stochastic tools, even powerful ones, we need something more demanding: the ability to formulate questions, the judgment to evaluate whether the answer is trustworthy, and the theoretical grounding to verify the result independently. The burden of verification doesn't disappear, it intensifies. And this makes rigorous thinking, the kind that distinguishes plausible from correct, more critical than ever.

This is what exams, at their best, have always tested: not memory, but judgment. Not reproduction, but recognition. Not what you've seen, but what you can see.

# Conclusion

In a world where machines can interpolate at massive scale, and in special cases, extrapolate within formal constraints, exams and disciplined study matter more than ever. Not despite the fact that they primarily test interpolation, but because of it.

The interpolative skills they build, recognizing structure, reasoning under constraints, building mental repertoires, are precisely what enable extrapolation. You cannot venture beyond the map without first learning to read it. The students who develop deep interpolative mastery, who internalize enough examples to see patterns across problems, are the ones who will recognize when they've stepped outside known territory and need to think differently.

That recognition, that capacity to distinguish familiar from genuinely novel, is itself a form of extrapolation. And it begins with disciplined study, with well-designed exams, with the hard work of building internal structure.

That's not a threat to education. It's a reminder of what education has always been for.


## Additional notes:

### The Debugging Nightmare and the "Complexity Wall"
There is a profound difference between a codebase that is "ugly" because of human laziness and one that is "ugly" because it was synthesized through millions of stochastic iterations. Human-written mess usually follows some form of idiosyncratic logic—there is a "ghost in the machine" you can eventually reason with. Machine-generated mess is often structurally alien.

As we move toward a world of "Post-Elegance Engineering," we face a terrifying debugging nightmare: the Complexity Wall. If a team of agents builds a 100,000-line system that functions today, what happens when it fails tomorrow in a way the agents cannot self-repair? We risk creating "digital black boxes", systems that are functionally correct but cognitively impenetrable. Humans generally dislike working in environments where they lack "conceptual ownership". If we cannot navigate the code, we cannot truly trust it. The psychological toll of maintaining a system one does not understand is a variable we haven't yet factored into the future of work. We don't yet know if the efficiency of automated generation will be eventually canceled out by the sheer cognitive load of human oversight.

### The Economics of the Agentic Employee
To put the Anthropic experiment in perspective, consider the cost. Building a functional C compiler for $20,000 in two weeks is an incredible feat of efficiency when compared to traditional labor.

In 2026, a mid-level software engineer carries a total compensation package of roughly $150,000 to $400,000 when factoring in benefits and corporate overhead. A junior engineer might cost $90,000. If an AI agent burns $1,000 a day in API credits, it is roughly equivalent to the gross salary of a single full-time employee, but with zero "hidden" costs like healthcare, office space, or management latency. Crucially, the agent doesn't sleep; it provides the output of an entire 16-person "team" for the price of one human specialist. We are no longer just buying a tool; we are leasing a workforce.

### Verification: The Case of Axiom
The recent breakthroughs from Axiom are promising, but we must remain cautious. While the proofs themselves are mechanically verified by Lean, eliminating the standard concern of LLM hallucination, the "how" remains a black box. These are incredibly recent papers, and we do not yet fully understand the implications of the training methodology used to produce them. We don't know if this approach scales, if it relies on subtle data contamination, or if it represents a sustainable path toward general reasoning.

Until these results are fully integrated into the broader mathematical canon and the underlying training paradigms are transparently stress-tested by the research community, they remain "promising artifacts" rather than settled law. But they prove one thing: when we give an interpolator a formal cage to play in, it can occasionally find the key to the door leading outside.

Ultimately, these notes reinforce the same conclusion: whether we are navigating an alien codebase or auditing a machine-generated proof, the burden of final judgment remains stubbornly human.


# References:

1. Alpaydin, E. & Alimoglu, F. (1996). Pen-Based Recognition of Handwritten Digits [Dataset]. UCI Machine Learning Repository. [10.24432](https://doi.org/10.24432/C5MG6K).
2. [strongDM](https://factory.strongdm.ai/), [Wayback](https://web.archive.org/web/20260207182116/https://factory.strongdm.ai/)
3. [Simon Willison critic on StrongDM](https://simonwillison.net/2026/Feb/7/software-factory/), [Wayback](https://web.archive.org/web/20260207155128/https://simonwillison.net/2026/Feb/7/software-factory/)
4. [Agents](https://www.anthropic.com/engineering/building-effective-agents), [Wayback](https://web.archive.org/web/20260122170652/https://www.anthropic.com/engineering/building-effective-agents)
5. [Skills](https://code.claude.com/docs/en/skills), [Wayback](https://web.archive.org/web/20260207050926/https://code.claude.com/docs/en/skills)
6. [Model Context Protocol Specification](https://modelcontextprotocol.io/), [Wayback](https://archive.is/oT9GA)
7. [Axiom theorem proving (french)](https://www.lesnumeriques.com/intelligence-artificielle/une-ia-vient-de-resoudre-quatre-enigmes-mathematiques-complexes-que-personne-n-avait-denouees-n251153.html), [Wayback](https://web.archive.org/web/20260206182303/https://www.lesnumeriques.com/intelligence-artificielle/une-ia-vient-de-resoudre-quatre-enigmes-mathematiques-complexes-que-personne-n-avait-denouees-n251153.html)
8. [Parity of k-differentials in genus zero and one, 2602.03722](https://arxiv.org/pdf/2602.03722)
9. [Fel's conjecture on syzygies of numerical semigroups, 2602.03716](https://arxiv.org/pdf/2602.03716)
10. [Dead ends in square-free digit walks ,2602.05095](https://arxiv.org/pdf/2602.05095)
11. [Almost all primes are partially regular ,2602.05090](https://arxiv.org/pdf/2602.05090)
12. Moura, L.d., Ullrich, S. (2021). The Lean 4 Theorem Prover and Programming Language. In: Platzer, A., Sutcliffe, G. (eds) Automated Deduction – CADE 28. CADE 2021. Lecture Notes in Computer Science, vol 12699. Springer, Cham. [10.1007/978-3-030-79876-5_37](https://doi.org/10.1007/978-3-030-79876-5_37)
13. [The Lean Theorem Prover](https://lean-lang.org/)
14. [Continual Learning with RL](https://cameronrwolfe.substack.com/p/rl-continual-learning), [Wayback](https://web.archive.org/web/20260127125419/https://cameronrwolfe.substack.com/p/rl-continual-learning)
