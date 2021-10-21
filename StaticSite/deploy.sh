cd StaticSite/portfolio
npm run build
touch dist/_astro/.nojekyll
git add -A
git status
git commit -m "Deployment Build ($(date))"
git push
cd ../..
git subtree split --prefix StaticSite/portfolio/dist -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages