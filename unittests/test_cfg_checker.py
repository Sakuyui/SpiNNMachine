# Copyright (c) 2014-2023 The University of Manchester
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest
from spinn_utilities.config_holder import run_config_checks
from spinn_machine.config_setup import unittest_setup


class TestCfgChecker(unittest.TestCase):

    def setUp(self):
        unittest_setup()

    def test_cfg_checker(self):
        unittests = os.path.dirname(__file__)
        parent = os.path.dirname(unittests)
        spinn_machine = os.path.join(parent, "spinn_machine")
        run_config_checks(directories=[spinn_machine, unittests])
