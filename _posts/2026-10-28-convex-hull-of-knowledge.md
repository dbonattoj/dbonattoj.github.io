---
layout: post
title: The Convex Hull of Knowledge - Scientific Discovery in the Age of LLMs
date: 2026-10-28 10:00:00
description: LLMs make solutions cheap, but not the choice of which problem is worth solving. A reflection on the convex hull hypothesis, counterexamples, mathematics, and what happens to attribution when a shared model learns from every scientist.
tags: llm mathematics
categories: llm mathematics
---

_This article extends the series on [interpolation and extrapolation]({% link _posts/2026-02-07-extrapolation-interpolation_p3.md %}), with a focus on scientific research._

There is a distinction I keep returning to: solving a problem is not the same as discovering which problem is worth solving.

LLMs can now produce proofs, develop algorithms and write scientific software that would have required substantial human effort not long ago. Some systems even produce results that challenge established beliefs in mathematics and theoretical computer science. So what happens when the cost of a solution falls much faster than our ability to decide which solutions matter?

I have run into this in my own work. LLMs implemented ideas I had considered but never had time to pursue, and turned mathematical intuitions into formal frameworks in hours instead of months. Yet when I ask the same models for genuinely different ways of thinking about a problem, I have to steer them away from the familiar approach again and again. They are very good at executing difficult intellectual work, and not so good at choosing where to go.

## The convex hull hypothesis

Picture the space of scientific ideas. Every theorem, physical model, algorithm and framework sits somewhere in it. Some ideas are close to each other, others are far apart. New ideas come from old ones, by generalization, by unexpected connections, or by dropping the assumptions that organized the previous landscape.

Now take an LLM trained on a large fraction of humanity's written output. It has seen more arguments, papers and explanations than anyone could read in a lifetime, and it can combine patterns from areas that rarely meet in a single person's head. Its output can therefore be surprising to a human without being novel relative to existing knowledge.

This is what I call the _convex hull hypothesis_: a model mostly generates ideas inside, or close to, the region spanned by its training data, even when these ideas lie outside the experience of the person asking. It is the same picture as in [Part 3]({% link _posts/2026-02-07-extrapolation-interpolation_p3.md %}), where exams sample within the convex hull of what students have seen, and [Part 2]({% link _posts/2026-02-07-extrapolation-interpolation_p2.md %}), where I argued that LLMs remain interpolators over a very large corpus.

The geometry is only a metaphor. A convex hull depends on how ideas are represented, and nothing says that LLM outputs are confined to such a region. Models generalize, and they may produce things that were never explicitly in their data. Recombination is not a lack of creativity either: many discoveries are connections between existing concepts. The hypothesis is useful because it separates three things that are often conflated:

- an idea can be new to an individual without being new to a field;
- it can be new to a field without changing its foundations;
- it can change how a whole class of problems is formulated.

These are different achievements. They loosely match the distinction Boden makes between combinational, exploratory and transformational creativity [1]. Breadth of knowledge gives the first one almost for free. The third requires recognizing that the landscape itself is inadequate, which is what Kuhn described as an anomaly forcing a change of paradigm [2].

## The gravitational pull of the known

In my experience, models need persistent steering to leave familiar approaches. This is not hallucination. The answer can be correct, coherent and well argued, and still miss the task: it solves the problem with the standard method when I asked for an alternative, it proposes a "new" framework that is an existing theory in disguise, or it gives ten ideas that look different but share the same assumptions. The failure is subtle because it looks like progress.

Asked to be creative, a model produces something unusual. Asked to be actually novel, I have to challenge its assumptions and reject its first proposals, several times. This is consistent with the convex hull picture, but does not prove it. Training data, training objectives, and the preference for plausible continuations over uncertain departures could all play a role. I do not need to know which one for it to matter when using these systems for research.

Humans have the same problem. Communities develop fashions and preferred methods, and research programs stay trapped in a framework long after its limits are visible. But a scientist who notices that every proposed solution relies on the same questionable assumption can change the problem itself. The contribution is not another solution, it is the realization that all of them answer the wrong question. This is why I think scientific AI should be evaluated not only on solving problems, but on recognizing when its current approach is insufficient.

