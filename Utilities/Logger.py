# import logging
# import inspect
#
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         classname = inspect.stack()[1][3]
#         logger = logging.getLogger(classname)
#         file = logging.FileHandler(
#             "Logs/logfile.log"
#         )
#         format = logging.Formatter(
#             "%(asctime)s: %(levelname)s : %(name)s : %(funcName)s: %(message)s"
#         )
#         file.setFormatter(format)
#         logger.addHandler(file)
#         logger.setLevel(logging.INFO)
#         return logger

import logging
import inspect


class LogGen:
    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]

        logger = logging.getLogger(classname)
        file_handler = logging.FileHandler(
            "Logs/logfile.log", mode="w"
        )  # Use 'w' to overwrite existing log file
        formatter = logging.Formatter(
            "%(asctime)s: %(levelname)s : %(name)s : %(funcName)s: %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

        return logger
