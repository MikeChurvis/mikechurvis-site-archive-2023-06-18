cd StaticSite/portfolio
npm run build
cd ../..
touch StaticSite/portfolio/dist/.nojekyll
git subtree split --prefix StaticSite/portfolio/dist -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages