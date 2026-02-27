---
layout: post
title: Evaluating Insight, Not Just Computation
date: 2026-02-27 21:32:10
description: Evaluating a Knowledge Graph, instead of evaluating computations in higher education.
tags: teaching
categories: teaching
---

## What I Actually Want to Measure

When I give an exam, my primary concern is not whether a student can carry out a long computation without mistakes. In machine learning, for example, nobody in industry will be asked to manually differentiate a loss function or expand a matrix derivation on a whiteboard, except perhaps during an interview. What matters, years later, is something more durable: whether they recognize when a problem is about optimization, when it reduces to linear algebra, when regularization is implicitly shaping the hypothesis space, or when a probabilistic interpretation clarifies what a model is actually assuming. The students need to see how optimization, regularization, and probabilistic modeling relate to one another.

In computer graphics, students must understand how linear transformations structure space. In hardware architecture, they must grasp how memory hierarchies and parallelism constraints shape performance. In each case, I am less interested in whether a student can reproduce a long derivation than in whether they understand the structural role a concept plays within a larger system.

In other words, I care less about procedural fluency and more about structural insight. The story would be different if these exams were given at an early bachelor level. But for late bachelor and master students, computations can always be reconstructed. Insight, however, is what allows someone to know which mathematics to reconstruct, and why. It is the difference between remembering formulas and understanding the landscape in which those formulas live.

The issue is not discipline-specific. It concerns the nature of understanding itself, and that has direct consequences for what we choose to test, how we test it, and what we consider evidence of mastery.

## Climbing the Structure of Knowledge

There is a useful metaphor for the progression of knowledge in the so-called DIKW pyramid. At the bottom lies data; above it, information; above that, knowledge; and at the top, wisdom. Traditional evaluation often stabilizes somewhere between information and procedural knowledge: students demonstrate that they can manipulate symbols correctly and reproduce established arguments. That has value. But it does not necessarily move them upward toward structured understanding or sound judgment.

What I am trying to reach, by using [insights-based learning]({% link _posts/2024-12-08-inquiry-based-learning.md %}) (my own version of inquiry-based learning), corresponds to the upper layers of that pyramid. Moving from information to knowledge means not only applying a method, but understanding why it works, under which assumptions, and how it connects to other ideas. Moving toward wisdom, in an academic sense, means being able to reorganize knowledge, detect hidden structures, and evaluate when a framework applies, and when it does not.

This perspective aligns closely with what educational theory calls Higher-Order Thinking Skills (HOTS). HOTS go beyond recall and routine application. They involve analysis, synthesis, abstraction, transfer, and critical evaluation. Many educational reforms, such as inquiry-based science and reform mathematics, explicitly aim to cultivate these abilities, sometimes even reducing emphasis on rote procedures in favor of conceptual exploration. Assessments designed around HOTS typically rely on open-ended questions, justification, and structured reasoning rather than recognition-based formats.

In the context of the DIKW pyramid, HOTS can be seen as the cognitive operations that allow students to climb upward. They transform isolated information into organized knowledge and, occasionally, into principled judgment. My goal is not to eliminate computation, but to situate it within that ascent. Computation belongs to the structure, but it should not define the summit.

The difficulty, of course, is that insight is harder to measure than computation. A derivative is either correct or not. A matrix inversion either works or it fails. But how do we assess whether someone truly sees the connections between ideas?

What I am trying to evaluate lies closer to structural knowledge. It is the ability to organize techniques under unifying principles, to recognize when two results are instances of a broader theorem, or to detect when an assumption silently governs an entire chain of reasoning.

This applies whether we are discussing generalization in learning systems, homogeneous coordinates in graphics, or warp scheduling on GPUs. The domain changes; the epistemic structure does not.

## Exams with Knowledge Graphs

This year, I am experimenting with a different approach. Instead of emphasizing derivations alone or broad concepts and terminology, I ask students to build a comprehensive mind map of the course before the exam and bring it with them.

For example, machine learning is not a linear subject; it is a graph. Loss functions connect to optimization theory. Optimization connects to convexity. Convexity connects to generalization guarantees. Generalization connects to bias–variance trade-offs. Capacity control connects to overfitting. Probabilistic modeling connects to uncertainty quantification. Each concept is a node, and the discipline emerges from the arrows between them.

The assignment is simple in appearance but demanding in practice. Students must identify the main concepts encountered during the semester and represent them as nodes. More importantly, they must draw arrows that encode precise relationships: general theoretical links (what is the link between a Gaussian process and kernel methods? between kernel methods and PCA?), implication, specialization, reformulation, causal influence, equivalence under assumptions, or methodological dependence.

It is at that stage that one can identify missing links, see hidden assumptions, or detect conceptual gaps. Knowledge becomes navigable rather than accumulative.

During the exam, instead of asking them to reproduce a lengthy proof, I may ask them to explain the meaning of a specific arrow (for example, why least squares does not work well for classification, what the link is between least squares and regression, or what the link is between regression and the sigmoid), justify why a connection should exist if it is missing, or argue why two nodes should not be directly connected without additional assumptions. In doing so, I am not grading memory; I am evaluating the structure of their internal graph.

