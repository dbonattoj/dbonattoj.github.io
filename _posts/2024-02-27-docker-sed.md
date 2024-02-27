---
layout: post
title: Docker Dependency Magic - Unleashing sed to Tailor Your Packages
date: 2024-02-27 16:24:00
description: Papers just miss this kind of interactivity.
tags: formatting latex
categories: publications
---

In the world of Docker workflows, situations arise where you find yourself in the familiar dance of cloning a Git repository, installing via CMake, or setting up a pip or Anaconda environment. Yet, the default packages don't always align perfectly with your needs.

To tackle this common dilemma, I often resort to a simple yet effective maneuver: using sed to gracefully replace specific text within someone else's package in Docker. It's not groundbreaking, but it's a reliable technique that often gets overlooked.

In this blog post, I share my go-to command – a straightforward sed line – making the process of adjusting packages in Docker a breeze.

{% highlight Dockerfile %}
{% raw %}
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/refs/tags/4.5.5.zip && unzip opencv.zip && \
    wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/refs/tags/4.5.5.zip  && unzip opencv_contrib.zip

RUN mkdir -p build && cd build && cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.5.5/modules ../opencv-4.5.5

RUN cd build && cmake -Bbuild . -DCMAKE_BUILD_TYPE=Release \
                    -DBUILD_TESTS=OFF \
                    -DBUILD_PERF_TESTS=OFF \
                    -DBUILD_EXAMPLES=OFF \
                    -DBUILD_opencv_apps=OFF

RUN cd build && cmake --build . -j "$(nproc)" --target install

# [...git clone of another repository...]

# Changing version of OpenCV in external package
RUN sed -i 's/find_package(OpenCV 4\.2 REQUIRED)/find_package(OpenCV 4.5 REQUIRED)/g' CMakeFile.txt

[...]
# Removing the use of pip in anaconda environment file
RUN sed -i '/pip:/d' environment.yml
RUN sed -i '/- module_name/d' environment.yml

# [...continue making...]
{% endraw %}
{% endhighlight %}

And there you have it – a little Docker magic with the trusty sed line! It might not be the star of the show, but in the everyday chaos of Docker setups, it sure plays a solid supporting role. So, next time you're tweaking your environment, give sed a nod – it's your backstage pass to smoother, customized Docker adventures !