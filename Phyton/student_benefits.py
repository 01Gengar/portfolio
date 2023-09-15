# Defining index raise here
index_raise = 1.17

# Reading the user input
study_benefits = input("Enter the amount of the study benefits: ")

# Let's fix issue if "," is separating decimals and converting it to float
if "," in study_benefits:
    student_benefits = float(study_benefits.replace(",", "."))
else:
    student_benefits = float(study_benefits)

# Calculating new study benefits
new_benefits = student_benefits * index_raise / 100 + student_benefits
optimistic_benefits = new_benefits * index_raise / 100 + new_benefits

# Let's print the result
print("If the index raise is", index_raise, "percent, the study benefit,")
print("after a raise, would be", new_benefits, "euros")
print("and if there was another index raise, the study\nbenefits would be as much as", optimistic_benefits, "euros")
