#Atuará como intermediário entre a UI e o modelo de dados. Ele processará os dados de entrada da UI, passará para o modelo para criar o JSON e enviará o JSON via MQTT.

# TODO: Define functions to handle user input and interact with the model and MQTT client.

# controller.py

from model import Model, AspectType, Variable, AssetType, Asset, Mapping
from mqtt_client import publish_model

class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.model = Model(tenant_id="your_tenant_id")  # you will get this from your config or user input

    def create_aspect_type(self, name, description, variables):
        # Create and add a new aspect type to the model
        aspect_type = AspectType(tenant_id="your_tenant_id", name=name, description=description, variables=variables)
        self.model.add_aspect_type(aspect_type)

    def create_variable(self, name, data_type, quality_code, searchable, unit=None):
        # Create a new variable
        return Variable(name=name, data_type=data_type, quality_code=quality_code, searchable=searchable, unit=unit)

    def create_asset_type(self, name, description, aspects):
        # Create and add a new asset type to the model
        asset_type = AssetType(tenant_id="your_tenant_id", name=name, description=description, aspects=aspects)
        self.model.add_asset_type(asset_type)

    def create_asset(self, type_name, name, description):
        # Create and add a new asset to the model
        asset = Asset(tenant_id="your_tenant_id", type_name=type_name, name=name, description=description)
        self.model.add_asset(asset)

    def create_mapping(self, aspect_name, variable_name, asset_reference):
        # Create and add a new mapping to the model
        mapping = Mapping(aspect_name=aspect_name, variable_name=variable_name, asset_reference=asset_reference)
        self.model.add_mapping(mapping)

    def generate_json(self):
        # Generate the JSON representation of the model
        return self.model.to_json()

    def submit_model(self):
        # Generate the JSON and publish it via MQTT
        json_data = self.generate_json()
        publish_model(json_data)  # This function will be defined in mqtt_client.py

    # Add more methods as needed to handle UI actions and update the model
