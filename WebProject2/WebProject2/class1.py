import itertools
import os


clauses = []

digits = range(1, 4)

def varnum(i, j):
    assert(i in digits and j in digits)
    return 10*i + j 


def exactly_one_of(literals):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])


# cell [i,j] contains exactly one digit
for (i, j) in itertools.product(digits, repeat=2):
    exactly_one_of([varnum(i, j) for j in digits])




with open('tmp.cnf', 'w') as f:
    f.write("p cnf {} {}\n".format(999, len(clauses)))
    for c in clauses:
        c.append(0);
        f.write(" ".join(map(str, c))+"\n")

os.system("minisat tmp.cnf tmp.sat")

with open("tmp.sat", "r") as satfile:
    for line in satfile:
        if line.split()[0] == "UNSAT":
            print("There is no solution")
        elif line.split()[0] == "SAT":
            pass
        else:
            assignment = [int(x) for x in line.split()]

            for i in digits:
                for j in digits:
                    for k in digits:
                        if varnum(i, j, k) in assignment:
                            print(k, end="")
                            break

                print("")

