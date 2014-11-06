# Copyright 2014 Xinyu, He <legendmohe@foxmail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import logging
import logging.handlers

file_name = 'log/home_debug.log'
debug_logger = logging.getLogger('DebugLog')
handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=50*1024*1024)
formatter = logging.Formatter("[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s")
handler.setFormatter(formatter)
debug_logger.setLevel(logging.DEBUG)
debug_logger.addHandler(handler)
debug_logger.propagate = False # now if you use logger it will not log to console.

comm_name = 'log/home.log'
comm_logger = logging.getLogger('CommonLog')
handler = logging.handlers.RotatingFileHandler(comm_name, maxBytes=20*1024*1024)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s [%(filename)s] ')
handler.setFormatter(formatter)
comm_logger.setLevel(logging.INFO)
comm_logger.addHandler(handler)
comm_logger.propagate = False # now if you use logger it will not log to console.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# def stack_info_debug(info):
#     stack_info = inspect.currentframe().f_back.f_code.co_name
#     debug_logger.debug("%s:  %s" % (stack_info, info))

DEBUG = debug_logger.debug
# DEBUG    = stack_info_debug # only output to file
INFO     = comm_logger.info
WARN     = comm_logger.warning
ERROR    = comm_logger.error
CRITICAL = comm_logger.critical

FDEBUG    = debug_logger.debug
FINFO     = debug_logger.info
FWARN     = debug_logger.warning
FERROR    = debug_logger.error
FCRITICAL = debug_logger.critical

