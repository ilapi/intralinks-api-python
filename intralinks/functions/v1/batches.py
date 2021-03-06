"""
For educational purpose only
"""

def get_batch_items(api_client, exchange_id, batch_id):
    raise Exception()
    
def get_batches(api_client, exchange_id, operation_type='Bulk Upload'):
    raise Exception()

def create_batch(api_client, exchange_id, type, size):
    response = api_client.create(
        'services/workspaces/batches', 
        params={
            'workspaceId':exchange_id,
            'operationType':type,
            'batchSize':size
        }, 
        data={'xml':'<batchItemRequest/>'},
        api_version=1
    )
    
    response.check(200, 'text/xml')
    
    data = response.data()
    
    return data