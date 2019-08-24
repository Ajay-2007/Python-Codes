# create HTML List

items = ['first string', 'second string']
html_str = "<ul>\n"

for i in range(len(items)):
    html_str += "<li>" + items[i] + "</li>\n"
html_str += "</ul>"
print(html_str)

print()
# Udacity Solution
html_str1 = "<ul>\n"
for item in items:
    html_str1 += "<li>{}</li>\n".format(item)
html_str1 += "</ul>"
print(html_str1)