## Two examples from my research

### From an idea to an implementation

In October 2024, I wrote about [function hashing in Unison]({% link _posts/2024-10-18-Unison.md %}): a function is identified by a hash of its implementation and parameters, so as long as these are unchanged, its identity is too. I thought it could be applied to Python, Rust or C++, with consequences for incremental builds, version compatibility, distributed execution and dynamic updates. I even explored the Python source code, and concluded that I did not have the time.

Recently I came back to it with LLMs. About four hours later, the implementation was working on CPython, PyPy and GraalPy, the PEP was ready to submit, and ten read-only demonstrations against the patched interpreter behaved as intended.

The direction had already been set: I had found the idea in Unison, understood what it could mean, and wanted it for Python. The model only collapsed the time between the direction and a working implementation. Could an LLM have found this application alone, given the Unison documentation and the Python source? Perhaps. But executing the plan once I supplied it does not show that it would have picked this plan.

### From an intuition to a formalism

While preparing a research grant, we already had experimental results and a strong intuition that a certain mathematical formulation would work. Making it complete and rigorous was estimated at six months, and it appeared as such in the Gantt chart. With LLMs, about twelve hours were enough to lay down its foundations.

It is not a finished theory, and the project will certainly raise new questions. But the formalism can now evolve with the research instead of delaying it by six months. Those months go elsewhere: more questions, more experimental validation, a more ambitious project for the same budget. Again, the experiments and the intuition provided the structure, and the model made it explicit.

Neither example shows that LLMs can find the next big idea. They show that the distance between a promising direction and something technically usable can shrink a lot. Research proposals are limited by the time needed to turn ideas into methods, proofs and validated tools. If this time drops, we can fit more into the same project, but we still have to decide which additional questions are worth asking, which formal results are really needed, and where more rigor could change the conclusions.

## The overlooked art of counterexamples

Mathematics has a large repertoire for constructing proofs: strategies are taught, formal systems exist, and tools check that an argument follows from its assumptions. Finding counterexamples gets much less systematic treatment, although Lakatos built a whole philosophy of mathematics around it [3].

A statement holds on many examples. We can try to prove it, or ask when it would fail. The second question calls for another kind of exploration: boundary cases, relaxed assumptions, unusual objects, a hidden condition the statement depends on. The textbook example: "every continuous function is differentiable" sounds plausible if we only think of smooth functions, but $$f(x)=\vert x\vert$$ is continuous and not differentiable at the origin. One counterexample is enough to kill a universal claim.

The same holds for much more complicated structures. A counterexample can show that a conjecture is false, that a theorem needs stronger assumptions, or that a whole family of approaches rests on a wrong premise. It can save years spent on a direction that was dead from the start.

The field is not untouched: SAT and SMT solvers [4], model finders, property-based testing [5] and counterexample-guided synthesis [6] are all about finding failures. What is still missing, I think, are systematic methods for _open-ended_ counterexample search, when the space of structures is huge and the failure is not captured by a predefined test.

This connects to the previous section. If an LLM keeps proposing variations of the same approach, asking for yet another solution is the wrong request. We should ask it to search for a counterexample to the assumptions shared by all these solutions. The model then explores the boundary of the framework, instead of the answers inside it. Generating plausible conjectures and proving them is not enough, we also need cheap ways to discover that they are wrong, and why.

## Solving a problem is not discovering one

Suppose an LLM produces a difficult and correct proof. It would be a mistake to dismiss it because a machine wrote it. But around that proof, someone had to formulate the conjecture, recognize that it mattered, decide which assumptions were reasonable, and, once it was established, understand what it changed. A proof can be a remarkable achievement without answering an important question. Conversely, a question that opens a new direction can be a major contribution before any solution exists.

If an LLM can generate and formally verify thousands of proofs around a conjecture, what becomes scarce is probably not deriving results by hand, but knowing which conjectures deserve attention and which results are surprising.

