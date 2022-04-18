#1/usr/bin/env bash

set -eu

mkdir -p docs/_pages/members docs/assets/pdfs/members

pushd jsonresume

for folder in jsons/*
do
	people=`awk -F/ '{print $NF}' <<< $folder`
	cp $folder/resume.json .

	npm run build:html
	cat "${GITHUB_WORKSPACE}/ci/template/jsonresume.html.header" | sed "s/%PEOPLE%/${people}/g" | cat - resume.html > "${GITHUB_WORKSPACE}/docs/members/${people}.html"
	rm resume.html
done

popd

git config --global user.name "Tinson Lai"
git config --global user.email "laitingsheng@hotmail.com"

git add docs

git commit -m 'Automated JSON Resume build from GitHub Actions' || echo "Nothing to commit"

git push
