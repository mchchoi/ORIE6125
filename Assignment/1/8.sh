echo "Question 5:"
git ls-tree -r --full-tree HEAD | sed -n -e 's/^.*blob //p'
echo "Question 6:"
git rev-parse origin/master
echo "Question 7:"

