The ULCDC project's awesome documentation site. To make modifications to the textual content, you should be able to easily edit files through GitHub's edit interface. 

Written using Jekyll (http://jekyllrb.com/)

I've used rbenv to get the correct version of Ruby running on my mac:

  1. Use Homebrew to install rbenv (note: incompatible with rvm): 

      brew update
      brew install rbenv ruby-build

  2. Following the instructions from the rbenv install, I added to my .bash_profile:

      if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
      source ~/.bash_profile

  3. Navigate to the folder I'm using to develop these pages in:

      cd ~/Projects/ucldc-docs

  4. Set up a local ruby environment in this folder:
      rbenv local 1.9.3-p125
      rbenv rehash

Then I followed the instructions [here](https://help.github.com/articles/using-jekyll-with-pages) (https://help.github.com/articles/using-jekyll-with-pages) to get jekyll up and running. This uses Bundler and the github-pages gem, to ensure your setup most closely resembles how GitHub Pages works to host your Jekyll site. 

  1. gem install bundler
  2. rbenv rehash
  3. Bundler wasn't playing nice with rbenv for the bundle install command, so I ran:

      gem install github-pages

  4. make a file named Gemfile and add 

      source 'https://rubygems.org'
      gem 'github-pages'

At this point, you can clone this repository: 

  1. git clone https://github.com/ucldc/ucldc-docs/
  2. then checkout the gh-pages branch: git checkout -b gh-pages origin/gh-pages
  3. modify the url line of _config.yml from "http://ucldc.github.io/ucldc-docs" to "localhost:4000"

Run the Jekyll server:

  1. bundle exec jekyll serve

I usually add the --watch flag to jekyll serve. This flag watches for changes in the jekyll source files and automatically builds and serves changed files. 
