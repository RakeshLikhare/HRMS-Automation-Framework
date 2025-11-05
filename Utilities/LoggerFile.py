import logging
import inspect

class LogGenerator:
    @staticmethod
    def loggen():
        name=inspect.stack()[1][3]
        logger=logging.getLogger(name)
        logfile=logging.FileHandler(".\\Logs\\OrangeHRMLogs.log")
        logformate=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s")
        logfile.setFormatter(logformate)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


### logs ke create hone ke bad uska level kaise hota hai --->imp for interview
##debug
##info
##warning
##error
##critical
## ye hota hai level ese he level batana hai sequence me aage piche nhi chalenga guys