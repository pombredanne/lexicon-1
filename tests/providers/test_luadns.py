# Test for one implementation of the interface
from lexicon.providers.luadns import Provider
from integration_tests import IntegrationTests
from unittest import TestCase
import pytest

# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from define_tests.TheTests
class LuaDNSProviderTests(TestCase, IntegrationTests):

    Provider = Provider
    provider_name = 'luadns'
    domain = 'capsulecd.com'
    def _filter_headers(self):
        return ['Authorization']

    @pytest.mark.skip(reason="CNAME requires FQDN for this provider")
    def test_Provider_when_calling_create_record_for_CNAME_with_valid_name_and_content(self):
        return