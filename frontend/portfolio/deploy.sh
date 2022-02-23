cd frontend/portfolio
npm run build
touch dist/.nojekyll
cd ../..
git add -A
git status
git commit -m "Deployment Build ($(date))"
git push
git subtree split --prefix frontend/portfolio/dist -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages