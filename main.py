print("Exsample a * b + c * d = 180000")
qw_1 = int(input("Enter a: "))
qw_2 = int(input("Enter b: "))
qw_3 = int(input("Enter c: "))
qw_4 = int(input("Enter d: "))

assert qw_1 * qw_2 + qw_3 * qw_4 == 180000, "Example incorrect"
if qw_1 * qw_2 + qw_3 * qw_4 == 180000:
    print("Example correct")