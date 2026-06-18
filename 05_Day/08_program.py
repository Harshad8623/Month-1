def fun(**kwargs):
    for i, j in kwargs.items():
        print(i,"=", j)

fun(Patient="John Doe", Age=45, Condition="Healthy")