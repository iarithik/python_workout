import random
def create_password_generator(string):
    def password_generation(num):
        password = []

        for i in range(num):
            op = random.choice(string)
            password.append(op)
        return ''.join(password)
    return password_generation

alpha_pass = create_password_generator('abcedf')

print(alpha_pass(10))

    