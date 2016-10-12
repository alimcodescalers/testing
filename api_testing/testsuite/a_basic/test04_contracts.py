from functional_testing.Itsyouonline.api_testing.utils import BaseTest
import types
import unittest


class ContractsTests(BaseTest):

    def setUp(self):
        super(ContractsTests, self).setUp()
        response = self.client.api.GetUserOrganizations(self.user)
        self.lg('GetUserOrganizations [%s] response [%s]' % (self.user, response.json()))
        self.assertEqual(response.status_code, 200)
        organization_id = response.json()['owner'][0]
        response = self.client.api.GetOrganizationContracts(organization_id)
        self.assertEqual(response.status_code, 200)
        self.contractId = response.json()[0]
        self.lg('contractId %s' % self.contractId)

    #Currently fail due to issue https://github.com/itsyouonline/identityserver/issues/233
    @unittest.skip("fail due to issue https://github.com/itsyouonline/identityserver/issues/233")
    def test001_get_contracts(self):
        """ ITSYOU-023
        *Test case for check get a contract GET /contracts/{contractId}.*

        **Test Scenario:**

        #. check get a contract, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        response = self.client.api.GetContract(self.contractId)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), types.DictType)
        self.lg('%s ENDED' % self._testID)