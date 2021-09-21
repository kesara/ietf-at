from logging import getLogger
from subprocess import run as proc_run, CalledProcessError

from xml2rfc import __version__ as xml2rfc_version


def get_kramdown_rfc2629_version(logger=getLogger()):
    '''Return kramdown-rfc2629 version'''

    output = proc_run(
                args=['kramdown-rfc2629', '--version'],
                capture_output=True)

    try:
        output.check_returncode()
        return output.stdout.decode('utf-8').replace(
                'kramdown-rfc2629', '').strip()
    except CalledProcessError:
        logger.info('kramdown-rfc2629 error: {}'.format(
            output.stderr.decode('utf-8')))
        return None


def get_id2xml_version(logger=getLogger()):
    '''Return id2xml version'''

    output = proc_run(args=['id2xml', '--version'], capture_output=True)

    try:
        output.check_returncode()
        return output.stdout.decode('utf-8').replace('id2xml', '').strip()
    except CalledProcessError:
        logger.info('id2xml error: {}'.format(
            output.stderr.decode('utf-8')))
        return None


def get_xml2rfc_version():
    '''Return xml2rfc version'''

    return xml2rfc_version