The boundary is not clean, though. Mathematicians often find the right question while struggling with a theorem, and physicists find theories by working on problems that looked routine. The point is not that humans ask and machines answer. Science is a cycle of choosing questions, attempting solutions, interpreting results and reformulating the questions. Automation changes the cost of some parts of the cycle, and so changes where human effort has the most impact.

## Mathematics in an identity crisis

I think mathematics is approaching a moment of uncertainty about its own future. LLM-based systems now produce proofs of open problems and challenge assumptions that people relied on for years. Some results come with a lot of human guidance, others are presented as more autonomous. Reliability and significance vary, but the pace forces mathematicians to ask what can be automated. I covered an early example in [Part 2]({% link _posts/2026-02-07-extrapolation-interpolation_p2.md %}) with the Lean proofs from Axiom.

A more striking example appeared at the end of October 2026. OpenAI and Anthropic released separate manuscripts claiming subexponential-time algorithms for 3-SAT or related counting problems, which would contradict the Exponential Time Hypothesis (ETH) [7,8,9]. According to OpenAI [14], its system found a natural-language disproof on October 16th, and the result was formalized in Lean the next day. Both the write-up and the Lean proof are public.

What I find as interesting as the result is how it is handled. The verification is led by a group around Impagliazzo, Paturi and Williams, that is, by the people who proposed ETH and who have spent 30 years working with it or against it. All the raw data is to be public, and OpenAI committed to funding a conference to understand the implications. The announcement explicitly asks the community to discuss "verification, access, credit, and the future of research" [14]. These are the same questions I come back to below.

ETH is the conjecture, proposed by Impagliazzo, Paturi and Zane [7], that 3-SAT cannot be solved in subexponential time in the number of variables. It has been used in hundreds of papers to derive conditional hardness results, in graph theory, databases, computational geometry and more [14]. It is **not** the same as $$\mathrm{P}=\mathrm{NP}$$. A subexponential algorithm can still be superpolynomial. What would give $$\mathrm{P}=\mathrm{NP}$$ is a polynomial-time algorithm for 3-SAT: since 3-SAT is NP-complete [10], every problem in NP reduces to it with polynomial overhead. The claims do not provide such an algorithm. They attack a different assumption, but an important one, as many algorithms and lower bounds in theoretical computer science rely on assumptions about the hardness of SAT.

These are extraordinary claims, and not a reason to consider every consequence settled. A formalization in a proof assistant is strong evidence that a formal argument is valid, but the formal statement, its encoding and its relation to the intended problem still have to be checked by people. What matters here is that systems now produce arguments that researchers must take seriously enough to inspect, verify and possibly build upon.

Still, current mathematical LLMs are far from autonomous mathematicians. The user formulates the problem, picks promising directions, challenges unproductive approaches, checks assumptions, and decides whether the argument proves what was intended. Access is also unequal: the best systems depend on expensive subscriptions and large compute, so not every researcher can experiment with them.

It reminds me of programming with GPT-3. The models could already write code and explain algorithms, but serious development meant constant debugging and supervision, because plausible solutions failed in subtle ways. It was enough to see what was coming, not enough to change every developer's workflow. That changed with the agents I described in [Part 1]({% link _posts/2026-02-07-extrapolation-interpolation_p1.md %}). Mathematics may be at the GPT-3 stage: a model that occasionally produces a remarkable proof is not a model you can trust to develop an entire theory. A reliable research instrument must sustain long chains of reasoning, notice when its assumptions fail, tell a valid proof from a convincing-looking one, and remain useful away from familiar territory.

So the technology is good enough to challenge the identity of a profession, but not good enough to hand the work over. If it reaches the reliability that the best coding models have today, at a price ordinary researchers can pay, mathematicians may start to treat it as a collaborator for exploring entire landscapes: examples, unexpected structures, conjectures, counterexamples, and finally a formal theory built from what survives. People would still need to recognize which patterns are meaningful, which abstractions are useful, and which questions should organize a research program. But the theories within reach of a single researcher could expand a lot, closer to a collective renaissance than a return of the lone genius.

This is a possibility, not a prediction. Verification may stay expensive, the best systems may stay out of reach, the successes may be less general than they look, and a flood of results brings its own problem: a literature that grows faster than anyone can read it. I still find it hard to imagine mathematics unchanged.

## Mathematicians, physicists, and the meaning of a result

The impact will differ across disciplines, because they do not give the same role to formal results.

For a mathematician, proving a theorem can be the achievement. But choosing definitions, developing conjectures and finding abstractions are just as central, so automated proving changes both the execution and the economics of choosing what to pursue.

For a physicist, a correct derivation is not a discovery. A model can be elegant and consistent and still not describe the world, or rely on an approximation that is wrong for the phenomenon. The hard questions are which degrees of freedom matter, which idealizations are justified, which observations would separate two models, and which mathematical structure corresponds to something real. None of this reduces to the internal correctness of a derivation.

Neither discipline is immune, both involve conceptual innovation. But the same proof can be the main result in one setting, a tool in another, and a minor step toward a larger discovery in a third. This is also why benchmarks that only measure correct answers are not enough: they say little about identifying significant problems or changing the framework in which they are posed.

## The economics of scientific work

Calculators made arithmetic cheap, compilers removed the need to translate every instruction by hand. Neither eliminated numerical reasoning or software engineering, they changed the level at which expertise applies. LLMs may do the same to research, with two differences: they cover tasks that used to take a large share of intellectual labor, and their outputs are not always reliable (I discussed the stochastic part in [Part 3]({% link _posts/2026-02-07-extrapolation-interpolation_p3.md %})).

I see three shifts:

1. **Execution becomes less scarce.** Deriving, implementing a known algorithm or exploring a familiar family of models takes less human time.
2. **Evaluation becomes more important.** Many generated results require detecting errors and hidden assumptions, and separating discoveries from correct but unimportant outputs.
3. **Direction becomes more valuable.** Someone has to decide which problems matter and which results justify changing course.

If six months of formalization shrink to a day, the grant does not get shorter, the months go to other work. If a promising software idea costs hours, more ideas become worth trying. And the bottleneck moves: from hundreds of candidate proofs to choosing conjectures, from candidate physical models to designing the experiment that separates them, from cheap scientific software to knowing what it should measure and how to interpret it.

None of this is guaranteed. If AI systems become able to identify important questions, judge their significance and design the next experiments, the boundary moves again. Nothing says problem formulation will stay human. The question is not whether humans keep a monopoly on creativity, but which contributions remain scarce as automation advances. I expect expertise to mean navigating the whole process: recognizing meaningful problems, using automated systems well, judging their output, and knowing when a result changes how a field should think. It is the same argument as in [Part 1]({% link _posts/2026-02-07-extrapolation-interpolation_p1.md %}) about designing the harness, and it echoes the idea in [the exam article]({% link _posts/2026-02-27-mindmap_exam.md %}) that computation is derivative of insight. When computation gets cheap, identifying the structure of the problem is worth more.

## What if the model learned from every scientist?

Most interactions with an LLM do not change the model for everyone else. A researcher may find a better way to formulate a problem, identify a recurring failure, or learn how to get a model out of a familiar pattern. Unless this is captured somewhere, it stays local, and the next researcher spends the same time rediscovering it.

Now imagine a model that learns continuously from the scientific community. One researcher finds a strategy that makes a class of proofs easier, another spots a blind spot in a physical model, a third finds a way to detect when several solutions share a hidden assumption. These contributions are validated, distilled and incorporated into a shared model. The next researcher starts from a better place.

We already accumulate knowledge through papers, books, lectures and databases. A continuously learning model could also accumulate part of the methods, heuristics and habits behind the results. A system that retrieves more papers is a better library. A system whose reasoning improves through its users' contributions is a better instrument. The goal is not more facts, it is better abstractions, better challenges to assumptions, and a better sense of when familiar methods have reached their limit.

This does not mean updating the weights after every conversation. It means a reliable process through which validated contributions progressively change the model, and that is hard. Indiscriminate learning absorbs incorrect results, reinforces dominant fashions, and forgets earlier capabilities [11]. A flawed idea embedded in a shared model is inherited by everyone. We would need validation, versioning, provenance, uncertainty, and a way to keep ideas as hypotheses until they are tested (see also the continual learning discussion in [12]).

There is a deeper risk. If everybody uses the same model and its dominant ways of reasoning become the default starting point, we build a mechanism for collective conformity. Scientific communities already have correlated blind spots, because we read the same papers and use the same methods. A shared model could amplify them, becoming better at solving problems while less able to explore directions that conflict with its own structure. That would reinforce exactly the behavior that motivated this article, the pull of the known. Breakthroughs often start as departures that are hard to validate and look implausible at first.

More data or more confidence does not fix this. We need to preserve disagreement and alternative representations: perhaps competing models evolving in parallel, perhaps a way to test a new idea against the established model without merging it, perhaps keeping the history of rejected hypotheses so that ideas dismissed under old assumptions can be revisited. Collective intelligence should not mean a single way of thinking.

### Who made the discovery?

Consider a researcher who spends months developing a method that lets a model solve a class of previously inaccessible problems, and the method ends up in the shared model. A second researcher, who never met the first, uses the improved model to prove a theorem. A third sees that the theorem matters for a physical theory and opens a new line of investigation. The first contributed the method, the second the result, the third the significance, the developers the infrastructure, and earlier researchers the knowledge the model learned from.

Our conventions for attribution were built around identifiable outputs: papers, theorems, experiments, teams. They fit poorly when the capabilities of a shared model are modified continuously by its users. We may need to distinguish between discovering a result, developing a method that makes discoveries possible, improving the shared model, and interpreting what was found.

The problem of distributed credit is not new. Instrument builders, software engineers and database curators have always enabled discoveries made by others, and Merton described how credit already concentrates on the already-recognized [13]. What changes is how pervasive it could become: a scientist could enable thousands of discoveries without appearing in any of the papers, and another could publish a result whose originality depends on a capability someone else added to the model. If contributions to the shared model go unrecognized, there is little incentive to improve it. If everyone who contributed must be credited, attribution becomes impractical. And if the model changes continuously, reconstructing the lineage of a result requires that the system records its own development carefully. We probably need a richer notion of scientific contribution, one that counts methods, tools and shared capabilities, not only results.

## What should we teach scientists?

It is tempting to conclude that students should spend less time on calculations, code and formal proofs, if these are automated. I think this is wrong, for the reasons given in [Part 3]({% link _posts/2026-02-07-extrapolation-interpolation_p3.md %}): to see that a model uses an inappropriate method you must know the method, to find a hidden assumption you must know what it does, and to judge whether a theorem is meaningful you must understand the structure it sits in. Guiding an automated system requires enough expertise to notice when it is doing the wrong thing.

Education should also go beyond reproducing methods. In the [knowledge graph]({% link _posts/2025-12-28-knowledge-graph.md %}) and [mind map]({% link _posts/2026-02-27-mindmap_exam.md %}) articles, I argued that understanding is a connected structure and not a pile of facts. Research needs one more step: seeing when that structure is inadequate. Students need to learn to identify which assumptions deserve to be questioned, which results would change our understanding, and how to explore when there is no established procedure. This guarantees no permanent human advantage, but it lets researchers take part in a process whose capabilities change quickly. And if models learn from researchers, the quality of the collective intelligence we build depends on the quality of the people who challenge it.

## Beyond the convex hull

The convex hull hypothesis is a useful starting point for thinking about LLM creativity. A model produces surprising and useful ideas because it has access to far more knowledge than any individual, but combining existing ideas does not show an ability to see the limits of the frameworks they come from. Current models can be very capable and still need guidance to leave familiar approaches, while the practical effect is already large: an implementation becomes feasible in hours, a formalism that should take months gets its foundations in a day. Making an idea easier to realize does not make it easier to find.

I do not think the limits are permanent, nor that every impressive demonstration is a lasting breakthrough. We need to separate what models do today, what has been independently verified, and what may come as reliability improves. Mathematics may feel it first. And the most interesting development may not be a model that proves harder theorems alone, but a scientific system that improves through the work of its users, learning not only results but better ways to approach problems. It would make exploring established directions cheaper and spread methods across the community, and would force us to rethink attribution, incentives, validation and the risk of conformity.

