duty_dict = {
    1: "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.",
    2: "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.",
    3: "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.",
    4: "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
    5: "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts",
    6: "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
    7: "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).",
    8: "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
    9: "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).",
    10: "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
    11: "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.",
    12: "Duty 12 Look to automate any manual tasks that are repeated, often using APIs.",
    13: "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience.",
}

def print_duties(option):
    if option == 3:
        print(duty_dict[9])
    elif option == 4:
        specific_duties_index = [1, 2, 3, 4, 13]
        [print(duty_dict[i]) for i in specific_duties_index]
    elif option == 5:
        specific_duties_index = [5, 7, 10]
        [print(duty_dict[i]) for i in specific_duties_index]    
    else: 
        for duty in duty_dict.values():
            print("{0}\n".format(duty))

def format_html():
    lines = [
        "<html>",
        "    <head>",
        "        <meta charset=\"UTF-8\"/>",
        "        <title>Apprenticeship Duties</title>",
        "    </head>",
        "    <body>",
        "        <h1>Apprenticeship Duties</h1>",
        "        <ol>"
    ]
    for duty in duty_dict.values():
        lines.append(f"            <li>{duty}</li>")
    lines.extend([
        "        </ol>",
        "    </body>",
        "</html>"
    ])
    return "\n".join(lines)

def write_duties():
    with open("file.html", "w") as file:
        duties_html = format_html()
        file.write(duties_html)
    

if __name__=="__main__":
    choice = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
    Press (2) to create a file that lists all the duties\n       
    Enter your choice:
    """)
    if choice == '1':
        print_duties(1)
    elif choice == '2':
        write_duties()
    elif choice == '3':
        print_duties(3)
    elif choice == '4':
        print_duties(4)