This evaluation echoes my article on how to teach a [graph of knowledge]({% link _posts/2025-12-28-knowledge-graph.md %}) and my version of [inquiry based learning]({% link _posts/2024-12-08-inquiry-based-learning.md %}).

## A Built-In Revision Mechanism

I hope that this method also transforms how students study.

If a student postpones the construction of the mind map until the final days before the exam, they are forced to revisit the entire course in compressed form. They must traverse the conceptual terrain repeatedly, checking whether each connection makes sense. That phase is intellectually intense, but it forces them to extract structure from content.

If, instead, they build the map progressively during the year, every new chapter forces them to reintegrate prior knowledge. Each new concept triggers a systematic question: does this modify an existing node? Does it create a new link? Does it contradict a previous assumption? In effect, the method enforces continuous revision without explicitly scheduling it.

Either way, the graph grows denser, and insights are extracted.

## Collective Understanding

There is also a collective dimension. While each student constructs their own map, they can discuss arrows in small groups. Debating whether early stopping is a form of regularization, or whether cross-entropy is simply maximum likelihood in disguise, forces them to articulate mechanisms rather than recite definitions.

The conversation shifts from "how do you solve this exercise?" to "what is the structural role of this concept in the theory?" That shift is precisely what I want. The goal is not isolated correctness, but shared structural understanding.

Building mind maps encourages students to work together, and many minds are often more powerful than an isolated one. I think it also helps refine concepts collectively, learning from one another how to extract meaning from equations.

## Studying in the Age of Automation

We are entering a period in which increasingly autonomous systems can generate derivations (even if they are often incorrect), produce code, and replicate standard arguments. The technical shift toward highly automated systems is real, and trust in computational agents is expanding.

In such a context, the comparative advantage of human learners shifts. If procedural reproduction becomes automated, then structured thinking, the ability to connect, abstract, critique, and reorganize, becomes more central.

Across all the courses I teach, my objective is therefore consistent: I want students to begin forming the internal graph characteristic of expertise. If that graph exists, computations follow as structured consequences. If it does not, computations remain disconnected maneuvers.

## What I Hope Remains

Ultimately, what I want students to leave with is not a collection of formulas, but a structured internal graph. Five years from now, they may not remember the exact algebra behind a support vector machine. But if they understand that it is fundamentally about margin maximization in a high-dimensional feature space, they can reconstruct the details when needed.

Insight functions as compressed knowledge: a small set of organizing ideas from which technical machinery can be regenerated.

## Conclusion

I do not yet know whether this experiment will succeed. Evaluating insight is inherently more subtle than grading computations. But I am convinced that, in a world where calculation is cheap and automation is ubiquitous, education must aim higher in the pyramid.

If students leave not merely with formulas, but with a coherent and densely connected internal representation of the field, then the exam will have achieved its purpose. Computation will not disappear. It will simply be grounded in insight rather than memorization.

# Additional notes:

### Insight and Computation

When I say that computation is not my primary concern, I do not mean that it is unnecessary or that software can replace reasoning. What I mean is more precise: if the insight is present, the computation should follow naturally, even if a book is needed to recall the exact formalism.

If a student truly understands that a problem reduces to an optimization question, then gradients, constraints, or dual formulations are direct consequences. If they understand how a transformation acts on a vector space, then its matrix representation is no longer a memorized artifact but an inevitable encoding. If they understand how architectural constraints affect throughput, then performance formulas become explanatory rather than decorative.

Computation is not dispensable. It is derivative. It unfolds from structure.

Without insight, procedures remain isolated techniques. With insight, they become necessary expressions of a coherent framework.

### Mind Maps and Their Intellectual Lineage

The idea of representing knowledge as a mind map is not new. Tony Buzan popularized mind maps decades ago in highly visual and colorful books that left a lasting impression on many readers. His central intuition was that understanding radiates outward from core ideas and branches associatively rather than unfolding as a rigid outline.

Years ago, I also read Alain Thiry and Fanny Demeulder, who developed structured study methodologies grounded in mind mapping principles. Their work formalizes the process: mind maps are not merely visual summaries but instruments for organizing cognition and reinforcing structural integration.

My approach builds on that tradition, but situates it within technical higher education.


# References:

1. Anderson, L. W., & Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom’s Taxonomy of Educational Objectives.*
2. Brookhart, S. M. (2010). *How to Assess Higher-Order Thinking Skills in Your Classroom.*
3. Buzan, T. (1993). *The Mind Map Book.*
4. Thiry, A., Demeulder, F. (2012). "Ça y est, j'ai compris!".
5. Ackoff, R. L. (1989). *From Data to Wisdom*. Journal of Applied Systems Analysis, 16, 3–9.
6. Zins, C. (2007). *Conceptual Approaches for Defining Data, Information, and Knowledge.* Journal of the American Society for Information Science and Technology, 58(4), 479–493.
7. Prince, M., & Felder, R. (2006). *Inductive Teaching and Learning Methods: Definitions, Comparisons, and Research Bases.* Journal of Engineering Education, 95(2), 123–138.