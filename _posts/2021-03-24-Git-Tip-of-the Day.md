---
layout: post
title:  "Git Tip of the Day"
subtitle: "a quick little prune"
date:   2021-03-24 08:43:29 -0400
categories: git, bash, tutorial
---
(no need for a "one weird trick" type of line here, this actually works)

Have too many local branches that need to be pruned? Don't want to `git branch -D` for **EVERY. SINGLE. ONE.** while making sure you have the branch name exactly right each time?

<!--more-->

Type in the following and you'll be one and done, leaving just the `master` branch!

```bash
git branch | grep -v "master" | xargs git branch -D
```

It will take less time than it took to make this blog post.

Code on.

-Mike Merin
