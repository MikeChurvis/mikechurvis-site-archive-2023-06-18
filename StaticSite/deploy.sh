cd StaticSite/portfolio
npm run build
touch dist/.nojekyll
git commit -am "Deployment Build ($(date))"
cd ../..
git subtree split --prefix StaticSite/portfolio/dist -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages