#Definirá a estrutura do modelo de dados. Incluirá a lógica para construir o JSON conforme a formatação necessária para o MindSphere.

# TODO: Define the data model and functions to create JSON for MindSphere.

# model.py

import json
import uuid

class Model:
    def __init__(self, tenant_id):  # Ensure this matches the argument list
        self.tenant_id = tenant_id
class Variable:
    def __init__(self, name, data_type, quality_code, searchable, unit=None):
        self.name = name
        self.data_type = data_type
        self.quality_code = quality_code
        self.searchable = searchable
        self.unit = unit
        self.reference_id = f"{name}Id"

    def to_dict(self):
        variable_dict = {
            "name": self.name,
            "dataType": self.data_type,
            "qualityCode": self.quality_code,
            "searchable": self.searchable,
            "referenceId": self.reference_id
        }
        if self.unit:
            variable_dict["unit"] = self.unit
        return variable_dict

class AspectType:
    def __init__(self, tenant_id, name, description, variables):
        self.id = f"{tenant_id}.{name}"
        self.name = name
        self.description = description
        self.category = "dynamic"
        self.reference_id = f"{name}ReferenceId"
        self.variables = variables

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "referenceId": self.reference_id,
            "variables": [var.to_dict() for var in self.variables]
        }

# Additional classes for AssetType, Asset, and Mapping would be defined similarly.

class Model:
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id
        self.aspect_types = []
        self.asset_types = []
        self.assets = []
        self.mappings = []

    def add_aspect_type(self, aspect_type):
        self.aspect_types.append(aspect_type)

    # Methods to add asset types, assets, and mappings would go here as well.

    def to_dict(self):
        return {
            "id": str(uuid.uuid4()),
            "data": {
                "typeModel": {
                    "aspectTypes": [aspect_type.to_dict() for aspect_type in self.aspect_types],
                    "assetTypes": [asset_type.to_dict() for asset_type in self.asset_types]
                },
                "instanceModel": {
                    "assets": [asset.to_dict() for asset in self.assets]
                },
                "mappingModel": {
                    "mappings": [mapping.to_dict() for mapping in self.mappings]
                }
            }
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)
# model.py (continuação)

class AssetType:
    def __init__(self, tenant_id, name, description, aspects):
        self.id = f"{tenant_id}.{name}"
        self.name = name
        self.description = description
        self.parent_type_id = "core.basicasset"
        self.reference_id = f"{name}TypeReferenceId"
        self.aspects = aspects

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "parentTypeId": self.parent_type_id,
            "referenceId": self.reference_id,
            "aspects": [aspect.to_dict() for aspect in self.aspects]
        }

class Asset:
    def __init__(self, tenant_id, type_name, name, description):
        self.name = name
        self.type_id = f"{tenant_id}.{type_name}"
        self.parent_reference_id = "root"
        self.description = description
        self.reference_id = f"{name}ReferenceId"

    def to_dict(self):
        return {
            "name": self.name,
            "typeId": self.type_id,
            "parentReferenceId": self.parent_reference_id,
            "description": self.description,
            "referenceId": self.reference_id
        }

class Mapping:
    def __init__(self, aspect_name, variable_name, asset_reference):
        self.aspect_name = aspect_name
        self.variable_name = variable_name
        self.data_point_id = variable_name
        self.asset_reference_id = asset_reference
        self.reference_id = f"{variable_name}MappingReferenceId"

    def to_dict(self):
        return {
            "aspectName": self.aspect_name,
            "variableName": self.variable_name,
            "dataPointId": self.data_point_id,
            "assetReferenceId": self.asset_reference_id,
            "referenceId": self.reference_id
        }

# Expand Model class to handle AssetTypes, Assets, and Mappings
class Model:
    # ... existing content ...

    def add_asset_type(self, asset_type):
        self.asset_types.append(asset_type)

    def add_asset(self, asset):
        self.assets.append(asset)

    def add_mapping(self, mapping):
        self.mappings.append(mapping)

    # ... existing to_dict and to_json methods ...
