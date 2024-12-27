---
layout: post
title: The Evolution of Scientific Curiosity - From Triangles to Gaussians in Graphics
date: 2024-11-05 21:18:00
description: This opinion piece explores the journey of scientific research, from the persistence of unsolved questions to the rise and fall of fields shaped by innovation and limitations. Using computer graphics as a lens, it examines how triangle-based methods and point-based graphics evolved, the social dynamics of research, and the challenges of balancing theoretical advancements with practical constraints.
tags: GaussianSplatting
categories: publications
---

# Prelude

Science evolves in fascinating and often unexpected ways. Consider this: someone begins with a simple question, perhaps sparked by curiosity - "Why does light behave strangely through this object?" - a playful thought experiment - "What’s the optimal way to cut a cake?" - or a practical need - "I have a list; how can I efficiently order it?"

At first glance, the question seems straightforward. "This should be easy to solve," they think. Hours turn into days, months, or even years, and with persistence, some insights may emerge. If they are a scientist, they publish their findings. Even if no solution is reached, they might write a research article detailing why the problem is more complex than it initially appeared and why others should care about it.

(Much) later, someone else with the right background might solve the problem effortlessly, by inadvertance sometimes. They may not even publish their solution, or they might share it if sufficiently motivated. More often, the problem remains unsolved for a long time. Yet, this does not imply stagnation. Some mathematical problems have taken centuries to resolve. Along the way, new methods are developed, old ones are rediscovered, and the problem is dissected into numerous sub-problems, each analyzed with a diverse set of tools.

Through this process, insights accumulate - not just for individuals but for the entire scientific community working within the field. Even if the original question remains unresolved, the collective understanding deepens. From a researcher's perspective, or that of a science journalist, this process might appear to generate a flood of minor papers that seem like noise around the central question. However, this 'noise' is crucial, as it facilitates exploration and allows meaningful trends to emerge.

But what exactly constitutes a "field" of scientists? Broadly speaking, it is a community of researchers working on the same subject, striving to develop a shared understanding of their discipline’s "important problems." It is crucial to note, however, that the definition of "important" evolves over time, often shaped by shifting priorities or trends within the field. Research is inherently a social endeavor; a charismatic scientist can steer focus toward new directions through sheer influence, while equally significant contributions from less prominent researchers may remain overlooked.

In an ideal world, the social dynamics of science would be absent, enabling progress to focus solely on genuinely important problems and reducing noise. Yet, without the social aspect, how would we even begin to define what is important? And without the noise, how would the emergence of trends become visible?

Another aspect of scientific research is that a problem may gain prominence in a community as more researchers recognize its significance, only to fade into relative obscurity a decade later once solutions are found and its relevance diminishes.

# Triangle-based Geometry

One successful and interesting field of science is Computer graphics. For a long time, computer graphics have revolved around the use of triangles as fundamental primitives, with significant research dedicated to manipulating these geometric shapes. GPUs were initially designed to handle triangles with maximum efficiency, inspiring the creation of algorithms to compute lighting on triangular meshes [1]. This foundation gave rise to modern computer graphics, where triangles dominated everything from game development [2] to rendering pipelines [3-5]. This focus also led to the development of discrete differential geometry [6], which studies continuous mathematical functions defined over discrete meshes. This field enabled more advanced manipulations of triangles, laying the groundwork for software like Blender [7], where users can paint, deform, and compute integrals and divergences on triangle-based meshes.


However, triangles alone often fail to produce photorealistic results. While they can approximate reality in some cases, they frequently betray the artificial nature of a virtual scene. To address this, a parallel line of research emerged, focusing on ray tracing [8] - a method that still uses triangles to represent scenes but prioritizes simulating the behavior of light. Ray tracing involves tracing light rays from the screen, calculating their intersections with objects, and accounting for effects such as reflection and refraction. When a ray intersects with a light source, the light's influence is propagated backward along the ray’s path, following physics-based equations. This process, while producing highly realistic results, is computationally expensive, as every ray must be calculated individually, and each interaction with an object can spawn additional rays.

One key advantage of triangle-based methods is their ability to associate materials with meshes. This allows ray tracing to simulate complex interactions, such as light refracting through glass. Rays passing through transparent materials interact with objects behind them, propagating color and light properties to the transparent surface, resulting in strikingly realistic visuals. Without ray tracing, such effects are nearly impossible to replicate accurately, which underscores why this method yields superior graphical results.

Fortunately, recent advancements in GPU technology have incorporated ray tracing primitives and optimized hardware for faster intersection calculations [9]. These innovations have made real-time ray-traced rendering achievable, revolutionizing the visual fidelity of interactive graphics.

