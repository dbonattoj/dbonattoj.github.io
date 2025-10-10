---
layout: post
title: Strong Types in Scientific Software - Safety and Pitfalls
date: 2025-05-31 21:38:42
description: How rich, domain-specific types in scientific software prevent subtle bugs and clarify logic, but can sometimes introduce hidden inefficiencies.
tags: programming, scientific-software, rust, types, productivity
categories: productivity, software-development, research
---

## Why I Use Rich Types in My Code — Even for Temperature

I’ve seen many interesting posts online about programming with types, especially around the idea of avoiding *naked primitives* like `int`, `float`, or `size_t` for domain-specific values. Instead, we should define real types that carry meaning.

### A Classic Problem

Here’s an example of what can go wrong when everything is just a number:

```rust
fn get_money(an: usize) -> f64 {
    let account = get_account(an);
    account.get_balance()
}

fn get_birthday(un: usize) -> Date {
    let user = get_user(un);
    user.get_birthday()
}

let un: usize = 123456; // user number  
let an: usize = 147258; // account number

get_money(un);    // no compile error!
get_birthday(an); // still compiles!
```

There's no type distinction between a user ID and an account number. Swapping them leads to nonsense, but the compiler can’t help us.

Now let’s add some real types:

```rust
struct UserNumber(usize);
struct AccountNumber(usize);

fn get_money(an: AccountNumber) -> f64 {
    let account = get_account(an);
    account.get_balance()
}

fn get_birthday(un: UserNumber) -> Date {
    let user = get_user(un);
    user.get_birthday()
}

let un = UserNumber(123456);
let an = AccountNumber(147258);

get_money(un);    // compile error!
get_birthday(an); // compile error!
```

Much better. The compiler now guards us from mixing up concepts that don’t belong together.

### Encoding Domain Logic in Types

Strong types don’t just prevent mistakes—they let you encode logic directly. Consider temperature conversion between degrees Celsius and Kelvin:

```rust
struct Kelvin(f64);
struct Degrees(f64);

impl From<Degrees> for Kelvin {
    fn from(d: Degrees) -> Self {
        Kelvin(d.0 + 273.15)
    }
}

impl From<Kelvin> for Degrees {
    fn from(k: Kelvin) -> Self {
        Degrees(k.0 - 273.15)
    }
}

impl Add<Degrees> for Kelvin {
    type Output = Kelvin;

    fn add(self, d: Degrees) -> Kelvin {
        let d_in_k = Kelvin::from(d);
        Kelvin(self.0 + d_in_k.0)
    }
}
```

Now we can write something like:

```rust
fn update_temperature(k: Kelvin) -> Kelvin {
    let delta: Degrees = some_sensor_reading();
    k + delta
}
```

The domain logic is now compiler-enforced. You can’t accidentally add one Kelvin to another and get Degrees, or mix up raw floats. The code becomes safer and easier to reason about.

### When the Cost Shows Up

But this type safety can come with a price. Imagine a loop doing conversions repeatedly:

```rust
let mut d = Degrees(10.0);

for _ in 0..100_000 {
    let k: Kelvin = d.into();
    d = k.into();
}
```

The conversions themselves are trivial in this case, but this pattern could appear in more complex forms. In domains like graphics, robotics, or signal processing, conversions might involve expensive matrix operations, non-linear transforms, or interpolations. If those happen repeatedly inside a tight loop, performance can degrade without obvious symptoms—especially if each type’s logic is abstracted behind constructors or `From` traits.

Types help you write correct code. But they can also hide inefficient behavior if you're not careful.

### When Types Multiply

There’s a subtle but dangerous pattern I’ve encountered in real systems — a kind of *diamond-shaped overload problem*, reminiscent of the classic multiple inheritance issue.

It usually starts with good intentions: someone introduces a new type because it makes certain operations faster, cleaner, or more expressive. For example, a researcher working on large-scale graph computations might use **sparse matrices** — they're ideal for representing structures like adjacency graphs or document-term matrices, where most entries are zero. Later, another part of the codebase needs to feed that data into a deep learning model — which requires **dense tensors**, especially if it's running on a GPU where sparse operations aren’t well supported.

So now, both representations coexist in the code. Each serves a specific set of algorithms well: the sparse matrix unlocks efficient traversal and storage for linear solvers; the dense tensor enables convolutional layers and matrix multiplications to run efficiently on hardware accelerators.

But then someone writes a tool that calls into both modules — maybe running in a loop a preprocessing step optimized for sparse data, followed by a model pass that expects dense input. Suddenly, the data is **silently bouncing back and forth between formats**. What started as two justifiable abstractions begins to trigger a chain of **invisible and expensive conversions**.

A common workaround is to **cache both formats**, converting once and storing the result. But this creates another problem: what if one version is updated? For instance, the dense tensor is normalized or augmented after a model pass — but now the sparse matrix is stale. Keeping both in sync becomes tricky, especially if multiple functions touch different representations in different orders. You can’t just “store both” unless you also **coordinate updates and ownership** — which is a major source of bugs and performance regressions in real-world systems.

Even worse, these issues rarely show up as compiler errors. They creep in as *slowdowns*, inconsistent results, or strange numerical mismatches — and by the time you notice them, the conversion logic is buried under layers of calls.


One might argue this whole problem could be avoided with a solid roadmap and better planning. And in principle, yes — if the software had clearly defined data flow boundaries and strict architectural guidelines, these type collisions wouldn’t occur.

But in practice, **scientific software is rarely built this way**.

Much of the work is exploratory by nature: researchers try out new algorithms, adapt to new data, or prototype pipelines under time pressure. Dozens of contributors might touch the same codebase — each with different goals. One person adds a faster solver. Another integrates a new model. A third tweaks the data loader to support a new format. No one sets out to break the abstraction — but slowly, unintentionally, the code becomes a patchwork of overlapping types and assumptions.

That’s when the silent costs appear.

### In the End

Using expressive, domain-specific types helps encode meaning, prevent bugs, and clarify intent. They serve as a form of documentation the compiler can enforce. And in most applications, the cost is negligible compared to the clarity and safety they offer.

Still, it’s important to be realistic about what they solve. For transparency, using rich types can reduce misuse and verbosity, but they won’t prevent all issues—like factual inaccuracies, incorrect assumptions, or inefficient structure. Just as telling an LLM to write “without fluff” won’t make it factually accurate, adding types won’t guarantee deeper correctness in your system. But both are simple, useful tools that help avoid common pitfalls—and that’s often more than enough to justify them.
