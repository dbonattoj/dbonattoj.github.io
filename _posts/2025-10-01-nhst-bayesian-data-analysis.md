---
layout: post
title: NHST vs. Bayesian Data Analysis, and what about machine learning?
date: 2025-10-01 00:30:42
description: A personal view on why Bayesian analysis feels more natural than NHST, and how it connects to machine learning.
tags: statistics, bayesian, nhst, machine-learning
categories: research, methods
---

# Why I Prefer Bayesian Data Analysis Over NHST

I’m by no means a statistician, and what follows reflects only my view. Still, I’ve spent some time wrestling with statistical tools in research to have formed some opinions on why **Null Hypothesis Significance Testing (NHST)** often feels unsatisfying, and why I find **Bayesian data analysis** a better fit for how we actually think about uncertainty.

Most of us were first introduced to NHST in our early stats classes. It goes something like this:

* Assume a null hypothesis.
* Compute a test statistic from your data.
* Get a **p-value**, the probability of observing something as extreme as your result under the null.
* If the p-value is below a magic threshold (often 0.05), you "reject" the null.

It sounds neat and tidy, but the interpretation is tricky. A p-value is *not* the probability that your hypothesis is true. It is not the probability of being wrong. It’s only the probability of seeing your data (or something more extreme) if the null were correct - a subtlety that often leads to confusion.


---

### The Infinite Space of Statistical Tests

Choosing the "right" test is harder than it looks. Imagine the design space:

* Sample size $S$
* Parametric vs. non-parametric assumptions $PNP$
* Distribution families and their parameters $F_p$
* Single or multiple hypotheses $H$
* Dependence structures $D$
* And countless other details $O$

This space

$$
	\Omega = (S, PNP, F_p, H, D, O)
$$

is effectively infinite.

Throughout history, tests were developed as answers to very specific (often industrial) problems: Student’s *t*-test, Fisher’s exact test, Wilcoxon rank-sum, ANOVA... Each of them is just one **point in the infinite space of possible tests**. Some are more useful and general, so they make it into textbooks. The hope is: if you can correctly map your problem to one of these points, you can apply the corresponding test.

But navigating this space is not straightforward. Different textbooks, authors, or software packages organize it differently. One might start with the number of samples, another with distributional assumptions, another with independence. There is no universal decision tree that always lands you on the right test.

---

### The Problem of Rigidity

One challenge in teaching NHST is that we rarely show how to **extend tests**. Suppose you’ve identified the "correct" test - but your problem has a slight twist: maybe the null hypothesis isn’t standard, or one assumption doesn’t quite hold. Do you invent a whole new test? Or can you adapt the existing one? This question is often left unanswered.

In reality, many of our assumptions are hidden or unknown. We might not even realize what we’re assuming about independence, variance, or distributions until things go wrong.

And even when people do their best: A striking demonstration of this problem comes from a recent study in social science [1], where 73 independent research teams analyzed the same dataset to test whether immigration affects support for social policies. Despite identical data, teams’ conclusions ranged from strongly negative to strongly positive effects. The researchers found that the analytical choices themselves explained very little of the variation — most of the differences came from a "hidden universe of uncertainty". This perfectly illustrates how, in NHST, even skilled analysts can reach opposite conclusions because the framework doesn’t make assumptions explicit or robust. Bayesian modeling, by contrast, encourages transparency: priors, likelihoods, and hierarchical structure make the uncertainty visible rather than hidden behind a p-value.

Worse, academic publishing often reinforces rigidity. Papers sometimes get rejected not because the analysis was flawed, but because it didn’t fit into a standard NHST interval or template. A Bayesian analysis may provide clear and valid evidence, yet remain "uninterpretable" to reviewers trained only in p-values.

---

### The Bayesian Alternative

Bayesian data analysis takes a different route. Instead of navigating the infinite map of pre-built tests, you **build a model**. You write down your assumptions explicitly (priors, likelihoods), combine them with your data, and then compute the posterior distribution. From there, you can answer the questions that actually matter: how likely is a parameter to fall in a certain range? What is the probability that one hypothesis is more supported than another?

Mathematically:
$$
p(\theta \mid X) \propto p(X \mid \theta) \, p(\theta)
$$

* $p(\theta)$: your prior, the assumptions you bring.
* $p(X \mid \theta)$: the likelihood, describing how data arise under the model
* $p(\theta \mid X)$: the posterior, what you learn after seeing the data

From the posterior, you can compute directly:

* $\Pr(\theta > 0 \mid X)$, the probability an effect is positive
* Credible intervals for parameters
* Predictions for future data

In this view, inference is not about finding the right test in $\Omega$. It’s about writing down a plausible model and letting Bayes’ theorem do the work. The model *is* the test.

This approach is more flexible. It’s essentially **test-free**. The model is the test. If you can specify it, you can run it. Instead of memorizing dozens of special-purpose procedures, you work in one unified framework. The quality of the results depends on the quality of the model - but at least the assumptions are visible, not hidden.

This is only widely feasible now that we have the computational power to sample from posteriors. For most of the 20th century, NHST made sense as the practical choice. But today, Bayesian methods are gaining traction, even if they’re not yet mainstream. Many good Bayesian papers are still rejected by journals locked into NHST norms - but the field is shifting.

Of course, this doesn’t mean Bayesian inference is truly "test-free". Instead of choosing among a fixed menu of NHST procedures, you’re choosing among an effectively infinite space of models: priors, likelihood forms, hierarchical structures, approximations. Those choices can be just as contentious as picking the "right" statistical test. The key difference is transparency. In Bayesian analysis, assumptions are visible and debatable, rather than hidden inside the machinery of a pre-packaged test.

---

### A Note on Machine Learning

Some might ask: why not just use machine learning (ML) instead? After all, ML also seems test-free. The difference is data regime and goals. In machine learning, we often have massive datasets. The model is "learned" automatically, with fewer explicit assumptions, and optimized for prediction, not interpretability.

Bayesian analysis sits in a different niche: smaller datasets, richer models, and a need for interpretable uncertainty. Instead of black-box predictions, you get probabilities and insights grounded in your domain knowledge.

In some sense, ML lets the data find its own place in (\mathcal{S}), but without making explicit which assumptions are being chosen. Bayesian modeling, by contrast, forces you to declare your assumptions and gives you transparent probabilities rather than opaque predictions.

Do we still need to learn Bayesian Data Analysis, you might ask? My answer is yes - there is still value. If you don’t have enough data to apply machine learning, Bayesian analysis remains one of the most powerful ways to obtain a satisfying result. But even if you never directly apply it because you *do* have enough data, many of the methods that improved deep learning in recent years can be understood as essentially Bayesian ideas in disguise.

Take **fine-tuning** for example: starting from a pre-trained model is nothing more than using a strong prior $p(\theta)$, and then updating it with new data $X_{\text{new}}$ via Bayes’ rule,
$$
p(\theta \mid X_{\text{new}}) \propto p(X_{\text{new}} \mid \theta), p(\theta).
$$
What practitioners call "adapting weights to a new dataset" is simply posterior updating.

Or consider **dropout**: at training time, we randomly mask neurons, which in a Bayesian interpretation corresponds to integrating over a distribution of thinned networks. This can be formalized as an approximation to Bayesian model averaging,
$$
p(y \mid x, X) \approx \tfrac{1}{T} \sum_{t=1}^T p(y \mid x, \theta_t),
$$
where each $\theta_t$ is a sampled subnetwork under dropout.

**Style transfer** can also be read through a Bayesian lens, though here the interpretation is more metaphorical than standard. The process of generating an image $I$ that balances fidelity to a content image $I_c$ with similarity to the distribution of a style image $I_s$ looks like a posterior tradeoff:
$$
p(I \mid I_c, I_s) \propto p(I_c \mid I)^{\alpha} , p(I \mid I_s)^{\beta},
$$
where the exponents $\alpha$ and $\beta$ act like prior strengths. In practice, ML papers frame this as an optimization of loss functions, not as Bayesian inference. Still, the analogy is useful: what looks like a balancing of competing objectives can often be reframed as a Bayesian updating problem.

Even **regularization** in its most basic form has a Bayesian interpretation. For instance, L2 regularization (weight decay) corresponds to placing a Gaussian prior on the parameters,
$$
p(\theta) \propto \exp!\left(-\tfrac{\lambda}{2} |\theta|^2\right).
$$
Training with a penalty is just MAP (maximum a posteriori) estimation.

So, even in a world dominated by machine learning, Bayesian analysis has enduring value: it provides a language and framework that helps us see the hidden logic behind many of the tools we already use.

---

### In the End

NHST has given us a toolbox of powerful, historically useful procedures. But it’s a toolbox built from scattered points in an infinite design space. Bayesian data analysis offers a more direct route: start from your model, combine it with your data, and let inference follow naturally.

It doesn’t eliminate the need for judgment, but it does make the process clearer, more flexible, and - in my view - closer to how science should reason under uncertainty.


# References

[1] [10.1073/pnas.2203150119](https://www.pnas.org/doi/10.1073/pnas.2203150119)