scores_list = input("Enter student scores: ").split()
for n in range(0, len(scores_list)):
    scores_list[n] = int(scores_list[n])

print(f"Scores:  {scores_list}")
max = 0;
for score in scores_list:
    if score > max:
        max = score
print(f"Max Score: {max}")