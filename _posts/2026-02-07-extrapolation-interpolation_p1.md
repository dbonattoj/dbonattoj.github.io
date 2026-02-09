---
layout: post
title: The Rise of Autonomous Systems - When Machines Write Their Own Code
date: 2026-02-07 15:58:10
description: How LLM agents are decoupling correctness from elegance, and what this means for the future of software development and human expertise.
tags: teaching llm
categories: teaching llm
---

*This is Part 1 of a series on AI, education, and expertise.*

Something has changed in how companies approach software development [1,2]. The phrase "the art of programming" already hints at something important: programming has an artistic component. There's care in making code beautiful, readable, extensible, maintainable. That matters, especially to programmers themselves.

But historically, programming was never an end in itself. It's a means to an end. Companies build products for users, not for the intrinsic beauty of the codebase. If we view programming primarily as a tool, then it's natural to want something better at achieving the underlying goal.

If the resulting code is ugly underneath but produces correct answers, the goal is achieved; if a client is unhappy and we can ask a system to refine the pipeline without breaking it; if this refinement happens in hours without supervision, this is the grail many companies, and many researchers, have chased for decades.

For a long time, large language models simply weren't reliable enough to write or maintain code at scale. By late 2025, something shifted subtly. With the previous introduction of agents, skills, and now better performing models with longer horizon contextes and thinking capacities, notably Claude Code, coding capabilities changed qualitatively. Instead of producing code that degraded as complexity increased, agents began writing systems that could locally repair themselves, improve iteratively, and (hopefully) remain stable over time.

Much of this improvement addresses what I think of as the context problem. When a single model tries to reason about everything at once, its context becomes polluted and output quality drops sharply. Agent-based systems [3] mitigate this by decomposing work into smaller subtasks. A child agent focuses narrowly on a specific problem, then sends a concise summary back to its parent. This keeps the parent's context clean while preserving essential information for coordination.

Another key idea is what we call skills [4], particularly in the Model Context Protocol (MCP) [5] context. The goal: give language models access to the external world through tools. Naively, this would require exposing large APIs directly in the model's context. Imagine giving an LLM access to all of Chrome's functionality, the API alone would overwhelm the context window immediately. Skills solve this by acting as minimal specifications of desired interactions. A small team of agents builds the required tool on the fly, exposing only a narrow interface. The orchestrating agent operates with a minimal API in context, drastically improving reliability.

These architectural improvements enabled a remarkable demonstration, Anthropic recently built a complete C compiler using agents, a budget around $20,000, and only the C language specification [6]. This compiler isn't yet on par with GCC, it's slower and less optimized, but it achieved something I find remarkable: it successfully compiled the full Linux kernel.

That's not a toy benchmark. It's a strong signal we're approaching a world where fully automatic systems are not just plausible but operational.

## When Correctness Decouples from Quality

This experiment makes one thing clear to me: goal-directed correctness is now decoupling from code quality.

Compiling the Linux kernel is one of the most demanding integration tests in systems programming: enormous codebase, decades of accumulated assumptions, undefined behaviors, edge cases, architecture-specific quirks, implicit contracts. That a compiler written autonomously by LLM agents can get that far already feels extraordinary to me.

Even with all the caveats, inefficient generated code, reliance on GCC for some phases, lack of elegance, partial shortcuts, the result surprised me. A 100,000-line clean-room compiler, capable of building the Linux Kernel, would have been considered science fiction not long ago. The fact that it's "ugly" by expert standards doesn't really matter at this stage. What matters is that the system can navigate toward a precise goal, detect failures, adapt its behavior, and eventually satisfy a brutally strict external constraint.

The agents aren't "inventing" compiler theory. They're not discovering new abstractions in the sense a human researcher might. Instead, they're performing massive, guided search in the space of known ideas, implementations, and failure modes, but at a scale and persistence no human could sustain. Thousands of iterations, relentless testing, endless retries, zero fatigue. The result is not a beautiful solution but a working one.

And I think that's the key shift.

For many practical goals, ugly but correct is already sufficient. The traditional human advantage, writing clean, elegant, well-factored code, is no longer the decisive bottleneck for many tasks. What becomes decisive is the ability to define the right goal, design the right tests, and recognize when the system is fooling itself.

Notice how much success in the Anthropic experiment comes not from "better prompts" but from better harnesses: carefully designed tests, oracles (GCC as a reference), feedback loops, constraints that make it possible for agents to orient themselves. The intelligence is not just in the model; it's in the structure surrounding it.

## What This Means for Human Expertise

This reframes human contribution. If LLM agents can already produce large, functional systems through persistent iteration and testing, human expertise shifts upward: toward theory, toward specification, toward reasoning about correctness, complexity, invariants, failure modes.  

This is exactly why I believe theoretical knowledge, algorithmic thinking, and mathematical maturity matter more, not less, in the age of LLMs. These are the tools needed to design the harness, not just the code (more on this in [Part 3]({% link _posts/2026-02-07-extrapolation-interpolation_p3.md %})).

The world doesn't need everyone to be a human GCC. But it desperately needs people who can tell whether a system is correct, understand why it works, see where it might break, and design constraints that prevent silent failure. That kind of judgment can't be outsourced to automation. It's built through deep understanding, abstraction, and disciplined reasoning, precisely the skills developed through theory-heavy courses, exploratory problem solving.

The Anthropic compiler is impressive to me not because it replaces human programmers outright, but because it exposes where human value now lies. We're moving from writing code to shaping computation. From producing artifacts to defining spaces in which artifacts can be safely generated.

In that world, learning to think formally, whether through mathematics, algorithms, or programming-as-experimentation, isn't an anachronism. It's preparation.

## Additional notes:

### The Debugging Nightmare and the "Complexity Wall"
There is a profound difference between a codebase that is "ugly" because of human laziness and one that is "ugly" because it was synthesized through millions of stochastic iterations. Human-written mess usually follows some form of idiosyncratic logic—there is a "ghost in the machine" you can eventually reason with. Machine-generated mess is often structurally alien.

As we move toward a world of "Post-Elegance Engineering," we face a terrifying debugging nightmare: the Complexity Wall. If a team of agents builds a 100,000-line system that functions today, what happens when it fails tomorrow in a way the agents cannot self-repair? We risk creating "digital black boxes", systems that are functionally correct but cognitively impenetrable. Humans generally dislike working in environments where they lack "conceptual ownership". If we cannot navigate the code, we cannot truly trust it. The psychological toll of maintaining a system one does not understand is a variable we haven't yet factored into the future of work. We don't yet know if the efficiency of automated generation will be eventually canceled out by the sheer cognitive load of human oversight.

### The Economics of the Agentic Employee
To put the Anthropic experiment in a soustenability perspective, consider the cost [2]. Building a functional C compiler for $20,000 in two weeks is an incredible feat of efficiency when compared to traditional labor.

In 2026, a mid-level software engineer carries a total compensation package of roughly $150,000 to $400,000 when factoring in benefits and corporate overhead. A junior engineer might cost $90,000. If an AI agent burns $1,000 a day in API credits, it is roughly equivalent to the gross salary of a single full-time employee, but with zero "hidden" costs like healthcare, office space, or management latency. Crucially, the agent doesn't sleep; it provides the output of an entire 16-person "team" for the price of one human specialist. We are no longer just buying a tool; we are leasing a workforce.
*Continue reading:*

- *Part 2: [Formal Verification and the Path to Machine Discovery]({% link _posts/2026-02-07-extrapolation-interpolation_p2.md %}) - examining mathematical proof systems and machine extrapolation*
- *Part 3: [Interpolation, Extrapolation, and What Exams Really Measure]({% link _posts/2026-02-07-extrapolation-interpolation_p3.md %}) - the fundamental distinction and what it means for education*

# References:

1. [strongDM](https://factory.strongdm.ai/), [Wayback](https://web.archive.org/web/20260207182116/https://factory.strongdm.ai/)
2. [Simon Willison critic on StrongDM](https://simonwillison.net/2026/Feb/7/software-factory/), [Wayback](https://web.archive.org/web/20260207155128/https://simonwillison.net/2026/Feb/7/software-factory/)
3. [Agents](https://www.anthropic.com/engineering/building-effective-agents), [Wayback](https://web.archive.org/web/20260122170652/https://www.anthropic.com/engineering/building-effective-agents)
4. [Skills](https://code.claude.com/docs/en/skills), [Wayback](https://web.archive.org/web/20260207050926/https://code.claude.com/docs/en/skills)
5. [Model Context Protocol Specification](https://modelcontextprotocol.io/), [Wayback](https://archive.is/oT9GA)
6. [Anthropic C Compiler using Agents](https://www.anthropic.com/engineering/building-c-compiler), [Wayback](https://web.archive.org/web/20260207021716/https://www.anthropic.com/engineering/building-c-compiler)