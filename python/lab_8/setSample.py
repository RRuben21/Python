Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
set1=set()
set1
set()
set1.add(1)
set1
{1}
set1.add(2)
set1
{1, 2}
set2={2,3,4,5}
set2
{2, 3, 4, 5}
set1.difference(set2)
{1}
set2.difference(set1)
{3, 4, 5}
set1.union(set2)
{1, 2, 3, 4, 5}
set1.intersection(set2)
{2}
set1.isdisjoint(set2)
False
set3={2,3}
set3.issubset(set2)
True
set3.issuperset(set2)
False
