---
layout: post
title: Rust Workspaces
date: 2025-01-02 03:05:00
description: An exploration of organizing Rust projects using workspaces, with a practical guide for structuring and managing dependencies.
tags: rust
categories: programming
---

While working on a Rust project involving multiple libraries and applications, I explored Rust workspaces to manage interconnected components. I found the process somewhat unintuitive and poorly documented, especially when it came to importing libraries into applications. To streamline future efforts, I’ve summarized the steps I followed here.

### Why Use Workspaces?  

For small projects, a single binary or library is sufficient, created with a simple command like:  
```bash  
cargo new app --bin  
```  
However, for larger projects involving multiple libraries and applications that need to interact with each other, Rust workspaces provide a convenient way to organize the structure.  

### Workspace Structure  

Here’s an example structure I used for my project:  
```css
.  
├── Cargo.lock  
├── Cargo.toml  
├── app/  
│   ├── app1/  
│   │   ├── Cargo.lock  
│   │   ├── Cargo.toml  
│   │   └── src/  
│   │       └── main.rs  
│   ├── app2/  
│   │   ├── Cargo.lock  
│   │   ├── Cargo.toml  
│   │   └── src/  
│       └── main.rs  
├── lib/  
│   ├── lib1/  
│   │   ├── Cargo.lock  
│   │   ├── Cargo.toml  
│   │   └── src/  
│   │       └── lib.rs  
│   ├── lib2/  
│   │   ├── Cargo.lock  
│   │   ├── Cargo.toml  
│   │   └── src/  
│       └── lib.rs  
└── tests/  
    ├── some-integration-tests.rs  
    └── multi-file-test/  
        ├── main.rs  
        └── test_module.rs  
```  

### Setting Up a Workspace  

1. **Create the Workspace Root**  

   Start with an empty directory containing a `Cargo.toml` file:  
   ```toml  
   [workspace]  
   members = []  
   ```  

   It would be nice to have a `cargo new --workspace workspaceName` command, but apparently, it is [not implemented](https://github.com/rust-lang/cargo/issues/8365).

2. **Create Applications and Libraries**  

   In the same folder, run the following commands to create your applications and libraries:  
   ```bash  
   cargo new app/app1 --vcs none --bin  
   cargo new app/app2 --vcs none --bin  
   cargo new lib/lib1 --vcs none --lib  
   cargo new lib/lib2 --vcs none --lib  
   ```  
   The `--vcs none` flag prevents each subproject from initializing its own Git repository.  

   These commands will automatically update the `members` section in the workspace’s `./Cargo.toml` file, located in the root directory. The resulting file should look like this:  
   ```toml  
   [workspace]  
   members = ["app/app1", "app/app2", "lib/lib1", "lib/lib2"]  
   ```  

3. **Adding Dependencies in the Workspace**  

   To make library dependencies available to all applications, add them to the workspace's `./Cargo.toml`:  
   ```toml
   [workspace.dependencies]
   lib1 = { path = "lib/lib1" }
   lib2 = { path = "lib/lib2" }
   ```

### Adding Dependencies  

To use `lib1` in `app1`, add it as a dependency in `./app/app1/Cargo.toml`:  
```toml  
[dependencies]
lib1 = { workspace = true }
```  

Then, in `./app/app1/src/main.rs`, you can reference it like this:  
```rust  
use lib1;  

fn main() {  
    println!("Hello, world!");  
    println!("{}", lib1::add(1, 2));  
}  
```

### Building and Running  

To build the entire workspace, use:  
```bash  
cargo build  
```  

To execute a specific application (e.g., `app1`):  
```bash  
cargo run --bin app1  
```  

By following this structure, you can effectively manage complex Rust projects while maintaining a clear organization of your codebase.