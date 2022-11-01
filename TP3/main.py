import argparse
from typing import List, Any
from dataclasses import dataclass

from graph import Graph
from utils import ford_fulkerson



@dataclass
class TaskCosts:
    name: str
    team1_cost: int
    team2_cost: int


@dataclass
class TransitionCost:
    next: str
    cost: int


def parse_file(file_name: str) -> (List[TaskCosts], List[List[TransitionCost]]):
    list_of_tasks = []
    list_of_transitions = []

    with open(file_name) as f:
        for line in f:
            split = line.strip().split(',')
            list_of_tasks.append(TaskCosts(split[0], int(split[1]), int(split[2])))
            list_of_transitions.append(parse_transition_costs(split[3:]))

    return list_of_tasks, list_of_transitions


def parse_transition_costs(list_of_costs: List[str]):
    dictionary = {}

    last_letter = None
    for element in list_of_costs:
        if not element.isnumeric():
            last_letter = element
        else:
            dictionary[last_letter] = int(element)

    final_list = []
    for k, i in dictionary.items():
        final_list.append(TransitionCost(k, i))

    return final_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Network Flow problem")
    parser.add_argument(
        "--f", dest="file_name", help="Archivo de entrada", type=str, required=True
    )

    args = parser.parse_args()
    file_path = args.file_name

    tasks, transition_costs = parse_file(file_name=file_path)
    tasks_index = [x.name for x in tasks]

    new_graph = Graph(len(tasks) + 2)
    fuente_index = 0
    sumidero_index = 1

    for index, x in enumerate(tasks):
        actual_index = index + 2

        new_graph.add_edge(fuente_index, actual_index, x.team1_cost)
        new_graph.add_edge(actual_index, sumidero_index, x.team2_cost)

        for dependency in transition_costs[index]:
            new_graph.add_edge(actual_index, tasks_index.index(dependency.next) + 2, dependency.cost)

    result = ford_fulkerson(new_graph, fuente_index, sumidero_index)
    print('Costo minimo: {}'.format(result))

    # Obtengo que grupo hizo cada task
    lista_de_fuente = new_graph.m_adj_matrix[0][2:]
    for index, element in enumerate(lista_de_fuente):
        team = 2
        if element == 0:
            team = 1

        print("Tarea {} hecha por el equipo {}".format(tasks_index[index], team))


