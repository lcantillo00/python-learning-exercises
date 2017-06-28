num_touchdowns = input("How many touchdowns were scored? ")
num_field_goals = input("How many field goals were scored? ")

touchdowns_pts = input("How much is a touchdowns worth? ")
field_goals_pts = input("How much is a field goals worth? ")

total_score = int(touchdowns_pts) * int(num_touchdowns) + int(field_goals_pts) * int(num_field_goals)

print("The team has", total_score, "points")
