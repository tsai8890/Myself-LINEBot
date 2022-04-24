#! /bin/zsh
git add --all
git commit --amend -m "test"
git push heroku main --force
