from typing import List
import argparse


class Caja:
    def __init__(self, codigo: int, largo: int, alto: int):
        self.codigo = codigo
        self.largo = largo
        self.alto = alto

    def __repr__(self) -> str:
        return f"Caja {self.codigo}: Largo: {self.largo} - Alto: {self.alto}"


def parse_file(file_path: str) -> List[Caja]:
    final_list: List[Caja] = []

    with open(file_path) as file:
        lines = file.readlines()

        for line in lines:
            list_of_str = line.split(',')
            box = Caja(int(list_of_str[0]), int(list_of_str[1]), int(list_of_str[2]))
            final_list.append(box)

    return final_list


def solve_problem(boxes: List[Caja], number_of_boxes: int, max_width: int) -> (List[int], List[int]):
    total_heights: List[int] = [0 for _ in range(number_of_boxes + 1)]
    boxes_shelves: List[int] = [0 for _ in range(number_of_boxes)]
    number_of_shelves = 0

    for i in range(1, number_of_boxes + 1):
        number_of_shelves += 1
        actual_box_width = boxes[i - 1].largo
        actual_box_height = boxes[i - 1].alto

        shelve_max_height = actual_box_height
        shelve_used_width = actual_box_width

        # Se agrega la caja a una nueva repisa y se calcula la altura total
        # con el resultado anterior
        total_height = total_heights[i - 1] + actual_box_height

        # -------------------------------------------------------
        boxes_in_shelve = [i]
        for j in range(i - 1, 0, -1):
            box_width = boxes[j - 1].largo
            box_height = boxes[j - 1].alto

            if box_width + shelve_used_width > max_width:
                break

            # Actualizo largo usado de la repisa
            shelve_used_width = shelve_used_width + box_width
            # Actualizo altura maxima
            shelve_max_height = max(shelve_max_height, box_height)

            new_total_height = total_heights[j - 1] + shelve_max_height
            if new_total_height < total_height:
                total_height = new_total_height
                boxes_in_shelve = range(j, i + 1)

        total_heights[i] = total_height

        for index in [x - 1 for x in boxes_in_shelve]:
            boxes_shelves[index] = number_of_shelves

    initial_number = boxes_shelves[0]
    counter = 1
    final_list = [0 for _ in range(0, number_of_boxes)]
    for index, element in enumerate(boxes_shelves):

        if initial_number != element:
            counter += 1
            initial_number = element

        final_list[index] = counter

    return total_heights, final_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Greey Problem")
    parser.add_argument(
        "--n", dest="n", help="Numero de cajas", type=int, required=True
    )
    parser.add_argument(
        "--w", dest="w", help="Ancho máximo de la repisa", type=int, required=True
    )
    parser.add_argument(
        "--f", dest="file_name", help="Archivo de entrada", type=str, required=True
    )

    args = parser.parse_args()

    file_path = args.file_name
    shelve_size = args.w
    number_of_boxes = args.n

    list_of_boxes = parse_file(file_path=file_path)
    heigths, shelves = solve_problem(
        boxes=list_of_boxes,
        number_of_boxes=number_of_boxes,
        max_width=shelve_size
    )

    print("Altura mínima total", heigths[-1])
    for index, box_shelve in enumerate(shelves):
        print(f"Repisa {box_shelve}: Caja {index + 1}")
