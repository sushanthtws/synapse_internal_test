import logging


class Logger:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )
        self.logger = logging.getLogger("skill-repo")

    def info(self, msg: str):
        self.logger.info(msg)

    def error(self, msg: str):
        self.logger.error(msg)


logger = Logger()