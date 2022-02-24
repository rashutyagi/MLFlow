import mlflow

def calculate_nth_power(x, n):
    return x**n

if __name__ == '__main__':
    x,n = 8, 4
    y = calculate_nth_power(x, n)
    with mlflow.start_run():
        mlflow.log_param("x", x)
        mlflow.log_param("n", n)
        mlflow.log_metric("y", y)

# mlflow provides us the User Interface