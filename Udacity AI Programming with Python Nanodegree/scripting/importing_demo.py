# importing_demo.py
import useful_functions_with_main as uf

scores = [88, 92, 79, 93, 85]
mean = uf.mean(scores)
curved = uf.add_five(scores)
c_mean = uf.mean(curved)

print("Scores: ", scores)
print("Original Mean:", mean, " New mean: ", c_mean)

print(__name__)
print(uf.__name__)
print(mean)
#print(add_five)
