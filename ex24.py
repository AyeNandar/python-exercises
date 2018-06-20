print("Let's practice everything.")
print('You \'d need to know \'bout escapes with \\ that do:')
print('\n new;ines and \t tabs.')

poem = """
\t The lovely world 
with logic so family p;anted
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an expalanation
\n\t\t where there is none ."""

print("-----------")
print(poem)
print("------------------")

five = 10 - 2 + 3 - 6
print("This should be five:", five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 10000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point os :{}".format(start_point))
print("We'd have ", beans," beans,", jars,"and ", crates," c")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars,and {} crates.".format(*formula))
