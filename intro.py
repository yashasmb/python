# import requests
#
# YOUR_API_KEY = "lDboxur9dYBf7niNJhB2SjE2ZytxBfVCR28OcI9M"
# category = ["Any Category",
#             "Linux",
#             "Bash",
#             "Uncategorized",
#             "Docker",
#             "SQL",
#             "CMS",
#             "Code",
#             "DevOps"]
#
# Difficulty = [
#     "Any Difficulty",
#     "Easy",
#     "Medium",
#     "Hard"
# ]
#
# print("welcome to quiz ")
# print()
#
# print("which category do you wish to play")
# i = 1
# for catagory in category:
#     print(f"{i}.{catagory}")
#     i = i + 1
# print()
# cata = int(input("enter your choice (in number)"))
# cata = category[cata - 1]
# print(cata)
# # print()
#
#
# print("Choose the difficulty Difficulty")
# i = 1
# print()
# for catagory in Difficulty:
#     print(f"{i}.{catagory}")
#     i = i + 1
# print()
# diff = int(input("enter your choice (in number)"))
# diff = Difficulty[diff - 1]
# # print(diff)
# print()
#
# no_of_question = int(input("Enter the number of questions(0-20)"))
#
# if cata == category[0] and diff == Difficulty[0]:
#     api = f"https://quizapi.io/api/v1/questions?apiKey={YOUR_API_KEY}&limit={no_of_question}"
# elif cata == category[0]:
#     api = f"https://quizapi.io/api/v1/questions?apiKey={YOUR_API_KEY}&category=&difficulty={diff}&limit={no_of_question}"
# elif diff == Difficulty[0]:
#     api = f"https://quizapi.io/api/v1/questions?apiKey={YOUR_API_KEY}&category={cata}&difficulty=&limit={no_of_question}"
# else:
#     api = f"https://quizapi.io/api/v1/questions?apiKey={YOUR_API_KEY}&category={cata}&difficulty={diff}&limit={no_of_question}"
#
# print(api)
#
# r = requests.get(url=api)
# data =r.json()
# # print(response.status_code)
# print(data)
#
#





import requests

BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products")
print(response.json())
