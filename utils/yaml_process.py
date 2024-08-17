import yaml
import loguru

class Yaml_Parser:
    def __init__(self):
        self.data = None
        self.yaml_file = None
    def load_yaml(self, yaml_file):
        with open(yaml_file, 'r') as stream:
            try:
                self.data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                loguru.logger.warning(f"Error loading yaml file: {self.yaml_file}")
        self.yaml_file = yaml_file
        return self.data

    def get_value(self, key):
        return self.data[key]

    def set_value(self, key, value):
        self.data[key] = value

    def write_yaml(self):
        with open(self.yaml_file, 'w') as stream:
            try:
                yaml.dump(self.data, stream)
            except yaml.YAMLError as exc:
                print(exc)

    def close(self):
        self.data = None
        self.yaml = None

if __name__ == '__main__':
    yaml_file = 'utils/test.yaml'
    yaml_parser = Yaml_Parser()
    data = yaml_parser.load_yaml(yaml_file)
    print(data)
    print(yaml_parser.get_value('test'))
    yaml_parser.set_value('test', 'great')
    yaml_parser.write_yaml()
    print(yaml_parser.get_value('test'))