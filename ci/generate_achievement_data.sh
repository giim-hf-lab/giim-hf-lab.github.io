#1/usr/bin/env bash

set -eu

mkdir -p docs/_data/achievements

python3 ci/generate_achievement_data.py

git config --global user.name "Tinson Lai"
git config --global user.email "laitingsheng@hotmail.com"

git add docs

git commit -m 'Automated data generation from GitHub Actions' || echo "Nothing to commit"

git push
