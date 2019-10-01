#! usr/bin/env python3.7
# -*- coding: utf-8 -*-

# ref 1. https://qiita.com/amedama/items/b856b2f30c2f38665701
# ref 2. https://qiita.com/__init__/items/91e5841ed53d55a7895e
# ref 3. https://docs.python.org/ja/3/library/logging.html
# ref 4. https://qiita.com/toriwasa/items/fa8371c3b98aa993a2fc
# ref 5. https://qiita.com/abeken0713/items/77420c8c05e53628199a

from logging import basicConfig, getLogger, CRITICAL, ERROR, WARNING, INFO, DEBUG
import sys

# このスクリプト本体のロガーを取得してログレベルを設定する
logger = getLogger(__name__)
logger.setLevel(DEBUG)

# これはメインのファイルにのみ書く
#basicConfig(level=CRITICAL)
#basicConfig(level=ERROR)
#basicConfig(level=WARNING)
#basicConfig(level=INFO)
#basicConfig(level=DEBUG)

# これはすべてのファイルに書く
#logger = getLogger(__name__)

def test_output():
    funcName = sys._getframe().f_code.co_name
    logger.critical('critical: ' + funcName)
    logger.error('error: ' + funcName)
    logger.warning('warning: ' + funcName)
    logger.info('info: ' + funcName)
    logger.debug('hello: ' + funcName)

if __name__ == "__main__":
    # このスクリプトから呼び出されるモジュール全体のログ設定を行う
    basicConfig(
        format='[%(asctime)s] %(name)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger.critical('critical')
    logger.error('error')
    logger.warning('warning')
    logger.info('info')
    funcName = sys._getframe().f_code.co_name
    logger.debug('hello: ' + funcName)

    test_output()

# Ex. execute and output
# mocha@hoto:~/Github/python_debug_test$ python3 ./test_logger.py 
# [2019-10-01 12:13:54] __main__ CRITICAL: critical
# [2019-10-01 12:13:54] __main__ ERROR: error
# [2019-10-01 12:13:54] __main__ WARNING: warning
# [2019-10-01 12:13:54] __main__ INFO: info
# [2019-10-01 12:13:54] __main__ DEBUG: hello: <module>
# [2019-10-01 12:13:54] __main__ CRITICAL: critical: test_output
# [2019-10-01 12:13:54] __main__ ERROR: error: test_output
# [2019-10-01 12:13:54] __main__ WARNING: warning: test_output
# [2019-10-01 12:13:54] __main__ INFO: info: test_output
# [2019-10-01 12:13:54] __main__ DEBUG: hello: test_output
