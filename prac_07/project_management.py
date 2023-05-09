from project import Project
import datetime


def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    menu = ["l", "s", "d", "f", "a", "u", "q"]
    print(' - (L)oad projects')
    print(' - (S)ave projects')
    print(' - (D)isplay projects')
    print(' - (F)ilter projects by date')
    print(' - (A)dd new project')
    print(' - (U)pdate project')
    print(' - (Q)uit')
    user_choice = input(">>>")

    while user_choice != "q":
        if user_choice == 'l':
            filename = input('Enter filename to load: ')
            load_projects(filename)
            print(f'{len(projects)} projects loaded.')
        elif user_choice == 's':
            filename = input('Enter filename to save: ')
            save_projects(filename, projects)
            print(f'{len(projects)} projects saved.')
        elif user_choice == 'd':
            display_projects(projects)
        elif user_choice == 'f':
            filter_projects_by_date(projects)
        elif user_choice == 'a':
            add_project(projects)
            print('Project added.')
        elif user_choice == 'u':
            update_project(projects)
        else:
            print('Invalid choice. Please try again.')
    else:
        print("farewell")


def load_projects(filename):
    projects = []
    with open(filename) as file:
        for line in file:
            fields = line.strip().split('\t')
            project = Project(*fields)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write('Name\tStart Date\tPriority\tcost\tCompletion\n')
        for project in projects:
            file.write(f'{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost}\t{project.completion}\n')


def display_projects(projects):
    # Sort projects by priority
    projects = sorted(projects)

    # Display incomplete projects
    print("Incomplete projects:")
    for i, project in enumerate(projects):
        if project.completion < 100:
            print(f"{i} {project}")

    # Display complete projects
    print("\nComplete projects:")
    for i, project in enumerate(projects):
        if project.completion == 100:
            print(f"{i} {project}")


def filter_projects_by_date(projects):
    date_string = input('Enter start date (dd/mm/yyyy): ')
    date = datetime.datetime.strptime(date_string, '%d/%m/%Y').date()
    filtered_projects = sorted(filter(lambda p: p.start_date >= date, projects), key=lambda p: p.start_date)
    print('Filtered projects:')
    for project in filtered_projects:
        print(f'  {project}')


def add_project(projects):
    name = input('Enter project name: ')
    start_date = input('Enter start date (dd/mm/yyyy): ')
    priority = int(input('Enter priority: '))
    cost = float(input('Enter cost: '))
    completion = float(input('Enter completion percentage: '))
    project = Project(name, start_date, priority, cost, completion)
    projects.append(project)


def update_project(projects):
    display_projects(projects)
    project_index = int(input('Enter project index to update: '))
    project = projects[project_index]
    name = input('Enter project name: ')
    start_date = input('Enter start date (dd/mm/yyyy): ')
    priority = int(input('Enter priority: '))
    cost = float(input('Enter cost: '))
    completion = float(input('Enter completion percentage: '))
    project.name = name
    project.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    project.priority = priority
    project.cost = cost
    project.completion = completion

    # Sort the projects in alphabetical order by project name
    def get_project_name(project):
        return project.name.lower()

    sorted_projects = sorted(projects, key=get_project_name)

    # Iterate through the sorted projects and display them in the desired format
    for i, project in enumerate(sorted_projects):
        if project.completion == 100:
            status = 'completed'
        else:
            status = 'incomplete'
        print(
            f"{i} {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, cost: ${project.cost:.2f}, completion: {project.completion}% ({status})")


main()
