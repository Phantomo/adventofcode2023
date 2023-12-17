from pprint import pprint

def read_input():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


def cast_to_int(data):
    return (int(number) for number in data)


def clean_mapping_data(mappings):
    clean_data = {}
    source = None
    for line in mappings:
        if line.find("map") != -1:
            mapping_schema, _ = line.strip().split()
            source, _, destination = mapping_schema.split("-")
            clean_data[source] = {}
            clean_data[source]["destination"] = destination
        elif line:
            if not clean_data[source].get("mappings"):
                clean_data[source]["mappings"] = {}
            source_start_range, dest_start_range, range_length = cast_to_int(line.strip().split())
            for i in range(range_length):
                if source:
                    clean_data[source]["mappings"][dest_start_range + i] = source_start_range + i
    return clean_data

def find_lowest_location(seeds, data):
    location = None
    for seed in seeds:
        current_mapper = data["seed"]
        current_source = seed
        while True:
            if current_mapper["mappings"].get(current_source):
                current_source = current_mapper["mappings"][current_source]
            if not data.get(current_mapper["destination"]):
                break
            current_mapper = data[current_mapper["destination"]]
        if not location or current_source < location:
            location = current_source
    return location


if __name__ == "__main__":
    data = read_input()
    _, seeds = data[0].split(":")
    seeds = [int(seed) for seed in seeds.strip().split()]
    data = clean_mapping_data(data[1:])
    # pprint(data)
    print(find_lowest_location(seeds, data))