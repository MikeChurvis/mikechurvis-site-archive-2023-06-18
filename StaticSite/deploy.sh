git subtree split --prefix StaticSite/portfolio/dist -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages