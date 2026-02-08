---
layout: post
title: Interpolation, Extrapolation, and What Exams Really Measure
date: 2026-02-07 16:30:00
description: The distinction between pattern recognition and genuine discovery, and why understanding this gap matters for both students and machines.
tags: teaching llm
categories: teaching llm
---

*This is Part 3 of a series on AI, education, and expertise. See also: [Part 1: The Rise of Autonomous Systems]({% link _posts/2026-02-07-extrapolation-interpolation_p1.md %}) and [Part 2: Formal Verification and the Path to Machine Discovery]({% link _posts/2026-02-07-extrapolation-interpolation_p2.md %})*

There's a distinction I keep returning to when I think about what exams measure and what research demands. The simplest way I've found to express it is this: *most exams reward interpolation. Research, in contrast, is extrapolation*.

I realize this sounds like a neat formula, the kind that fits well in a tweet but collapses under scrutiny. And yet, the more I think about it, especially now, as large language models reshape how we write code, organize knowledge, and approach problems, the more this distinction feels very accurate.

## The Interpolation-Extrapolation Distinction

Consider how exam preparation works. Students train on a finite set of exercises, examples, and problem types. The exam samples from roughly the same distribution. Questions may be disguised, combined, or slightly perturbed, but they remain, in a statistical sense, within the convex hull of what has already been seen. Success requires recognizing patterns, mapping them to known solutions, and executing reliably.

This is not inherently bad. Interpolation is a real skill. It reflects domain mastery, technical fluency, and the ability to apply known ideas consistently. These matter. But we should be honest about what exams measure, and what they do not.

Research asks a different question. Not "have you seen something like this before?" but "what happens outside what we currently understand?" The goal is not to recombine known patterns, but to push beyond them: to ask questions that were not part of the training set, to explore regimes where existing tools break down, and to build new concepts when old ones no longer suffice.

And yet, something important happens during exam preparation that I think we often overlook. When students work through exercises, they're not just memorizing solutions, they're building an internal structure, a way of seeing patterns, a repertoire of moves. This repertoire becomes the foundation for extrapolation. You cannot extrapolate from nothing. The ability to venture beyond known territory requires first having stable ground to stand on, a rich enough internal model that you can recognize when something is genuinely new versus merely unfamiliar.

In this sense, the interpolation skills developed through exams are not opposed to extrapolation, they're prerequisite to it. The student who has deeply internalized enough examples, who has practiced recognizing structure across varied problems, is better equipped to notice when a problem falls outside the known space and requires something different. Mastery of interpolation, paradoxically, is what makes extrapolation possible.

## Why Human Extrapolation Still Matters

In [Part 1]({% link _posts/2026-02-07-extrapolation-interpolation_p1.md %}), I argued that human expertise is shifting upward: toward designing the harness, not just writing the code. In [Part 2]({% link _posts/2026-02-07-extrapolation-interpolation_p2.md %}), I showed how formal verification systems like Lean provide constraints that might make extrapolation mechanically checkable. But there's a deeper point I want to make explicit here: we cannot design good harnesses, or ask the right questions of formal systems, without becoming extrapolators ourselves.

This matters for a reason that's easy to miss. When an LLM hallucinates, when it produces plausible but incorrect output, the failure often looks like success. The syntax is correct. The explanation sounds reasonable. The structure mimics what a real solution would look like. Detecting this kind of failure requires exactly the skill that exams, are meant to cultivate: the ability to recognize when something has stepped outside the valid space.

Even with formal verification, the problem doesn't disappear, it transforms. Lean can tell you whether a proof is logically valid, but it cannot tell you whether you proved the right theorem. It cannot tell you whether your formalization captured the actual problem you cared about. That judgment requires deep understanding of the domain, the kind that comes from years of working through examples, building intuition, and learning to see when something is subtly wrong.

The Anthropic compiler experiment demonstrates this precisely. The success came not from better prompts but from carefully designed tests, reference oracles, and feedback loops that could detect when the system was fooling itself. Someone had to design those constraints. Someone had to know what correctness meant in that context. That someone needed to understand compilers well enough to recognize failure modes, edge cases, and the difference between "works on this input" and "works in general".

This is why studying remains essential, not despite the rise of capable AI systems, but because of it. The art is shifting toward asking the right questions, yes, but formulating good questions requires knowledge of how things work. You cannot ask whether a compiler correctly handles type inference if you don't understand what type inference is. You cannot verify a mathematical proof if you don't know what the theorem means. The burden of verification intensifies, and verification demands expertise.

Skills such as: Algorithmic thinking, mathematical reasoning, abstraction, and the ability to hold multiple interacting constraints in mind are the things that need to be cultivated. We should guide students to reason without scaffolding, to operate when the path is not spelled out, and to notice when something is missing or inconsistent. These are the same skills required to guide, question, and correct LLMs rather than blindly trust them.

As this trend continues, the scarce skill won't be typing programs but deciding what should be built, why it should work, and how to tell whether it actually does.

Exams are often criticized as artificial, stressful, or disconnected from real-world practice. Some of that criticism is justified. But exams do something I find extremely valuable: they build skills.

A well-designed exam doesn't primarily test whether a student remembers a formula. It tests whether they can recognize structure, choose an approach, reason under constraints, and adapt known ideas to a new situation. In other words, it tests controlled extrapolation. Not full research-level discovery, but the ability to go beyond rote interpolation while remaining within a well-defined space.

This matters even more today than a decade ago, I think.

The interpolative skills they build, recognizing structure, reasoning under constraints, building mental repertoires, are precisely what enable extrapolation. You cannot venture beyond the map without first learning to read it. The students who develop deep interpolative mastery, who internalize enough examples to see patterns across problems, are the ones who will recognize when they've stepped outside known territory and need to think differently.

That recognition, that capacity to distinguish familiar from genuinely novel, is itself a form of extrapolation. And it begins with disciplined study, with well-designed exams, with the hard work of building internal structure.

That's not a threat to education. It's a reminder of what education has always been for.

## Should We Still Teach Programming?

LLMs extrapolators do not mean programming becomes irrelevant. Quite the opposite.

Programming remains a crucial epistemic tool. When studying a theoretical concept, the ability to simulate it, plot it, stress-test it, or explore edge cases computationally is invaluable. Writing small programs forces precision. It exposes hidden assumptions. It turns vague understanding into something concrete and falsifiable.

Even if future software production relies heavily on automated agents, programming will still play the same role that experiments play in physics or diagrams play in mathematics: a way to think, not just a way to deliver a product.

The skill shift isn't from programming to theory, but from programming-as-output to programming-as-understanding. Exams, theory-heavy courses, and exploratory coding all point in the same direction: training minds that can reason, validate, and guide intelligent tools rather than compete with them.

If LLMs are becoming powerful extrapolators in constrained formal environments like Lean, then education must focus even more on something different but complementary: producing humans who can extrapolate in messy, undefined spaces where formal systems don't yet exist.

That includes recognizing which problems need formalization, crafting the right constraints, and building the harnesses that make machine extrapolation possible. These are not mechanical tasks. They require judgment, taste, and deep theoretical understanding, qualities that cannot be outsourced to automation without first being supplied by humans.

## The Paradox of Learning to Code in an Agentic World

I want to address something I find genuinely difficult about the world we're entering, something that affects students and newcomers more than experienced practitioners.

If you're learning to program today, you face what looks like an exercise in futility. Every coding task you struggle with, an LLM can solve faster and often better. Why spend hours debugging when an agent can iterate through solutions in minutes? Why learn algorithms when the machine has seen millions of implementations? The psychological barrier is real: it's hard to persist in learning a skill when you're constantly reminded that a machine outperforms you.

And yet, this framing misses what programming actually does for you as a learner.

When you write code to explore an idea, to test whether an algorithm behaves as you expect, to visualize a dataset, to simulate a system, you're not competing with agents. You're building the mental structures that make it possible to interrogate them effectively. Programming forces precision in a way that reading or watching cannot. It exposes the gap between "I understand this in principle" and "I can make this work in practice." It surfaces hidden assumptions, edge cases, and conceptual confusions that remain invisible otherwise.

This is exactly the shift I described earlier: from programming-as-output to programming-as-understanding. The goal isn't to produce production code. The goal is to build enough internal structure that you can recognize what questions to ask, what tests to run, what failures to look for. An LLM can generate code, but it cannot tell you which idea is worth exploring. It cannot recognize which result is surprising. It cannot know what you're trying to understand.

In Part 1, I argued that human value is moving upward, toward theory, specification, and reasoning about correctness. But you cannot reason about correctness without having struggled with incorrectness. You cannot design good specifications without having built broken systems. The process of learning to code, especially when it's hard, especially when you fail repeatedly, builds exactly the judgment needed to work effectively with autonomous systems.

This mirrors something I see in mathematics. Formal proof assistants like Lean can verify theorems, but mathematicians still work through proofs by hand, still struggle with examples, still build intuition through failure. Not because the manual work produces better proofs, but because the process of doing it builds the understanding needed to know what to prove and how to recognize when a result is meaningful.

So to newcomers facing this apparent paradox: yes, the machine codes better than you. That's not the point. The point is that learning to code, especially learning through struggle and failure, builds the conceptual scaffolding that will let you see what the machine cannot: which problems matter, which solutions are elegant, which failures are informative, and which successes are accidental.

That understanding cannot be outsourced. It has to be built, one failed program at a time.

## The Evolution of Trust and Verification

There's a pattern here worth noting. Every time we automate a skill, we don't make that skill obsolete, we make the meta-skill of understanding and judging it more valuable. Calculators didn't make arithmetic irrelevant; they made numerical reasoning more important. Compilers didn't make understanding code irrelevant; they made understanding abstractions essential.

But there's a crucial difference with LLMs that changes the nature of this pattern. Calculators and compilers are deterministic machines. We trust them precisely because they produce the same output every time, because their behavior is predictable and verifiable. LLMs, even those enhanced with formal systems, remain fundamentally stochastic at their core. The same prompt can yield different answers, some correct, some plausible, some subtly wrong. This introduces a qualitatively different kind of problem: the output can shift between runs, and there's no guarantee of consistency even when formal verification catches logical errors.

So the pattern still holds, but the meta-skill has evolved. With deterministic tools, we learned to trust the tool and focus on formulating the right question. With stochastic tools, even powerful ones, we need something more demanding: the ability to formulate questions, the judgment to evaluate whether the answer is trustworthy, and the theoretical grounding to verify the result independently. The burden of verification doesn't disappear, it intensifies. And this makes rigorous thinking, the kind that distinguishes plausible from correct, more critical than ever.

## Conclusion: What Exams Test in the Age of LLMs

This is what exams, at their best, have always tested: not memory, but judgment. Not reproduction, but recognition. Not what you've seen, but what you can see.

---

*This concludes the series. Return to [Part 1: The Rise of Autonomous Systems]({% link _posts/2026-02-07-extrapolation-interpolation_p1.md %}) or [Part 2: Formal Verification and the Path to Machine Discovery]({% link _posts/2026-02-07-extrapolation-interpolation_p2.md %})*