While ray tracing promises highly realistic results, it remains constrained by a fundamental limitation: the scenes are designed by artists. An artist can invest an enormous amount of time meticulously crafting a scene to appear as realistic as possible, but ultimately, it remains a single, handcrafted and fixed in time scene. Alternatively, they might opt for a non-realistic approach, enabling the creation of stylized games or imaginative movie worlds. However, this reliance on artistic interpretation highlights a shortcoming: the inability to capture reality as it truly is. A more desirable solution would be to directly capture reality rather than approximating it through an artistic lens.


# Point Clouds
In parallel, point clouds emerged as a natural representation for real scenes due to their acquisition from scanners capable of capturing environments in tremendous detail. Other techniques, such as structure-from-motion, also generate point clouds using photography. However, point clouds have undergone an unfortunate evolution. While their use is widespread across various fields, particularly those requiring depth information, the data they provide is inherently limited. Sensors often produce point clouds as a collection of discrete points in space, lacking any inherent connectivity or topology.

This absence of connectivity - no information about which points are linked - presents significant challenges for manipulating these primitives. Without this structure, rendering point clouds becomes impractical; points remain disjoint in space, making it impossible to compute light interactions between them. Consequently, a considerable effort has been devoted to solving this problem by reconstructing surfaces from point clouds, effectively adding the missing structure.

Several methods have been developed to address this, with Poisson reconstruction [10] being among the most prominent. This approach attempts to infer and link the points to form a coherent surface. More recent advancements, including less-known work by the same author [11], have yielded similarly compelling results. While these methods are effective for solving many practical problems, the renderings they produce remain non-realistic.

In parallel with triangle-based methods, point clouds captured the interest of a small group of researchers for over a decade. These researchers published articles, authored a book summarizing their findings [12], and explored the characteristics and limitations of point clouds. Instead of constructing a topology between points, they considered a different approach: what if points were rendered as larger primitives, effectively "splatting" them on the screen to eliminate gaps in the scene?

This crude approximation initially resulted in pixelated renderings, but it resolved the issue of visible holes between points. Over time, larger points were replaced with shapes like squares and discs, and eventually ellipses that conformed to the curvature of the objects being represented. However, the underlying issue persisted: the points remained distinctly disjointed. To address this, researchers proposed replacing points with 2D Gaussians - each represented as a soft distribution, with maximum intensity or color at the center and decreasing transparency outward. Each Gaussian was oriented perpendicular to the surface, providing a smoother and more cohesive representation.

Although this reintroduced gaps in the scene, it became a non-issue as the Gaussians blended seamlessly together. Normalizing the scene at the final stage ensured there were no remaining transparency artifacts, producing a visually cohesive representation.

Lighting posed another challenge. In triangle-based graphics, Phong shading [1] interpolates normals across triangles to calculate lighting at each point of intersection. This concept was adapted for splats by defining normal fields over them and using these fields for lighting computations. Further refinements included computing Gaussians into screen space instead of projecting Gaussians from 3D space to the screen, accounting for the distortion caused by perspective projection. To mitigate aliasing, anisotropic filtering was applied. Additionally, parameters such as clipping values were introduced to create sharp edges at object boundaries, enhancing the realism of the rendered scenes.

But then, this line of research largely faded away. The primary reason was the lack of hardware support - manipulating points proved significantly more challenging than handling triangles, despite their potential to deliver realistic scene quality and direct acquisition. While some attempts were made to develop custom FPGAs capable of rendering point clouds [13], and these showed promising results, the approach never gained traction with major hardware manufacturers, who were reaping substantial profits from triangle-based rendering.

Points also presented significant challenges in terms of compression. Each point could have numerous associated parameters - such as color, principal axes, position, direction, and clipping planes - making storage complex and compression even harder. Accessing point data required sophisticated space-partitioning methods to optimize performance. Although efforts, particularly within the MPEG community [14], aimed to compress these primitives effectively (as certain industries continued to derive value from them), the lack of native hardware support limited broader adoption.

The promise of points as primitives capable of rendering more realistic scenes was never fully realized. A major roadblock was the absence of effective raytracing algorithms for transparent objects. Point clouds are typically acquired through devices that struggle to capture depth information for transparent objects, or through photographic techniques, which also fail to provide depth for such surfaces. Without depth information, points lack material properties and can only represent opaque surfaces. This limitation made it impossible to accurately render transparent objects, stalling progress in the field for a considerable amount of time.

Fast forward to recent developments: a group of researchers revived interest in point-based graphics [15]. Rather than modeling points as 2D Gaussians with an orientation, they proposed representing them as full 3D Gaussians. To account for light interactions varying with direction, they incorporated spherical basis functions, enabling dynamic light manipulation at each point, allowing light effects to change depending on direction. This approach offered a way to simulate effects like reflection and refraction, crucial for achieving transparent appearances.

