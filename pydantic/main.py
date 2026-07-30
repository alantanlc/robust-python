import pdb
import yaml

with open('restaurant.yaml') as yaml_file:
    restaurant = yaml.safe_load(yaml_file)
    # pdb.set_trace()

print(restaurant)

