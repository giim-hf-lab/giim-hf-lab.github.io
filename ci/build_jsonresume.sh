#1/usr/bin/env bash

set -eu

mkdir -p docs/_pages/members docs/assets/pdfs/members

pushd jsonresume

for folder in jsons/*
do
	people=`awk -F/ '{print $NF}' <<< $folder`
	cp $folder/resume.json .

	npm run build:pdf
	npm run build:html

	cat "${GITHUB_WORKSPACE}/ci/template/jsonresume.html.header" | sed "s/%PEOPLE%/${people}/g" | cat - resume.html > "${GITHUB_WORKSPACE}/docs/_pages/members/${people}.html"
	rm resume.html
	mv resume.pdf "${GITHUB_WORKSPACE}/docs/assets/pdfs/members/${people}.pdf"
done

popd

git config --global user.name "Tinson Lai"
git config --global user.email "laitingsheng@hotmail.com"

git add docs

git commit -m 'Automated JSON Resume build from GitHub Actions'

git push
