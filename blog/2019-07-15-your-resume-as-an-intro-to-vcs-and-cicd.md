# Your Resume as an Introduction to Version Control and CI/CD 

[TL;DR: Steps](#Steps)

## Background

You know how to program -- maybe you've taken lower / upper division computer science classes. Or, you've 
attended a boot camp, are self-taught (good for you!), etc. 

However, there are a few known unknowns that separates where you are now to the developer in industry that you hope to 
be. 

In this article, I want to talk about one of these areas: Project Hygiene!

I'll cover a few concepts that you've likely heard of but might not use to the fullest extent: Version Control Systems
(VCS) and Continuous Integration / Continuous Deployment (CI/CD).  

I'll be going over a lot of particulars when I could be talking about generalities. I do this because I realize that 
at your current stage, it is critical to have something to show for what you know. Often when starting out, people get 
overwhelmed by information. Instead, I want to leave you knowing enough concepts and specific skills to empower you in 
your own personal projects. 

Instead of talking about these topics with a toy coding problem, I'd like to leave you with something practical. So, 
by the end of this tutorial, you will have a new way to write, maintain, and publish your resume! I love this 
application, because it clearly illustrates the value of VCS and CI/CD. 

Let's begin!

## April_Resume_Final_Final_2.pdf

Do you have a resume where you keep track of the version via the title? I have, in the past. And it cause me lots of 
problems, as you can imagine. 

* * * 

## Steps
1. Create a new Repository on GitHub
  - Click the `+` sign on the top right corner, select "Create new repository"
  - Give your Repo a name and description.
  - Add a license! I recommend Apache or MIT.
  - Add a default README
  - Follow the instructions to sync the GitHub repo with your local version
1. Groom your initial master branch
  - (recommended) `curl https://raw.githubusercontent.com/github/gitignore/master/TeX.gitignore -o .gitignore && git add .gitignore`
  - (optional) Add more information to your README.md, then `git add README.md`
  - `git commit -m "initial commit"`
1. Create a feature branch for the build
  - `git checkout -b build`
1. Acquire a resume template 
  - Easy starter: [Use this .tex file](https://github.com/sb2nov/resume)
  - [Choose a different resume template](https://www.latex-project.org/get/) or make your own.
  - `git add` all of the assets
1. Create build scripts for local development
  - [Set up Latex on your computer](https://www.latex-project.org/get/) 
  - Windows (assuming you installed miktex): 
  `echo "pdflatex <resume-filename>.tex" >> build.bat` 
  - Linux / Mac: 
  `echo "pdflatex <resume-filename>.tex" >> build.sh`

1. Fill in your resume in a edit-commit-push loop
  - Make edits to your template until you've finished one "chunk"
  - (optional) Compile your Latex file to see if what you have looks good.
  - `git add <resume-name>.tex`
  - `git commit -m "<description of latest changes>`
  - `git push origin initial-draft`
  - Repeat
1. When you're happy with the draft, make a Pull Request (PR) into master