The question is not whether humans or machines are more creative. It is how discovery changes when answers are cheap, when capabilities can be shared through an evolving model, and when the line between individual contribution and collective capability gets hard to draw. Some of the most important contributions may not be the theorems or the models, but the ideas that change what a whole community is able to discover.

## Additional notes:

### On the claims about ETH

I have not verified the arguments in the manuscripts [8,9], and I do not have the expertise to do so. The OpenAI announcement [14] says the result was checked in Lean, but as discussed above, a Lean proof only shows that the formal statement is proved, not that it says what we intend. That is precisely what the group led by Impagliazzo, Paturi and Williams is meant to examine. I could only read the OpenAI announcement, not the Anthropic manuscript, so what I say about that one rests on its description. Until independent checking is done, everything about ETH here is conditional: these are claims, not established results.

---

_Related articles in this series: [Part 1: The Rise of Autonomous Systems]({% link _posts/2026-02-07-extrapolation-interpolation_p1.md %}), [Part 2: Formal Verification and the Path to Machine Discovery]({% link _posts/2026-02-07-extrapolation-interpolation_p2.md %}), [Part 3: Interpolation, Extrapolation, and What Exams Really Measure]({% link _posts/2026-02-07-extrapolation-interpolation_p3.md %})_

# References:

1. Boden, M. A. (2004). _The Creative Mind: Myths and Mechanisms_ (2nd ed.). Routledge.
2. Kuhn, T. S. (1962). _The Structure of Scientific Revolutions_. University of Chicago Press.
3. Lakatos, I. (1976). _Proofs and Refutations: The Logic of Mathematical Discovery_. Cambridge University Press.
4. de Moura, L., & Bjørner, N. (2008). Z3: An Efficient SMT Solver. In TACAS 2008, LNCS 4963, 337–340. [10.1007/978-3-540-78800-3_24](https://doi.org/10.1007/978-3-540-78800-3_24)
5. Claessen, K., & Hughes, J. (2000). QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs. ICFP 2000, 268–279. [10.1145/351240.351266](https://doi.org/10.1145/351240.351266)
6. Solar-Lezama, A., Tancau, L., Bodík, R., Seshia, S., & Saraswat, V. (2006). Combinatorial Sketching for Finite Programs. ASPLOS 2006, 404–415. [10.1145/1168857.1168907](https://doi.org/10.1145/1168857.1168907)
7. Impagliazzo, R., Paturi, R., & Zane, F. (2001). Which Problems Have Strongly Exponential Complexity? Journal of Computer and System Sciences, 63(4), 512–530. [10.1006/jcss.2001.1774](https://doi.org/10.1006/jcss.2001.1774)
8. [OpenAI manuscript, The Exponential Time Hypothesis is False (October 25, 2026)](https://mathcommunity.github.io/oai-math-revised/papers/The-Exponential-Time-Hypothesis-is-False-October-25-2026/)
9. [Anthropic manuscript, 2610.00577v1](https://hexagonmath.org/2610.00577v1)
10. Cook, S. A. (1971). The Complexity of Theorem-Proving Procedures. STOC 1971, 151–158. [10.1145/800157.805047](https://doi.org/10.1145/800157.805047)
11. Kirkpatrick, J., et al. (2017). Overcoming catastrophic forgetting in neural networks. PNAS, 114(13), 3521–3526. [10.1073/pnas.1611835114](https://doi.org/10.1073/pnas.1611835114)
12. [Continual Learning with RL](https://cameronrwolfe.substack.com/p/rl-continual-learning), [Wayback](https://web.archive.org/web/20260127125419/https://cameronrwolfe.substack.com/p/rl-continual-learning)
13. Merton, R. K. (1968). The Matthew Effect in Science. Science, 159(3810), 56–63. [10.1126/science.159.3810.56](https://doi.org/10.1126/science.159.3810.56)
14. [OpenAI, The Exponential Time Hypothesis is false](https://openai.com/index/building-scientific-understanding-with-academic-communities/)