However, it is important to emphasize that this approach does not replace material points. Points inherently struggle to represent transparent materials accurately, as the capability to capture transparency remains limited. While reflections in the rendered results often appear convincing, refractions pose a more significant challenge, resembling a light field over a hypothetical surface rather than true physical refractions. Numerous other limitations of this scene representation model persist, which, though beyond the scope of this blog post, continue to present obstacles for the field.

Currently, research efforts are focused on making scenes as realistic as possible and tackling these persistent challenges. Some approaches involve generating point clouds using physically based simulation techniques instead of capturing them [16], enabling the creation of transparent materials and simulate physics. Others aim to improve the acquisition methods for transparent objects or refine techniques for faking these effects more effectively. Prestigious conferences like SIGGRAPH Asia [17] and ICME [18] now feature dedicated sessions addressing these topics, highlighting the growing interest and progress in the field.

Nevertheless, point-based graphics still face significant hurdles. Scenes built from points are far less manipulable than their triangle-based counterparts. Decades of research manpower have gone into triangle-based methods, putting point-based techniques far behind. Furthermore, there is no guarantee that hardware manufacturers will invest in point-based primitives, despite ongoing discussions within NVIDIA, Khronos, and MPEG groups.

I am actively working on these challenges and am eager to witness how the field evolves in the coming years. Research progresses rapidly, yet it often feels frustratingly slow at the same time. Still, I find encouragement in the revival this field is experiencing, with novel ideas and perspectives that hold great promise for the future. Perhaps one day, this field will become mainstream—or it may fade into obscurity for another decade.


References:
1. Bui Tuong Phong, "Illumination for Computer Generated Pictures," Comm. ACM, Vol 18(6):311-317, June 1975.
2. [Unreal Engine](https://www.unrealengine.com/en-US)
3. [OpenGL](https://www.opengl.org/)
4. [Vulkan](https://www.vulkan.org/)
5. [Metal](https://developer.apple.com/metal/)
6. Keenan Crane; Max Wardetzky (November 2017). "A Glimpse into Discrete Differential Geometry". Notices of the American Mathematical Society. 64 (10): 1153–1159. doi:10.1090/noti1578
7. [Blender](https://www.blender.org/)
8. Matt Pharr, Wenzel Jakob, and Greg Humphreys. 2016. Physically Based Rendering: From Theory to Implementation (3rd. ed.). Morgan Kaufmann Publishers Inc., San Francisco, CA, USA.
9. [NVIDIA RT Cores](https://developer.nvidia.com/rtx/ray-tracing)
10. Michael Kazhdan, Matthew Bolitho, and Hugues Hoppe. 2006. Poisson surface reconstruction. In Proceedings of the fourth Eurographics symposium on Geometry processing (SGP '06). Eurographics Association, Goslar, DEU, 61–70.
11. Kazhdan, M., Chuang, M., Rusinkiewicz, S. and Hoppe, H. (2020), Poisson Surface Reconstruction with Envelope Constraints. Computer Graphics Forum, 39: 173-182. https://doi.org/10.1111/cgf.14077
12. Markus Gross and Hanspeter Pfister. 2007. Point-Based Graphics. Morgan Kaufmann Publishers Inc., San Francisco, CA, USA.
13. Tim Weyrich, Simon Heinzle, Timo Aila, Daniel B. Fasnacht, Stephan Oetiker, Mario Botsch, Cyril Flaig, Simon Mall, Kaspar Rohrer, Norbert Felber, Hubert Kaeslin, and Markus Gross. 2007. A hardware architecture for surface splatting. ACM Trans. Graph. 26, 3 (July 2007), 90–es. https://doi.org/10.1145/1276377.1276490
14. Authors	Ohji Nakagami, Sebastien Lasserre, Sugio Toshiyasu, Marius Preda, "White paper on G-PCC", ISO/IEC JTC 1/SC 29/AG 03, 2023
15. Bernhard Kerbl, Georgios Kopanas, Thomas Leimkuehler, and George Drettakis. 2023. 3D Gaussian Splatting for Real-Time Radiance Field Rendering. ACM Trans. Graph. 42, 4, Article 139 (August 2023), 14 pages. https://doi.org/10.1145/3592433
16. Xie, Tianyi, Zong, Zeshun, Qiu, Yuxing, Li, Xuan, Feng, Yutao, Yang, Yin, & Jiang, Chenfanfu. PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics. Retrieved from https://par.nsf.gov/biblio/10535780.
17. [Siggraph Asia 2024](https://asia.siggraph.org/2024/)
18. [ICME 2025](https://2025.ieeeicme.org/ss11-challenges-in-vision-with-non-lambertian-objects-segmentation-3d-reconstruction-and-rendering/)