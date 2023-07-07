import os
from uie_convert import convert_graph, convert_to_oneie
from universal_ie.generation_format import generation_format_dict
from universal_ie.dataset import Dataset


def main_func(generation_format, config, output):
    generation_class = generation_format_dict.get(generation_format)

    if os.path.isfile(config):
        config_list = [config]
    else:
        config_list = [
            os.path.join(config, x) for x in os.listdir(config)
        ]
    print("config_list")
    print(config_list)
    for filename in config_list:
        dataset = Dataset.load_yaml_file(filename)

        datasets = dataset.load_dataset()
        label_mapper = dataset.mapper
        print(label_mapper)

        output_name = (
                f"converted_data/text2{generation_format}/{output}/"
                + dataset.name
        )

        if generation_class:
            convert_graph(
                generation_class,
                output_name,
                datasets=datasets,
                language=dataset.language,
                label_mapper=label_mapper,
            )
        elif generation_format == "oneie":
            convert_to_oneie(output_name, datasets=datasets)


def run_data_cmd():
    import os

    cmd = "python uie_convert.py -format spotasoc -config data_config/absa -output abas"
    os.system(cmd)


def run_debug():
    # "python uie_convert.py -format spotasoc -config data_config/absa -output abas"
    main_func(
        generation_format="spotasoc",
        config="data_config/absa",
        output="absa"
    )


if __name__ == '__main__':
    run_debug()
