import intralinks_test.user_accounts_helper

def test_user_accounts(v1_client, test_data):
    intralinks_test.user_accounts_helper.test_user_accounts(v1_client, test_data)
