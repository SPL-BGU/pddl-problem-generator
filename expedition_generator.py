#!/usr/bin/python3
import random
import sys
from pathlib import Path
from typing import NoReturn

from common import get_problem_template

TEMPLATE_FILE_PATH = Path("expedition_template.pddl")


def generate_instance(instance_name: str, num_sleds: int) -> str:
    """Generate a single planning problem instance.

    :param instance_name: the name of the problem instance.
    :param num_sleds: the number of sleds in the problem.
    :return: the string representing the planning problem.
    """
    template = get_problem_template(TEMPLATE_FILE_PATH)
    num_sleds = random.randint(1, num_sleds)
    num_disjoint_waypoints = random.randint(1, num_sleds)
    num_waypoints = random.randint(6, 15)
    waypoint_names = []
    waypoint_connections = []
    initial_waypoint_names = []
    for wtype in range(num_disjoint_waypoints):
        for i in range(num_waypoints):
            if i == 0:
                initial_waypoint_names.append(f"w{wtype}_{i}")
            waypoint_names.append(f"w{wtype}_{i}")
            if i == num_waypoints - 1:
                continue

            waypoint_connections.append(f"(is_next w{wtype}_{i} w{wtype}_{i+1})")

    sleds_locations = []
    if num_disjoint_waypoints == 1:
        for i in range(num_sleds + 1):
            sleds_locations.append(f"(at s{i} w0_0)")

    else:
        for i in range(num_sleds + 1):
            sleds_locations.append(f"(at s{i} w{i % num_disjoint_waypoints}_0)")

    sled_goal_positions = []
    for i in range(num_sleds + 1):
        if num_disjoint_waypoints == 1:
            sled_goal_positions.append(f"(at s{i} w0_{num_waypoints - 1})")
        else:
            sled_goal_positions.append(f"(at s{i} w{i % num_disjoint_waypoints}_{num_waypoints - 1})")

    template_mapping = {
        "instance_name": instance_name,
        "sleds_list": " ".join([f"s{i}" for i in range(num_sleds + 1)]),
        "waypoint_list": " ".join(waypoint_names),
        "sleds_initial_positions": "\n".join(sleds_locations),
        "sleds_capacity": "\n\t".join([f"(= (sled_capacity s{i}) {random.randint(3, 5)})" for i in range(num_sleds + 1)]),
        "sleds_supplies": "\n\t".join([f"(= (sled_supplies s{i}) {random.randint(1, 2)})" for i in range(num_sleds + 1)]),
        "waypoint_supplies":  "\n\t".join([f"(= (waypoint_supplies {name}) {10000 if name in initial_waypoint_names else 0})" for name in waypoint_names]),
        "waypoints_connections": "\n\t".join(waypoint_connections),
        "sleds_goal_positions": "\n\t".join(sled_goal_positions),
    }
    return template.substitute(template_mapping)


def generate_multiple_problems(output_folder: Path) -> NoReturn:
    """Generate multiple problems based on the input arguments.

    :param output_folder: the path to the output folder where the problems will be saved.
    """
    for i in range(0, 200):
        print(f"Generating problem index {i}")
        with open(output_folder / f"pfile{i}.pddl", "wt") as problem_file:
            problem_file.write(generate_instance(f"instance_{i}", 3))


def main():
    generate_multiple_problems(output_folder=Path(sys.argv[1]))


if __name__ == "__main__":
    main()
