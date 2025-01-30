data={
    "id":[0,1,2],
    "name":["hassan","arham","taimoor"],
    "salaries":[100,150,200],
    "marks":[90,70,80]

}
max_salary=max(data["salaries"])
min_salary=min(data["salaries"])
max_salary_index=data['salaries'].index(max_salary)
min_salary_index=data['salaries'].index(min_salary)

for key in data:
    print(data[key][max_salary_index])
    print(data[key][min_salary_index])

average_salary