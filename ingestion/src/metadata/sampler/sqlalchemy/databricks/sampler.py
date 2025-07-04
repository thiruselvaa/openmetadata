#  Copyright 2025 Collate
#  Licensed under the Collate Community License, Version 1.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  https://github.com/open-metadata/OpenMetadata/blob/main/ingestion/LICENSE
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
Helper module to handle data sampling for the profiler
"""
from metadata.ingestion.source.database.databricks.connection import (
    get_connection as databricks_get_connection,
)
from metadata.sampler.sqlalchemy.sampler import SQASampler


class DatabricksSamplerInterface(SQASampler):
    def get_client(self):
        """client is the session for SQA"""
        self.connection = databricks_get_connection(self.service_connection_config)
        client = super().get_client()
        self.set_catalog(client)
        return client
