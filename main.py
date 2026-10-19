# working with python sets
from pyscript import display, document

# predefined sets for each grade level
grade_seven = {'Gabriella Flores', 'Mia Anderson', 'Sophia Reyes', 'Olivia Santos'}
grade_eight = {'Isabelle Dimapilis', 'Hailey Asis', 'Frances Blue', 'Jillian Grospe'}
grade_nine = {'Blake Pancho', 'Jasmeen Kaur', 'Sofia Navarro', 'Nicole Mendoza'}
grade_ten = {'Adrianna Allas', 'Elise Lim', 'Ashley Mangondato', 'Misha Manalo'}

# combine the sets using union
all_members = grade_seven.union(grade_eight, grade_nine, grade_ten)

# show the members
def update_results():
    display(sorted(all_members), target="results")
    display(f"Total members: {len(all_members)}", target="total")

# add a member
def add_member(e):
    global all_members

    first = document.querySelector("#firstname").value.strip()
    last = document.querySelector("#lastname").value.strip()
    new_member = f"{first} {last}".strip()
    all_members = all_members.union({new_member})

    document.querySelector("#results").innerHTML = ""
    document.querySelector("#total").innerHTML = ""

    update_results()

    document.querySelector("#firstname").value = ""
    document.querySelector("#lastname").value = ""

# display the starting list
update_results()
