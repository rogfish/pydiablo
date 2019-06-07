import logging

logger = logging.getLogger('pydiablo')
logger.setLevel(logging.DEBUG)
#fh = logging.FileHandler('pydiablo.log')
fh = logging.StreamHandler()
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)
