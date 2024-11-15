# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from taipy.common.config import Config, Section, _inject_section
from typing import Optional, Dict, Union, Literal
from copy import copy

class RestSection(Section):
    name: str = "REST"

    def __init__(self):
        super().__init__("rest")
        self._port: int = 5000
        self._host: str = "127.0.0.1"
        self._use_https: bool = False
        self._ssl_cert: Optional[str] = None
        self._ssl_key: Optional[str] = None

    def __copy__(self):
        new_instance = RestSection()
        new_instance._port = self._port
        new_instance._host = self._host
        new_instance._use_https = self._use_https
        new_instance._ssl_cert = self._ssl_cert
        new_instance._ssl_key = self._ssl_key
        return new_instance
    
    @property
    def port(self) -> int:
        return self._port

    @port.setter
    def port(self, value: int):
        self._port = value

    @property
    def host(self) -> str:
        return self._host

    @host.setter
    def host(self, value: str):
        self._host = value

    @property
    def use_https(self) -> bool:
        return self._use_https

    @use_https.setter
    def use_https(self, value: bool):
        self._use_https = value

    @property
    def ssl_cert(self) -> Optional[str]:
        return self._ssl_cert

    @ssl_cert.setter
    def ssl_cert(self, value: Optional[str]):
        self._ssl_cert = value

    @property
    def ssl_key(self) -> Optional[str]:
        return self._ssl_key

    @ssl_key.setter
    def ssl_key(self, value: Optional[str]):
        self._ssl_key = value

    def configure_rest(self, port: int = 5000, host: str = "127.0.0.1", use_https: bool = False,
                       ssl_cert: Optional[str] = None, ssl_key: Optional[str] = None):
        self.port = port
        self.host = host
        self.use_https = use_https
        self.ssl_cert = ssl_cert
        self.ssl_key = ssl_key

# At the end of the file
_inject_section(RestSection, "rest", default=RestSection(), configuration_methods=[("configure_rest", RestSection.configure_rest)])

